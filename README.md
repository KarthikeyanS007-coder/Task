# Audio-to-text
# Audio-to-Text Django Project

This Django project allows users to upload a `.wav` audio file and converts the speech in the audio to text using **Google's Speech Recognition API** via the `SpeechRecognition` Python library.

---

## Features

- Upload `.wav` audio files via a web interface.
- Convert audio to text using **speech recognition**.
- Display the converted text on the webpage.
- Temporary storage of uploaded audio files in the `media/` folder.
- Simple, lightweight, and easy-to-use interface.

---

## Prerequisites

- Python 3.10+ installed.
- `pip` package manager.
- FFmpeg installed and added to the system PATH (required by `pydub` if you later want to support other audio formats).

---

## Installation

1. **Clone or download the project**:

```bash
git clone <your-repo-url>
cd audio_to_text
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
audio_to_text/
├── audio_to_text/           # Project settings
├── converter/               # App for audio conversion
│   ├── templates/converter/
│   │   └── index.html       # Upload form and result page
│   ├── forms.py             # Django form for file upload
│   └── views.py             # Handles file upload and conversion
├── media/                   # Temporary storage for uploaded files
├── manage.py
└── requirements.txt
