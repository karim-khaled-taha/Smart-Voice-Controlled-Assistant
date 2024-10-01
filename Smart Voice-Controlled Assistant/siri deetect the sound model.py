import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
import datetime
import serial
import pyttsx3

# Initialize speech recognizer, text-to-speech engine, and serial connection
recognizer = sr.Recognizer()
engine = pyttsx3.init()
ser = serial.Serial('COM4', 9600)  # Change COM4 to your Arduino's port

# Set up wake word
WAKE_WORD = "hey siri"

# Function to speak with pyttsx3 or gTTS
def siri_speak(audio_string, use_gTTS=False):
    if use_gTTS:
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 1000000)
        audio_file = f'audio{r}.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)
    else:
        engine.say(audio_string)
        engine.runAndWait()
    print(audio_string)  # Print the spoken text

# Function to send command to Arduino
def send_command(command):
    ser.write(command.encode())

# Function to record voice input
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            siri_speak(ask)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for background noise
        print("Listening...")
        try:
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Increase timeout
            voice_data = recognizer.recognize_google(audio_data, language="en")
            return voice_data.lower()  # Ensure voice data is in lowercase for comparison
        except sr.UnknownValueError:
            siri_speak('Sorry, I did not get that')
        except sr.RequestError:
            siri_speak('Sorry, my speech service is down')
        except sr.WaitTimeoutError:
            siri_speak("I didn't hear anything, please try again.")
        return ''  # Return empty string if no voice data is captured

# Function to handle voice commands
def respond(voice_data):
    if 'what is your name' in voice_data:
        siri_speak('My name is Siri', use_gTTS=False)
    if 'what time is it' in voice_data:
        siri_speak(datetime.datetime.now().strftime("%H:%M:%S"), use_gTTS=False)
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        siri_speak(f'Here is what I found for {search}', use_gTTS=False)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = f'https://google.nl/maps/place/{location}'
        webbrowser.get().open(url)
        siri_speak(f'Here is the location of {location}', use_gTTS=False)
    if 'open download' in voice_data:
        os.startfile("D:\DOWNLOAD")
    if 'turn on TV' in voice_data:
        send_command("1")
        siri_speak("The TV is turning on")
    if 'turn off TV' in voice_data:
        send_command("2")
        siri_speak("The TV is turning off")
    if 'open the door' in voice_data:
        send_command("3")
        siri_speak("The door is opening")
    if 'close the door' in voice_data:
        send_command("4")
        siri_speak("The door is closing")
    if 'turn on light' in voice_data:
        send_command("5")
        siri_speak("The light is turning on")
    if 'turn off light' in voice_data:
        send_command("6")
        siri_speak("The light is turning off")
    if 'go to sleep' in voice_data or 'exit' in voice_data:
        siri_speak('OKey', use_gTTS=False)
        exit()

# Main loop to continuously listen and respond
time.sleep(1)

while True:
    # Step 1: Listen for the wake word
    print("Listening for wake word...")
    voice_data = record_audio()

    # Step 2: If the wake word is detected, respond and be ready for commands
    if WAKE_WORD in voice_data:
        siri_speak("Yes, I am listening", use_gTTS=False)
        siri_speak('How can I help you?', use_gTTS=False)

        # Step 3: Enter command mode and listen for a command
        while True:
            command_voice_data = record_audio()

            # Check if a command was given
            if command_voice_data:
                respond(command_voice_data)
            
            # If the user says "stop listening" or similar, exit command mode
            if 'stop listening' in command_voice_data or 'goodbye' in command_voice_data:
                siri_speak("Okay, going back to standby mode.")
                break
    else:
        print("Wake word not detected")
