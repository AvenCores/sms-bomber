def method():
        method = "post"
        return method

def json():
        json = True
        return json

def name():
        name = "cian"
        return name

def url(pn):
        url = "https://api.cian.ru/sms/v1/send-validation-code/"
        return url

def data(phone):
        data = {"phone": "+"+phone,"type": "authenticateCode"}
        return data

def error():
        error = ""
        return error
