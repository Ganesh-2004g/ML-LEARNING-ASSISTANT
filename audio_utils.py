from gtts import gTTS
import os
from datetime import datetime

AUDIO_FOLDER = "outputs/audio"

def text_to_audio(text):
    """
    Converts text into MP3 audio
    """
    os.makedirs(AUDIO_FOLDER, exist_ok=True)

    filename = f"audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    tts = gTTS(text=text, lang="en")
    tts.save(filepath)

    return filepath
