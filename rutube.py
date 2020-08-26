def method():
        method = "post"
        return method

def json():
        json = True
        return json

def name():
        name = "rutube"
        return name

def url(pn):
        url = "https://pass.rutube.ru/api/accounts/phone/send-password/"
        return url

def data(phone):
        data = {"phone": "+"+phone}
        return data

def error():
        error = '{"success":false,"message":"Уважаемый пользователь, вы израсходовали лимит на повторную отправку смс в сутки. Пожалуйста, воспользуйтесь паролем, который мы отправляли вам ранее, или повторите попытку завтра."}'
        return error
