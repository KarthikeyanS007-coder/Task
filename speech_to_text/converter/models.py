from django.db import models

class AudioFile(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    transcription = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Audio - {self.uploaded_at}"

    class Meta:
        ordering = ['-uploaded_at']
