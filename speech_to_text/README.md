# Speech to Text Converter - Django Application

A Django web application that accepts `.wav` audio files from users and converts them to text using Google's Speech Recognition API.

## Features

- 🎤 Upload WAV audio files through a web interface
- 🔄 Automatic speech-to-text conversion using Google Speech Recognition
- 📝 View transcription history
- ⚡ Real-time status updates
- 🗑️ Delete audio files and transcriptions
- 📱 Responsive Bootstrap UI
- 🗄️ SQLite database for storing audio metadata

## Project Structure

```
speech_to_text/
├── converter/                 # Main Django app
│   ├── migrations/           # Database migrations
│   ├── models.py            # AudioFile model
│   ├── views.py             # View functions
│   ├── forms.py             # Audio upload form
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Admin interface
│   └── apps.py              # App configuration
├── speech_to_text/          # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── __init__.py
├── templates/
│   └── converter/
│       └── index.html       # Upload and results page
├── media/                   # Uploaded audio files (created during first run)
├── static/                  # Static files (CSS, JS)
├── manage.py                # Django CLI
└── requirements.txt         # Python dependencies
```

## Installation

### 1. Clone or Download the Project
```bash
cd speech_to_text
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional - for Django Admin)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage

1. **Upload Audio**: Click the upload area or drag & drop a `.wav` file
2. **Convert**: Click "Convert to Text" button
3. **View Results**: Wait for the transcription to complete
4. **Manage History**: Delete files as needed

## How It Works

1. User uploads a `.wav` audio file through the web interface
2. The file is saved to the `media/audio/` directory
3. `SpeechRecognition` library processes the audio using Google's Speech Recognition API
4. The transcribed text is stored in the database
5. Results are displayed on the page with auto-refresh

## API Endpoints

- `GET /` - Main page with upload form and history
- `POST /` - Upload audio file
- `GET /api/transcription/<audio_id>/` - Check transcription status (JSON)
- `GET /delete/<audio_id>/` - Delete an audio file

## Admin Interface

Access Django Admin at: `http://127.0.0.1:8000/admin/`
- Username and password set during superuser creation
- Manage audio files and transcriptions

## Dependencies

- **Django 4.2.7** - Web framework
- **SpeechRecognition 3.10.0** - Speech-to-text library
- **pydub 0.25.1** - Audio processing library (required by SpeechRecognition)

## Supported Audio Formats

- `.wav` (WAV/PCM format)

## Requirements

- Python 3.8+
- Internet connection (for Google Speech Recognition API)
- FFmpeg (optional, for audio format conversion)

## Troubleshooting

### "Could not understand the audio"
- Check if the audio quality is good
- Ensure the speech is clear
- Try with a different audio file

### "Error with speech recognition service"
- Check your internet connection
- The Google Speech Recognition API may be temporarily unavailable
- Try again later

### "Module not found" errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify virtual environment is activated

## Performance Notes

- Audio processing is done synchronously (blocks the request)
- For production, consider using Celery for asynchronous task processing
- Large audio files may take longer to process

## Production Deployment

For production use:

1. Set `DEBUG = False` in `settings.py`
2. Change `SECRET_KEY` to a secure random value
3. Add domain to `ALLOWED_HOSTS`
4. Use a production-grade database (PostgreSQL recommended)
5. Set up proper static/media file serving
6. Use a WSGI server (Gunicorn, uWSGI)
7. Consider implementing task queue (Celery) for audio processing

## Future Enhancements

- Support for more audio formats (MP3, OGG, etc.)
- Batch processing multiple files
- Export transcriptions to text/PDF
- Language selection
- Alternative STT engines (Azure, AWS, etc.)
- Asynchronous processing with progress tracking
- User authentication and file privacy

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please check the Django documentation:
- Django: https://docs.djangoproject.com/
- SpeechRecognition: https://github.com/Uberi/speech_recognition
