from django import forms
from .models import AudioFile

class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['audio_file']
        widgets = {
            'audio_file': forms.FileInput(attrs={
                'accept': 'audio/wav,.wav',
                'class': 'form-control',
            })
        }
