import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Alright, let's get Jarvis ready to listen and talk
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    # Jarvis opens his mouth here
    engine.say(text)
    engine.runAndWait()

# ------------------ Ears ------------------
def listen_command():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        # Give him a second to adjust to the room noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Try to make sense of what was said
        command = recognizer.recognize_google(audio).lower()
        print("👉 You said:", command)
        return command
    except:
        # Couldn't catch that, just move on
        return ""

# ------------------ Open Chrome and search something ------------------
def search_in_chrome(query):
    # Point this to wherever Chrome lives on your machine
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.get(f'"{chrome_path}" %s').open(url)

# ------------------ The brain — figures out what to do ------------------
def execute_task(command):

    # All the apps Jarvis knows how to open — add yours here
    apps = {
        "valorant": "valorant.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "spotify": "Spotify.exe",
        "vs code": r"C:\Users\Ranvijay\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "dev c plus plus": "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
    }

    # Websites Jarvis can open straight away
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
        "linkedin": "https://www.linkedin.com/in/ranvijay-suryawanshi-739a47315/"
    }

    # If the command starts with "search", just go look it up
    if command.startswith("search "):
        search_query = command.replace("search ", "", 1)
        speak(f"Searching for {search_query} in Chrome.")
        search_in_chrome(search_query)
        return

    # Heavy stuff — turning off or restarting the PC
    if "shutdown" in command:
        speak("Shutting down your computer, boss.")
        os.system("shutdown /s /t 1")
        return
    elif "restart" in command:
        speak("Restarting your computer, boss.")
        os.system("shutdown /r /t 1")
        return
    elif "log off" in command or "logout" in command:
        speak("Logging off, boss.")
        os.system("shutdown /l")
        return

    # Scan through the app list and open whichever one matches
    for app in apps:
        if app in command:
            speak(f"Opening {app}")
            os.startfile(apps[app])
            return

    # Same thing but for websites
    for site in websites:
        if site in command:
            speak(f"Opening {site}")
            webbrowser.open(websites[site])
            return

    # Didn't match anything, so just Google it and hope for the best
    speak("Command not recognized.")
    speak(f"Searching for {command} in Chrome.")
    search_in_chrome(command)

# ------------------ Wrapping up — asking if there's anything else ------------------
def ask_follow_up():
    

    try:
        with sr.Microphone() as source:
            print("🎤 Listening for follow-up...")
            # A little pause to filter out background noise
            recognizer.adjust_for_ambient_noise(source)
            # Wait 5 seconds — if nothing comes, assume we're done
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        response = recognizer.recognize_google(audio).lower()
        print("👉 You said:", response)
        return response
    except:
        # Silence or couldn't understand — treat it as a no
        return "no"

# ------------------ Where everything kicks off ------------------
def main():
    print("🚀 Say 'Hey Jarvis' to activate...")
    command = listen_command()

    # Wake up only when the boss calls
    if "hey jarvis" in command or "jarvis" in command:
        speak("How may I help you, boss?")
        task_command = listen_command()
        execute_task(task_command)

        # Task done — now politely check if there's more to do
        speak("Sure sir, anything else I can help you with?")
        follow_up = ask_follow_up()

        if "no" in follow_up or follow_up == "":
            # Boss said no or went quiet — time to sign off
            speak("Sure Boss, Glad to help.")
            print("🛑 Task completed. Stopping program.")
        else:
            # Got another command — handle it then say goodbye
            execute_task(follow_up)
            speak("Sure Boss, Glad to help.")
            print("🛑 Task completed. Stopping program.")

if __name__ == "__main__":
    main()