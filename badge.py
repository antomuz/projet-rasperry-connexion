#!/usr/bin/env python
#https://pimylifeup.com/raspberry-pi-rfid-rc522/
from os import access
import requests
import RPi.GPIO as GPIO
import json
from mfrc522 import SimpleMFRC522
import accessbdd
import time

def lecture_badge():
    #TODO AJOUTER UN TIMER DE 30 SEC POUR LECTURE.
    reader = SimpleMFRC522()
    try:
        id = reader.read()
    except:
        print('erreur')
    finally :
        GPIO.cleanup() 
    return id[0]

def check_badge_webservice(login):
    vretour = []
    vid = lecture_badge()
    if vid[0] != 0:
        url = requests.get('https://btssio-carcouet.fr/ppe4/public/badge/{0}/{1}'.format(str(login),str(vid)))
        text = url.text
        data = json.loads(text)
    
        if data.get('status')=='true':
            vretour.append(True)
            return vretour
        else:
            vretour.append(False)
            vretour.append("le badge présenté est invalide, code :" + str(vid))
            return vretour
        #return data  
