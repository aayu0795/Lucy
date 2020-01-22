import os
import time
import parser
import pyttsx3
import requests
import winsound
import webbrowser
from datetime import datetime
import speech_recognition as sr
from wikipedia import wikipedia


class Assistance:
    lucy = pyttsx3.init()
    lucy.setProperty('rate', 140)

    def am_pm(self):
        hour = int(time.strftime('%H'))
        if int(hour) < 12:
            return 'AM'
        else:
            return "PM"

    def hi(self):
        hour = int(time.strftime('%H'))
        if hour < 12:
            self.lucy.say('Hi User, Good morning')
            self.lucy.runAndWait()

        elif hour < 18:
            self.lucy.say('Hi User, Good afternoon')
            self.lucy.runAndWait()

        else:
            self.lucy.say('Hi User, Good evening')
            self.lucy.runAndWait()

    def command(self):
        r = sr.Recognizer()
        with sr.Microphone() as user_command:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(user_command, duration=0.2)
            cmd_audio = r.listen(user_command, phrase_time_limit=5)
        try:
            cmd_text = r.recognize_google(cmd_audio, language='en-US')
            return cmd_text.lower()
        except sr.UnknownValueError:
            cmd_text = self.command()
        return cmd_text.lower()

    def bye(self):
        self.lucy.say('bye bye user, have a nice day')
        self.lucy.runAndWait()

    def introduce(self):
        self.lucy.say('Hi, i am Lucifer.')
        self.lucy.say('you can call me lucy')
        self.lucy.say('I am voice controlled virtual assistant')
        self.lucy.say('I was born on 01/01/2020')
        self.lucy.runAndWait()

    def calculate(self):
        self.lucy.say('what you want me to calculate')
        self.lucy.runAndWait()
        winsound.PlaySound('init.wav', winsound.SND_ASYNC)
        cmd_text = self.command()
        if cmd_text is not None:
            a = parser.expr(cmd_text).compile()
            result = eval(a)
            self.lucy.say('The answer is {}'.format(result))
            self.lucy.runAndWait()

    def greetings(self):
        self.lucy.say('I am good, what about you')
        self.lucy.runAndWait()

    def name(self):
        self.lucy.say('My name is Lucifer, you can call me lucy')

    def maker(self):
        self.lucy.say('I was created my Aayu')
        self.lucy.say('You might know him as, Aayush kumar')
        self.lucy.runAndWait()

    def cant_answer(self):
        self.lucy.say("I can't answer that")
        self.lucy.runAndWait()

    def open_website(self):
        self.lucy.say('Which website would you like to open')
        self.lucy.runAndWait()
        winsound.PlaySound('init.wav', winsound.SND_ASYNC)
        cmd_text = self.command()
        if cmd_text is not None:
            new_cmd = (str(cmd_text).replace('.com', '')).strip()
            self.lucy.say('Opening {}'.format(new_cmd))
            self.lucy.runAndWait()
            webbrowser.open('https://www.{}.com/'.format(new_cmd))

    def time(self):
        hour = int(time.strftime('%H'))
        if hour - 12 == 0 or hour - 12 == -12:
            self.lucy.say(('The time is, {}:{} {}'.format(12, time.strftime('%M'), self.am_pm())))
            self.lucy.runAndWait()
        elif hour > 12:
            self.lucy.say(('The time is, {}:{} {}'.format((hour - 12), time.strftime('%M'), self.am_pm())))
            self.lucy.runAndWait()
        else:
            self.lucy.say(('The time is, {}:{} {}'.format(hour, time.strftime('%M'), self.am_pm())))
            self.lucy.runAndWait()

    def date(self):
        now = datetime.now()
        self.lucy.say(('the date is, {}'.format(now.strftime("%A %d. %B %Y"))))
        self.lucy.runAndWait()

    def control_panel(self):
        self.lucy.say('Opening control panel')
        self.lucy.runAndWait()
        os.system('control.exe')

    def command_prompt(self):
        self.lucy.say('Opening command prompt')
        self.lucy.runAndWait()
        os.system('start cmd')

    def notepad(self):
        self.lucy.say('Opening notepad')
        self.lucy.runAndWait()
        os.system('notepad')

    def chrome(self):
        self.lucy.say('Opening chrome')
        self.lucy.runAndWait()
        os.system('start chrome')

    def joke(self):
        response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
        if response.status_code == requests.codes.ok:
            self.lucy.say(str(response.json()['joke']))
            self.lucy.runAndWait()
        else:
            self.lucy.say('oops!I ran out of jokes')
            self.lucy.runAndWait()

    def weather(self):
        response = requests.get(
            "https://openweathermap.org/data/2.5/weather?q=Indore,in&appid=b6907d289e10d714a6e88b30761fae22")
        data = response.json()
        desc = data['weather'][0]['description']
        city = data['name']
        temp = data['main']['temp']
        if response.status_code == requests.codes.ok:
            self.lucy.say("It's currently {} and {} degree in {} ".format(desc, temp, city))
            self.lucy.runAndWait()

    def temperature(self):
        response = requests.get(
            "https://openweathermap.org/data/2.5/weather?q=Indore,in&appid=b6907d289e10d714a6e88b30761fae22")
        data = response.json()
        temp = data['main']['temp']
        if response.status_code == requests.codes.ok:
            self.lucy.say("It's {} degree outside ".format(temp))
            self.lucy.runAndWait()

    def slow(self):
        self.lucy.say('I am trying my best, sorry for the delay')
        self.lucy.runAndWait()

    def thanks(self):
        self.lucy.say('My pleasure')
        self.lucy.runAndWait()

    def play(self):
        self.lucy.say('Which song would you like to play')
        self.lucy.runAndWait()
        winsound.PlaySound('init.wav', winsound.SND_ASYNC)
        cmd_text = self.command()
        if cmd_text is not None:
            url = "https://www.youtube.com/results?search_query=" + cmd_text.replace(' ', '+')
            webbrowser.open(url)

    def sorry(self):
        self.lucy.say("Sorry, I didn't get you.")
        self.lucy.runAndWait()

    def wikipedia(self):
        self.lucy.say('What you want to know')
        self.lucy.runAndWait()
        winsound.PlaySound('init.wav', winsound.SND_ASYNC)
        cmd_text = self.command()
        self.lucy.say('Let me see, what i can find')
        self.lucy.runAndWait()
        wiki_data = wikipedia.summary(cmd_text).split('.')
        self.lucy.say('.'.join(wiki_data[:3]))
        self.lucy.runAndWait()
        self.lucy.say('Do you want me to read more')
        self.lucy.runAndWait()
        winsound.PlaySound('init.wav', winsound.SND_ASYNC)
        cmd_text = self.command()
        winsound.PlaySound('init.wav', winsound.SND_ASYNC)
        if 'yes' in cmd_text and cmd_text is not None:
            self.lucy.say('.'.join(wiki_data[3:]))
            self.lucy.runAndWait()
        else:
            self.lucy.say('Okay')
            self.lucy.runAndWait()
