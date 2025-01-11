import json as js
import time
import os
from winotify import Notification, audio

estudos = {
    "harmonia": 10,
    "ritmo": 10,
    "partitura": 10,
    "tecnica": 5,
    "repertorio": 25
}

user = os.getenv("USERNAME")
notificacao = Notification(app_id="main.py", title="passou o tempo", msg="acabou o tempo", icon=f"C://Users/{user}/Documents/programacao/python/proj/test.png")
notificacao.set_audio(audio.LoopingAlarm4, loop=False)

def start() -> None:

    time.sleep()
    notificacao.show()

def data()-> None:
    pass


def main() -> None:
    while True:        
        os.system("cls")
        seconds = time.ctime()
        print(seconds)
        print("menu:\n1-começar\n2-ver dados\n3-sair ")
        esc = int(input("> "))

        match(esc):
            case 1:
                os.system("cls")
                start()
                break
            case 2:
                os.system("cls")
                data()
                break
            case 3:
                break
            


if __name__=="__main__":
    main()