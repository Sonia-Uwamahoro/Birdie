


# Simple Sample Automatic Speech Recognition(Birdie)


import speech_recognition as birdie
import datetime
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

listener = birdie.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with birdie.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'birdie' in command:
                command = command.replace('birdie', '')
                print(command)

    except:
        pass
    return command


def run_birdie():
    command = take_command()
    print(command)
    if 'play the song' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('It is ' + time)

    elif 'tell me' in command:
        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Hey, can you repeat that again')


while True:
    run_birdie()


run_birdie()
