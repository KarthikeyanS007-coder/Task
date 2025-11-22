import speech_recognition as sr
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import AudioFile
from .forms import AudioUploadForm
import os

def index(request):
    """Display the upload form and list of previous transcriptions"""
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.save()
            # Convert to text
            transcribe_audio(audio)
            return redirect('index')
    else:
        form = AudioUploadForm()
    
    # Get all audio files
    audio_files = AudioFile.objects.all()
    
    context = {
        'form': form,
        'audio_files': audio_files,
    }
    return render(request, 'converter/index.html', context)

def transcribe_audio(audio_obj):
    """Convert audio file to text using speech recognition"""
    recognizer = sr.Recognizer()
    
    try:
        # Get the file path
        audio_path = audio_obj.audio_file.path
        
        # Load the audio file
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
        
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        audio_obj.transcription = text
        audio_obj.is_processed = True
        
    except sr.UnknownValueError:
        audio_obj.error_message = "Could not understand the audio"
        audio_obj.is_processed = True
    except sr.RequestError as e:
        audio_obj.error_message = f"Error with speech recognition service: {str(e)}"
        audio_obj.is_processed = True
    except Exception as e:
        audio_obj.error_message = f"Error processing audio: {str(e)}"
        audio_obj.is_processed = True
    
    audio_obj.save()

def get_transcription(request, audio_id):
    """API endpoint to get transcription status"""
    audio = get_object_or_404(AudioFile, id=audio_id)
    
    if audio.is_processed:
        return JsonResponse({
            'status': 'completed',
            'transcription': audio.transcription or '',
            'error': audio.error_message or '',
        })
    else:
        return JsonResponse({'status': 'processing'})

def delete_audio(request, audio_id):
    """Delete an audio file"""
    audio = get_object_or_404(AudioFile, id=audio_id)
    
    # Delete the file from storage
    if audio.audio_file:
        if os.path.exists(audio.audio_file.path):
            os.remove(audio.audio_file.path)
    
    audio.delete()
    return redirect('index')
