#H       H         A          L
#H       H       A  A        L
#HHHHH     A      A      L
#H       H  AAAAAAA    L
#H       H  A           A    LLLL
import settings
import init
import sys
import action

class main():
        def __init__(self):
                inf = init.files()
                self.inf = inf

        def retinf(self):
                return self.inf

if __name__ == '__main__':
        main = main()
        settings.sl = main.retinf()

        at = str(input("Напишите 'y' если вы согласны что не нанесёте никому вред, из-за долго спама телефон может сломаться , 'n' если отказываетесь, приложение выключится => "))
        if(at == "n" or at == "N"):
                print("Досвидание")
                sys.exit("Отказ от отвественности")

        elif(at == "y" or at == "Y"):  
                pn = str(input("Укажите номер телефона жертвы (пример 79226111046) => "))
                settings.pn = pn
                loopc = int(input("Укажите количество повторов (в цифрах) => "))
                settings.loopc = loopc
                action.activate(settings.loopc,settings.sl,settings.pn)

        else:
                print("Досвидание")
                sys.exit("Не дал ответа")
        
        
        
        

