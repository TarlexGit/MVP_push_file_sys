import requests

def checking(token):
    r = requests.get('http://127.0.0.1:8000/api/clients/client/token',{'token': token})
    # print(r, r.status_code  )
    return r.status_code