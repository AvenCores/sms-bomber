#H       H         A          L
#H       H       A  A        L
#HHHHH     A      A      L
#H       H  AAAAAAA    L
#H       H  A           A    LLLL
from glob import glob

def files():
        sc = 0
        sl = []
        for file in glob('*.py'):
                if(file != "action.py" and file != "settings.py" and file != "main.py" and file != "init.py"):
                        sc += 1
                        sl.append(file)

        print("Сервисов загружено: "+str(sc))
        return sl

