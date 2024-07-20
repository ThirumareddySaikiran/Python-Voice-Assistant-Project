import speech_recognition as sr
from assistant.speech import speak
from assistant.tasks import perform_task, is_exit_command

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
        return ""

    def run(self):
        speak("How can I assist you today?")
        while True:
            command = self.listen()
            if command:
                if is_exit_command(command):
                    speak("Goodbye!")
                    break
                perform_task(command)
