import pika
import sys
import time
import json
import requests
import random
import tomcatmanager as tm

url= 'http://localhost:8080/manager'
#user= 'ace'
#password='newenglandclamchowder'

tomcat=tm.TomcatManager()
try:
        r=tomcat.connect(url)
        if r.ok:
                print('connected')
        else:
                print('bezveze si')
except Exception as err:
        print('not connected')


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

def temperature():
	#osijek
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Osijek,hr&appid=ae026e5831d1cee14ffd9a8b02717a4f')
	json_object = r.json()
	temp_k = round(float(json_object['main']['temp'] - 273.15),2)
	return str(temp_k)
def localtime():
    localtime=time.asctime( time.localtime(time.time()) )
    return str(localtime)


while True:
    
    channel.exchange_declare(exchange='logs',
                             exchange_type='fanout')
    temp=temperature()
    message = str(temp)+ " \u00b0C"
    channel.basic_publish(exchange='logs',
                            routing_key='',
                            body=message)
    

    print(" [x] Sent %r" % message)
    time.sleep(5)
connection.close()
