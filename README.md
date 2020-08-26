# sms-hal-bomber
SMS-BOMBER (Russian)

INSTRUCTION

# 1 - download
git clone https://github.com/halwarsing/sms-hal-bomber

# 2 - run python script main.py
python3 main.py

# 3 - agree licence
y - yes;
n - no;

# 4 - number phone
example - 79226111046 - it's not my phone number

# 5 - number of repetitions
0 - infinite

# 7 add your own services
If you know the services better, you can add your own, here's an example.

def method(): # method post or get
        method = "post"
        return method

def json(): # method json - false or true
        json = False
        return json

def name(): # name service
        name = "worki"
        return name

def url(pn): # url service
        url = "https://shop.vsk.ru/ajax/auth/postSms/"
        return url

def data(phone): # data or json
        data = {"phone": phone}
        return data

def error(): # error msg when an error occurs in the service
        error = '{"message":"Превышено количество попыток отправки кода. Попробуйте позже или обратитесь в службу поддержки.","errors":[{"message":"Превышено количество попыток отправки кода. Попробуйте позже или обратитесь в службу поддержки.","key":null,"code":null}]}'
        return error

Thanks for watching!
