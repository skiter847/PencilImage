from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .tasks import convert_to_pencil
from celery import current_app


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):

    def get(self, request):
        return render(request, 'home/base.html')

    def post(self, request):
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            fs = FileSystemStorage()
            filename = fs.save(image.name.replace(' ', ''), image)
            uploaded_file_url = fs.url(filename)
            task = convert_to_pencil.delay(uploaded_file_url)
            return JsonResponse({'task_id': task.id}, safe=False)


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response = {'task_status': task.status}
        if task.status == 'SUCCESS':
            response['path_to_img'] = task.get()

        return JsonResponse(response)
