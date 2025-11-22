from django.contrib import admin
from .models import AudioFile

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_at', 'is_processed', 'transcription_preview']
    list_filter = ['is_processed', 'uploaded_at']
    search_fields = ['transcription']
    readonly_fields = ['uploaded_at', 'transcription', 'error_message']
    
    def transcription_preview(self, obj):
        if obj.transcription:
            return obj.transcription[:50] + '...' if len(obj.transcription) > 50 else obj.transcription
        return 'Pending...'
    transcription_preview.short_description = 'Transcription'
