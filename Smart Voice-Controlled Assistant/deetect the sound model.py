import speech_recognition as sr
import serial
import pyttsx3
import datetime

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize the serial connection to Arduino
ser = serial.Serial('COM4', 9600)  # Change COM4 to your Arduino's port

def siri_speak(audio_string):
    # Use pyttsx3 to speak the text directly
    engine.say(audio_string)
    engine.runAndWait()
    print(audio_string)  # Print the spoken text

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        siri_speak("Good Morning Karim! How can I help you?")
    elif hour >= 12 and hour < 18:
        siri_speak("Good Afternoon Karim! How can I help you?")
    else:
        siri_speak("Good Evening Karim! How can I help you?")

greet_user()

# Function to send command to Arduino
def send_command(command):
    ser.write(command.encode())

# Continuously listen for voice commands
while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for background noise
        try:
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Increase timeout
            text = recognizer.recognize_google(audio_data)
            print("Recognized:", text)

            # Check for specific commands
            if "turn on TV" in text:
                send_command("1")
                siri_speak("The TV is turning on")
            elif "turn off TV" in text:
                send_command("2")
                siri_speak("The TV is turning off")
            elif "open the door" in text:
                send_command("3")
                siri_speak("The door is opening")
            elif "close the door" in text:
                send_command("4")
                siri_speak("The door is closing")
            elif "turn on light" in text:
                send_command("5")
                siri_speak("The light is turning on")
            elif "turn off light" in text:
                send_command("6")
                siri_speak("The light is turning off")
            elif "exit" in text:
                print("Exiting...")
                siri_speak("OK bye bye")
                break

        except sr.WaitTimeoutError:
            print("Listening timed out; please try again.")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the request: {e}")
