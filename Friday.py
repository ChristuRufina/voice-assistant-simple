import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
import openai
openai.api_key = ''

# Function to convert text to speech
def SpeakText(command):
    # Initialize the recognizer
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to record speech input
def record_text():
    # Loop in case of error
    while True:
        try:
            # Use microphone as source for input
            with sr.Microphone() as source2:
                # Prepare the recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("I'm listening...")
                # Listens for the user's input
                audio2 = r.listen(source2)
                # Using Google to recognize audio
                MyText = r.recognize_google(audio2)
                return MyText

        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))
        except sr.UnknownValueError:
            print('Unknown error occurred')

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0]['message']['content']
    messages.append(response.choices[0]['message'])
    return message

messages = []
r = sr.Recognizer()

while True:
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)
    print("Jarvis:", response)
