 Python Voice Assistant

A simple Python-based voice assistant that listens to spoken commands through a microphone, understands the user's request, performs useful actions, and responds using text-to-speech.

The project demonstrates the use of speech recognition, text-to-speech, date/time handling, web browser automation, functions, loops, and error handling in Python.

---

 Project Overview

The Python Voice Assistant is designed to provide basic hands-free interaction with a computer.

The assistant can:

-  Capture voice commands through a microphone
-  Respond to greetings such as "Hello" and "Hi"
- Tell the current time
- Tell the current date
- Search the web for a user-specified topic
- Respond using text-to-speech
- Handle situations where speech is not understood
- Exit when the user says "Goodbye", "Quit", "Stop", or "Exit"

---

 Project Objectives

The main objectives of this project are to:

1. Capture voice input using a computer microphone.
2. Convert spoken commands into text using the "SpeechRecognition" library.
3. Process the recognized commands using Python.
4. Provide predefined responses to common commands.
5. Retrieve the current date and time.
6. Perform web searches based on user requests.
7. Convert text responses into speech using "pyttsx3".
8. Implement graceful error handling when speech cannot be understood.

---

Technologies Used

Technology| Purpose
Python| Main programming language
SpeechRecognition| Converts speech into text
PyAudio| Provides microphone/audio input
pyttsx3| Converts text into speech
datetime| Retrieves current date and time
webbrowser| Opens web searches in the browser

---

Features

1.  Voice Input

The assistant uses the computer's microphone to capture the user's voice.

with sr.Microphone() as source:
    audio = recognizer.listen(source)

The captured audio is then converted into text.

---

2. Greeting Response

The assistant recognizes greetings such as:

Hello
Hi

and responds with a predefined greeting.

Example:

User: Hello

Assistant: Hello! Nice to hear from you. How can I help you?

---

3. Current Time

The user can ask:

What is the time?

The assistant retrieves the current system time using Python's "datetime" module.

Example:

User: What is the time?

Assistant: The current time is 10:35 PM.

---

4. Current Date

The assistant can also provide the current date.

Example:

User: What is today's date?

Assistant: Today is Thursday, September 24, 2026.

---

5. Web Search

The user can request a web search by saying:

Search Python programming

The assistant extracts the search topic and opens the search in the default web browser.

For example:

User: Search Python data structures

Assistant: Searching the web for Python data structures.

The browser then opens the corresponding Google search.

---

6. Text-to-Speech

The assistant uses "pyttsx3" to provide spoken feedback.

The main function is:

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

This allows the assistant to speak its responses instead of only displaying them on the screen.

---

7. Graceful Error Handling

The program handles situations where the user's speech cannot be understood.

For example:

except sr.UnknownValueError:
    speak("Sorry, I could not understand you. Please repeat.")

Instead of crashing, the assistant asks the user to repeat the command.

The project also handles:

- No speech detected
- Speech recognition service errors
- Unexpected errors

---

Requirements

Before running the project, make sure you have:

- Python 3.x
- A working microphone
- Speakers or headphones
- Internet connection for Google speech recognition and web searches
- A web browser

---

 Installation

Step 1: Clone the project

git clone https://github.com/your-username/voice-assistant.git

Move into the project directory:

cd voice-assistant

Step 2: Install dependencies

Run:

pip install SpeechRecognition pyttsx3 PyAudio

If "PyAudio" is already installed, you do not need to install it again.

---

How to Run

Run the Python file:

python voice_assistant.py

The assistant will start and provide an introductory message.

You can then speak commands into your microphone.

---

Example Commands

Voice Command| Action
"Hello"| Gives a greeting
"Hi"| Gives a greeting
"What is the time?"| Tells the current time
"What is today's date?"| Tells the current date
"Search Python"| Searches Google for Python
"Search data structures"| Searches Google for data structures
"Goodbye"| Stops the assistant
"Quit"| Stops the assistant
"Stop"| Stops the assistant
"Exit"| Stops the assistant

---

 Project Structure

Voice_Assistant/
│
├── voice_assistant.py
├── README.md
└── requirements.txt

"voice_assistant.py"

Contains the complete Python voice assistant program.

"README.md"

Contains the project documentation and instructions.

"requirements.txt"

Contains the Python libraries required by the project.

Example:

SpeechRecognition
pyttsx3
PyAudio

---

 How the System Works

The basic operation of the assistant is:

             ┌─────────────────┐
             │      User       │
             │  Speaks Command │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   Microphone    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ SpeechRecognition│
             │  Speech → Text  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Command         │
             │ Processing      │
             └────────┬────────┘
                      │
          ┌───────────┼────────────┐
          ▼           ▼            ▼
       Time/Date    Greeting    Web Search
          │           │            │
          └───────────┼────────────┘
                      ▼
             ┌─────────────────┐
             │    pyttsx3      │
             │    Text → Speech│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Assistant Speaks│
             └─────────────────┘

---

Main Python Concepts Demonstrated

This project demonstrates several important Python concepts:

- Importing libraries
- Variables
- Functions
- Conditional statements
- "if", "elif", and "else"
- "while" loops
- Exception handling
- String manipulation
- User input processing
- Working with dates and times
- Browser automation
- Object-oriented library usage

---

 Error Handling

The assistant uses Python's "try" and "except" statements to prevent the program from terminating unexpectedly.

Example:

try:
    audio = recognizer.listen(source)
    command = recognizer.recognize_google(audio)

except sr.UnknownValueError:
    speak("Sorry, I could not understand you. Please repeat.")

except sr.RequestError:
    speak("Sorry, the speech recognition service is unavailable.")

This makes the application more reliable and user-friendly.

---

 Future Improvements

The project can be expanded with additional features such as:

-  Search YouTube
-  Play music
-  Send emails
-  Check weather
-  Perform calculations
-  Answer general questions
-  Read news
-  Add user authentication
-  Support multiple languages
-  Create a graphical user interface
-  Integrate an AI model
-  Control smart-home devices

These features can gradually transform the basic assistant into a more advanced personal assistant.

---

 Privacy Note

The assistant uses a microphone to capture voice commands.

Users should understand that the "SpeechRecognition" configuration used in this project relies on an online speech-recognition service, so an internet connection is required for speech recognition.

Avoid using the assistant for sensitive or confidential information unless the speech-recognition setup has been changed to an appropriate offline solution.

---

 Learning Purpose

This project was created as a practical Python learning project to demonstrate how different Python libraries can work together to create a useful application.

It is suitable for students who are learning:

- Python programming
- Automation
- Speech recognition
- Human-computer interaction
- Basic software development

---

Author

Douglas Adjei

Computer Engineering Student

Project

Python-Based Voice Assistant

---

 License

This project is intended for educational and personal learning purposes.

You are free to modify and improve the project for learning and development.