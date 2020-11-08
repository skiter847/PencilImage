from django.conf.urls.static import static
from django.urls import path

from PencilImage import settings
from .views import HomeView, TaskView

urlpatterns = [
    path('', HomeView.as_view()),
    path('task/<str:task_id>', TaskView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
