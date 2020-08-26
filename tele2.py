def method():
        method = "post"
        return method

def json():
        json = True
        return json

def name():
        name = "tele2"
        return name

def url(pn):
        url = "https://msk.tele2.ru/api/validation/number/"+pn
        return url

def data(phone):
        data = {"sender": "Tele2"}
        return data

def error():
        error = '{"name":"TOO_MANY_REQUESTS","detail":"To many requests"}'
        return error
