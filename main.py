import json as js
import time
import os
from winotify import Notification, audio
from datetime import datetime

estudos = {
    "harmonia": 10,
    "ritmo": 10,
    "partitura": 10,
    "tecnica": 5,
    "repertorio": 25
}

user = os.getenv("USERNAME")

def load_json(path: str):
    if os.stat(path).st_size == 0:
        return []
    
    with open(path, "r") as file:
        try:
            return js.load(file)
        except (FileNotFoundError, js.JSONDecodeError):
            print("Erro !!!!")
            return []

 
def start() -> None:

    
    esc = input(f"qual você quer:\nharmonia,\nritmo,\npartitura,\ntecnica,\nrepertorio\n>")
    if esc in estudos:
        timer = estudos[esc] * 60
    else:
        esc = ""
        print("not in hash")
        input("aperte qualquer letra para retornar para o começo: ")
        main()
    notificacao = Notification(app_id="main.py", title=f"o tempo de {esc} passou", msg="vai pro proximo", icon=f"C://Users/{user}/Documents/programacao/python/proj/test.png")
    notificacao.set_audio(audio.LoopingAlarm4, loop=False)
    
    data_list = load_json("sample.json")
    # time.sleep(timer)
    notificacao.show()



    entendeu = input("conseguiu entender: ")



    dado = {
        "data:": datetime.now().strftime("%c"),
        "nome": esc,
        "tempo": estudos[esc],
        "entendeu": entendeu
    }

    data_list.append(dado)


    with open("sample.json", "w") as file:
        js.dump(data_list, file, indent=4)
    
    main()

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
                os.system("cls")
                break
            


if __name__=="__main__":
    main()