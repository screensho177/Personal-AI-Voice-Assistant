import os
from dotenv import load_dotenv
from deepgram import DeepgramClient, SpeakOptions
import sounddevice as sd
import soundfile as sf

load_dotenv()

class TTS:
    def __init__(self):
        self.filename = "output.wav"
    
    def speak(self, text):
        try:
            # STEP 1: Create a Deepgram client using the API key from environment variables
            deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

            # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
            options = SpeakOptions(
                model="aura-asteria-en",
                encoding="linear16",
                container="wav"
            )

            # STEP 3: Call the save method on the speak property
            SPEAK_OPTIONS = {"text": text}
            response = deepgram.speak.v("1").save(self.filename, SPEAK_OPTIONS, options)

            # STEP 4: Play the audio file
            data, samplerate = sf.read(self.filename, dtype="float32")
            sd.play(data, samplerate)
            sd.wait()

        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    tts = TTS()
    tts.speak("Hello, how can I help you today?")
