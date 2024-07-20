import webbrowser
import datetime
import os
from assistant.speech import speak

def perform_task(command):
    if "open" in command and "google" in command:
        speak("Opening Google.")
        webbrowser.open("http://www.google.com")
    elif "open" in command and "youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("http://www.youtube.com")
    elif "open" in command and "facebook" in command:
        speak("Opening facebook.")
        webbrowser.open("http://www.facebook.com")
    elif "open" in command and "bookmyshow" in command:
        speak("Opening bookmyshow.")
        webbrowser.open("http://www.bookmyshow.com")
    elif "open" in command and "linkedin" in command:
        speak("Opening linkedin.")
        webbrowser.open("http://www.linkedin.com")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        if search_query:
            speak(f"Searching for {search_query} on Google.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please specify what you want to search for.")
    elif "play music" in command:
        speak("Playing music.")
        music_file = "path/to/your/music/file.mp3"
        os.system(f"start {music_file}")  # For Windows
        # os.system(f"open {music_file}")  # For MacOS
        # os.system(f"xdg-open {music_file}")  # For Linux
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}.")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}.")
    else:
        speak("Sorry, I can't perform that task.")

def is_exit_command(command):
    return "exit" in command or "quit" in command or "stop" in command
