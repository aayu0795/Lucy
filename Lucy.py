import winsound
from Assistance import Assistance

obj = Assistance()

while True:

    command = obj.command()
    print(command.upper())

    if command in ['lucy', 'uc', 'loc', 'blue sea', 'loc']:

        winsound.PlaySound('Sounds/init.wav', winsound.SND_ASYNC)

        command = obj.command()
        print(command.upper())

        if 'introduce' in command:
            obj.introduce()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'hello' in command or 'hey' in command:
            obj.hi()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif command in ['how are you', 'how', 'you']:
            obj.greetings()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'calculate' in command:
            obj.calculate()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'you' in command and 'name' in command:
            obj.name()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'made' in command or 'maker' in command:
            obj.maker()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'joke' in command:
            obj.joke()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'time' in command:
            obj.time()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'date' in command:
            obj.date()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'open website' in command:
            obj.open_website()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'open chrome' in command:
            obj.chrome()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'control panel' in command:
            obj.control_panel()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'cmd' in command or 'command prompt' in command:
            obj.command_prompt()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'open notepad' in command:
            obj.notepad()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'weather' in command:
            obj.weather()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'temperature' in command:
            obj.temperature()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'thank' in command:
            obj.thanks()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'play' in command:
            obj.play()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'slow' in command:
            obj.slow()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif command in ['bye', 'bhai', 'exit', 'terminate', 'shutdown', 'sleep']:
            obj.bye()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            break

        elif 'girlfriend' in command:
            obj.cant_answer()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'want to know' in command:
            obj.wikipedia()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        elif 'pic' in command or 'pho' in command:
            obj.capture()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue

        else:
            obj.sorry()
            winsound.PlaySound('Sounds/stop.wav', winsound.SND_ASYNC)
            continue
