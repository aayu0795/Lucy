import parser
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
import os
import random

t_list = ["You're welcome.", "No problem.", "No worries.", "Don't mention it.",
          "My pleasure.", "Anytime.", "It was the least I could do.", "Glad to help."]

thanks = ''
c_list = []

now = datetime.now()
lucy = pyttsx3.init()  # object creation
r = sr.Recognizer()
hour = int(now.strftime('%H'))


def am_pm():
    if int(hour) < 12:
        return 'AM'
    else:
        return "PM"


def lucy_config():
    lucy.setProperty('rate', 150)  # setting up new voice rate
    lucy.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    voices = lucy.getProperty('voices')  # getting details of current voice
    lucy.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male, 1 for female


def lucy_response(response):
    lucy.say(response)
    c_list.append(('(Lucy)  {}'.format(response.capitalize())))
    lucy.runAndWait()


def command():
    global thanks
    thanks = random.choice(t_list)
    try:
        with sr.Microphone() as user_command:
            print('Listening')
            cmd_audio = r.listen(user_command, phrase_time_limit=5)
            cmd_text = r.recognize_google(cmd_audio, language='en-US')
            return cmd_text.lower()

    except sr.RequestError as e:
        lucy_response("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        return None


def assistance():
    cmd_text = command()

    if cmd_text is not None:

        if cmd_text == 'hi lucy' or cmd_text == 'hi' or cmd_text == 'hey' or cmd_text == 'hello':

            if hour < 12:
                c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
                lucy_response('Hi User, Good morning')

            elif hour < 18:
                c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
                lucy_response('Hi User, Good afternoon')

            else:
                c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
                lucy_response('Hi User, Good evening')

        elif 'bye' in cmd_text or 'exit' in cmd_text or 'close' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('bye bye user, have a nice day')
            obj.destroy()

        elif 'introduce' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Hi, i am Lucifer.')
            lucy_response('you can call me lucy')
            lucy_response('I am voice controlled virtual assistant')
            lucy_response('I was born on 01/01/2020')

        elif ('calculate' in cmd_text) and ('can you' in cmd_text or 'for me' in cmd_text):
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('what you want me to calculate')
            cmd_text = command()
            if cmd_text is not None:
                c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
                a = parser.expr(cmd_text).compile()
                result = eval(a)
                lucy_response('The answer is {}'.format(result))

        elif 'how do you do' == cmd_text or "how's you" == cmd_text or cmd_text == 'how are you':
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('I am good, what about you')

        elif 'your name' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('my name is Lucifer, you can call me lucy')

        elif 'made you' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('I was created my Aayu')
            lucy_response('You might know him as, Aayush kumar')

        elif 'girlfriend' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response("That's something, personal. I can't answer that")

        elif 'website' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Which website would you like to open')
            cmd_text = command()
            new_cmd = (str(cmd_text).replace('open website', '')).strip()
            c_list.append(('(You)   {}'.format(new_cmd.capitalize())))
            lucy_response('opening {}'.format(new_cmd))
            webbrowser.open('https://www.{}.com/'.format(new_cmd))

        elif 'time' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            if hour - 12 != 0:
                lucy_response(('the time is, {}:{} {}'.format((hour - 12), now.strftime('%M'), am_pm())))
            else:
                lucy_response(('the time is, {}:{} {}'.format(12, now.strftime('%M'), am_pm())))

        elif 'date' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response(('the date is, {}'.format(now.strftime("%A %d. %B %Y"))))

        elif 'repeat' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            new_cmd = str(cmd_text).replace('repeat', '')
            lucy_response(new_cmd)

        elif 'control panel' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Opening control panel')
            os.system('control.exe')

        elif 'command prompt' in cmd_text or 'cmd' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Opening command prompt')
            os.system("start cmd")

        elif 'notepad' in cmd_text or 'note pad' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Opening Notepad')
            os.system("notepad")

        elif 'joke' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
            if response.status_code == requests.codes.ok:
                lucy_response(str(response.json()['joke']))

            else:
                lucy_response('oops!I ran out of jokes')

        elif 'weather' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            response = requests.get(
                "https://openweathermap.org/data/2.5/weather?q=Indore,in&appid=b6907d289e10d714a6e88b30761fae22")
            data = response.json()
            desc = data['weather'][0]['description']
            city = data['name']
            temp = data['main']['temp']
            if response.status_code == requests.codes.ok:
                lucy_response("It's currently {} and {} degree in {} ".format(desc, temp, city))

        elif 'temperature' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            response = requests.get(
                "https://openweathermap.org/data/2.5/weather?q=Indore,in&appid=b6907d289e10d714a6e88b30761fae22")
            data = response.json()
            temp = data['main']['temp']
            if response.status_code == requests.codes.ok:
                lucy_response("It's {} degree outside ".format(temp))

        elif 'slow' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('I am trying my best, sorry for the delay')

        elif 'thank' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response(thanks)

        elif 'play' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Which song would you like to play')
            cmd_text = command()

            if cmd_text is None:
                lucy_response('Which song would you like to play')
                cmd_text = command()
                if cmd_text is not None:
                    c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            elif cmd_text == 'nothing':
                c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
                lucy_response('Okay')

            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            url = "https://www.youtube.com/results?search_query=" + cmd_text.replace(' ', '+')
            webbrowser.open(url)

        elif 'help' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response('Read the user manual')
            os.startfile('help.txt'.format(os.getcwd()))

        elif 'open' in cmd_text and 'computer' in cmd_text:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            new_cmd = (str(cmd_text).replace('open', '')).strip()
            os.startfile('computer.lnk')
            lucy_response('Opening ' + new_cmd.capitalize())

        else:
            c_list.append(('(You)   {}'.format(cmd_text.capitalize())))
            lucy_response("Sorry. I didn't get you, please repeat")

    else:
        lucy_response('How can i help you')


lucy_config()
obj = Tk()
obj.iconbitmap(r'icon.ico')
obj.geometry('324x212')
obj.title('Lucy')
obj.resizable(0, 0)
image = ImageTk.PhotoImage(Image.open('Lucy.jpg'.format(os.getcwd())))
lab = Label(obj, image=image)
lab.grid()
button = Button(obj, text='Listen', command=lambda: assistance(), width=20)
button.grid(row=0, column=0, sticky='s', pady=5)
obj.mainloop()

with open('conversations', 'a') as wc:
    wc.write('\n\n')
    for line in c_list:
        wc.write('{}\n'.format(line))
