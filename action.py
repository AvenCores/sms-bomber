#H       H         A          L
#H       H       A  A        L
#HHHHH     A      A      L
#H       H  AAAAAAA    L
#H       H  A           A    LLLL
import requests
import time

def activate(loopc,sl,pn):        
        def act(loopc,sl,pn):
                
                for i in range(loopc):
                        for file in sl:
                                modname = file
                                mod = __import__(modname.replace('.py',''))
                                method = mod.method()
                                name = mod.name()
                                url = mod.url(pn)
                                data = mod.data(pn)
                                error = mod.error()
                                json = mod.json()

                                if(json == False):
                                        if method == 'post':
                                                r = requests.post(url,params=data)
                                                text = r.text

                                        if method == 'get':
                                                r = requests.get(url,params=data)
                                                text = r.text

                                else:
                                        if method == 'post':
                                                r = requests.post(url,json=data)
                                                text = r.text

                                        if method == 'get':
                                                r = requests.get(url,json=data)
                                                text = r.text
                                

                                if text == error:
                                        print(str(time.ctime())+" "+name+" - error")

                                else:
                                        print(str(time.ctime())+" " +name+" - send")

        act(loopc,sl,pn)
