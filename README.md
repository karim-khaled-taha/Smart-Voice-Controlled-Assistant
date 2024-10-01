# Smart Voice-Controlled Assistant with Arduino Integration

## Project Overview

This project is a smart voice-controlled assistant that can perform various tasks using voice commands. It is designed to interact with a variety of devices such as TVs, lights, and doors, all controlled through voice commands and Arduino. The assistant listens for a wake word ("Hey Siri") and then responds to various commands to control devices, search the web, and perform other tasks.

### Key Features
- **Voice Commands**: Recognizes specific voice commands to perform actions.
- **Wake Word**: The assistant listens for the wake word ("Hey Siri") to activate.
- **Arduino Integration**: Controls external devices like lights, doors, and TV using an Arduino connected via serial communication.
- **Google Search**: Performs Google searches and location searches through voice input.
- **gTTS and pyttsx3**: Uses Google Text-to-Speech (gTTS) and pyttsx3 to provide voice feedback.
- **Error Handling**: Manages common errors like unknown input, timeouts, and speech recognition failures.

---

## Components and Libraries

### 1. **Speech Recognition (`speech_recognition` library)**
   - Used to capture and recognize voice input from the user.
   - The program listens for the wake word ("Hey Siri") to initiate listening for commands.
   - It uses Google’s speech-to-text engine to interpret voice commands.

### 2. **Text-to-Speech (`pyttsx3` and `gTTS`)**
   - **`pyttsx3`**: Converts text into speech without needing an internet connection.
   - **`gTTS`**: Google’s text-to-speech service, which is used to convert the assistant’s responses into speech.
   - The assistant uses pyttsx3 by default, but `gTTS` can be enabled as an option.

### 3. **Serial Communication (`serial` library)**
   - Used to communicate with an Arduino connected to a computer via a serial port (e.g., `COM4`).
   - Arduino receives commands to control devices such as TVs, lights, and doors.

### 4. **Web Browser (`webbrowser` library)**
   - Opens a web browser to perform searches or find locations on Google Maps based on the user's voice input.
   - The assistant uses voice prompts to ask the user what they want to search for or locate.

### 5. **Playsound (`playsound` library)**
   - Plays audio feedback from `gTTS` responses.
   - Audio files are temporarily saved and played, then deleted.

---

## Hardware Connection 
- Used The Relay as the switch To Conect the TV and Light and other wit the 220v AC
- ex for Light
  
![WhatsApp Image 2024-09-30 at 08 56 17_4d198f6c](https://github.com/user-attachments/assets/4f93b7ca-ea38-4b26-a0a8-595ef3ab8a18)


