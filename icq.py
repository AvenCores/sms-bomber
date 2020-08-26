def method():
        method = "post"
        return method

def json():
        json = False
        return json

def name():
        name = "icq"
        return name

def url(pn):
        url = "https://www.icq.com/smsreg/requestPhoneValidation.php"
        return url

def data(phone):
        data = {
                "msisdn": phone,
                "locale": "en",
                "counryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763",
        }
        return data

def error():
        error = '{"authId":null,"input_uin":null,"uin":null,"response":{"statusCode":410,"statusText":"phones_error_ratelimit ","statusDetailCode":"smsapi\/verify limit","requestId":"46763"}}'
        return error

