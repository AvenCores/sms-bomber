def method():
        method = "post"
        return method

def json():
        json = False
        return json

def name():
        name = "worki"
        return name

def url(pn):
        url = "https://shop.vsk.ru/ajax/auth/postSms/"
        return url

def data(phone):
        data = {"phone": phone}
        return data

def error():
        error = '{"message":"Превышено количество попыток отправки кода. Попробуйте позже или обратитесь в службу поддержки.","errors":[{"message":"Превышено количество попыток отправки кода. Попробуйте позже или обратитесь в службу поддержки.","key":null,"code":null}]}'
        return error
