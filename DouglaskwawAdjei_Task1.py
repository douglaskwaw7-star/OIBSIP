import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# ---------------------------------------
# INITIALIZE TEXT-TO-SPEECH ENGINE
# ---------------------------------------

engine = pyttsx3.init()

# Set speaking speed

engine.setProperty("rate", 170)

# Set volume
engine.setProperty("volume", 1.0)


# ---------------------------------------
# TEXT-TO-SPEECH FUNCTION
# ---------------------------------------

def speak(text):
    """Speak the given text."""
    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()


# ---------------------------------------
# CAPTURE VOICE INPUT
# ---------------------------------------

def listen():
    """Listen to the user's voice and convert it to text."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        # Adjust microphone for surrounding noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("Processing...")

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""

        except Exception as error:
            print("Error:", error)
            speak("Something went wrong. Please try again.")
            return ""


# ---------------------------------------
# GET CURRENT TIME
# ---------------------------------------

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak("The current time is " + current_time)


# ---------------------------------------
# GET CURRENT DATE
# ---------------------------------------

def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%A, %B %d, %Y"
    )

    speak("Today is " + current_date)


# ---------------------------------------
# WEB SEARCH
# ---------------------------------------

def search_web(topic):

    speak("Searching the web for " + topic)

    url = "https://www.google.com/search?q=" + topic.replace(" ", "+")

    webbrowser.open(url)


# ---------------------------------------
# PROCESS COMMAND
# ---------------------------------------

def process_command(command):

    if command == "":
        return True

    # -----------------------------------
    # HELLO
    # -----------------------------------

    if "hello" in command or "hi" in command:

        speak("Hello! Nice to hear from you. How can I help you?")


    # -----------------------------------
    # TIME
    # -----------------------------------

    elif "time" in command:

        tell_time()


    # -----------------------------------
    # DATE
    # -----------------------------------

    elif "date" in command or "today" in command:

        tell_date()


    # -----------------------------------
    # WEB SEARCH
    # -----------------------------------

    elif "search" in command:

        # Remove the word "search"
        topic = command.replace("search", "").strip()

        if topic:

            search_web(topic)

        else:

            speak("What would you like me to search for?")


    # -----------------------------------
    # EXIT
    # -----------------------------------

    elif (
        "exit" in command
        or "quit" in command
        or "stop" in command
        or "goodbye" in command
    ):

        speak("Goodbye! Have a great day.")

        return False


    # -----------------------------------
    # UNKNOWN COMMAND
    # -----------------------------------

    else:

        speak(
            "I don't understand that command. "
            "You can say hello, ask for the time, "
            "ask for the date, or say search followed by a topic."
        )

    return True


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

def main():

    speak(
        "Voice assistant started. "
        "You can say hello, ask for the time or date, "
        "or ask me to search the web."
    )

    running = True

    while running:

        command = listen()

        running = process_command(command)


# ---------------------------------------
# START PROGRAM
# ---------------------------------------

if __name__ == "__main__":
    main()
