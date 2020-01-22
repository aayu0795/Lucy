import os
import parser
import winsound
import pyttsx3
import webbrowser
import requests
from datetime import datetime
import speech_recognition as sr


class Assistance:
    now = datetime.now()
    lucy = pyttsx3.init()
    lucy.setProperty('rate', 140)
    hour = int(now.strftime('%H'))
    time = ''

    def am_pm(self):
        if int(self.hour) < 12:
            return 'AM'
        else:
            return "PM"

    def hi(self):
        if self.hour < 12:
            self.lucy.say('Hi User, Good morning')
            self.lucy.runAndWait()

        elif self.hour < 18:
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
        cmd_text = self.command()
        if cmd_text is not None:
            new_cmd = (str(cmd_text).replace('.com', '')).strip()
            self.lucy.say('Opening {}'.format(new_cmd))
            self.lucy.runAndWait()
            webbrowser.open('https://www.{}.com/'.format(new_cmd))

    def time(self):
        if self.hour - 12 == 0 or self.hour - 12 == -12:
            self.lucy.say(('The time is, {}:{} {}'.format(12, self.now.strftime('%M'), self.am_pm())))
            self.lucy.runAndWait()
        elif self.hour > 12:
            self.lucy.say(('The time is, {}:{} {}'.format((self.hour - 12), self.now.strftime('%M'), self.am_pm())))
            self.lucy.runAndWait()
        else:
            self.lucy.say(('The time is, {}:{} {}'.format(self.hour, self.now.strftime('%M'), self.am_pm())))
            self.lucy.runAndWait()

    def date(self):
        self.lucy.say(('the date is, {}'.format(self.now.strftime("%A %d. %B %Y"))))
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

    def temprature(self):
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
        cmd_text = self.command()
        if cmd_text is not None:
            url = "https://www.youtube.com/results?search_query=" + cmd_text.replace(' ', '+')
            print(url)
            webbrowser.open(url)

    def sorry(self):
        self.lucy.say("Sorry, I didn't get you.")
        self.lucy.runAndWait()


if __name__ == '__main__':

    obj = Assistance()
    now = datetime.now()

    while True:

        command = obj.command()
        print(command.upper())

        if 'lucy' in command:
            print("Lucy activated".upper())

            winsound.PlaySound('init.wav', winsound.SND_ASYNC)

            command = obj.command()
            print(command.upper())

            if 'introduce' in command:
                obj.introduce()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'how are you' in command or 'how' in command and 'you' in command:
                obj.greetings()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'calculate' in command:
                obj.calculate()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'you' in command and 'name' in command:
                obj.name()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'made' in command or 'maker' in command:
                obj.maker()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'joke' in command:
                obj.joke()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'time' in command:
                obj.time()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'date' in command:
                obj.date()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'open website' in command:
                obj.open_website()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'open chrome' in command:
                obj.chrome()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'control panel' in command:
                obj.control_panel()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'cmd' in command or 'command prompt' in command:
                obj.command_prompt()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'open notepad' in command:
                obj.notepad()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'weather' in command:
                obj.weather()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'temperature' in command:
                obj.temprature()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'thank' in command:
                obj.thanks()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'play' in command:
                obj.play()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'slow' in command:
                obj.slow()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            elif 'exit' in command or 'bye' in command or 'shutdown' in command:
                obj.bye()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                break

            elif 'girlfriend' in command:
                obj.cant_answer()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue

            else:
                obj.sorry()
                winsound.PlaySound('stop.wav', winsound.SND_ASYNC)
                continue
