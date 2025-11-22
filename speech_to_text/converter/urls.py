from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/transcription/<int:audio_id>/', views.get_transcription, name='get_transcription'),
    path('delete/<int:audio_id>/', views.delete_audio, name='delete_audio'),
]
