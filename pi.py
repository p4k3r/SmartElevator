import RPi.GPIO as GPIO

import time

from time import sleep

import face_recognition

from os import system

import database



lift1=[3,5,7,11]

lift2=[13,15,19,21]



cur_floor_lift1=1

cur_floor_lift2=1



def on(pin):

    GPIO.output(pin,GPIO.HIGH)



def off(pin):

    GPIO.output(pin,GPIO.LOW)



def close_all():

    off(lift1[0])

    off(lift2[0])

    off(lift1[1])

    off(lift2[1])

    off(lift1[2])

    off(lift2[2])

    off(lift1[3])

    off(lift2[3])



def initialise():

    on(lift1[0])

    on(lift2[0])





def move_lift1(cur_floor_lift1,target_floor):

    if cur_floor_lift1==target_floor:

        return

    if cur_floor_lift1<target_floor:

        dir=1

    else:

        dir=-1

    for i in range(cur_floor_lift1,target_floor,dir):

        off(lift1[i-1])

       # sleep(2)

        print "Lift 1 :" +str(i+dir)

        on(lift1[i+dir-1])

        cur_floor_lift1=i+dir

        sleep(3)

    return cur_floor_lift1



def move_lift2(cur_floor_lift2,target_floor):

    if cur_floor_lift2 == target_floor:

        return

    if cur_floor_lift2 < target_floor:

        dir = 1

    else:

        dir = -1

    for i in range(cur_floor_lift2, target_floor, dir):

        off(lift2[i - 1])

        print "Lift 2 :" + str(i + dir)

        on(lift2[i + dir - 1])

        cur_floor_lift2=i+dir

        sleep(3)

    return cur_floor_lift2

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# stop warnings

GPIO.setwarnings(False)



# set up GPIO output channel

GPIO.setup(3, GPIO.OUT)

GPIO.setup(5, GPIO.OUT)

GPIO.setup(7, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)

GPIO.setup(15, GPIO.OUT)

GPIO.setup(19, GPIO.OUT)

GPIO.setup(21, GPIO.OUT)



close_all()

initialise()


while(1):

    system("raspistill -o Img.png")

    user=face_recognition.recognize("Img.png")
    if user==-2:
        print "LIFT is Idle No face Detected"
	continue
    entry=int(raw_input("Enter Current Floor No :"))
    
    if user==-1:
#	print "AAya"
        exit=int(raw_input("Enter Destination :"))
	user=int(time.time())
        database.insert(user,entry,exit)

        if abs(entry-cur_floor_lift1)<abs(entry-cur_floor_lift2):
	    cur_floor_lift1= move_lift1(cur_floor_lift1,entry)
            cur_floor_lift1= move_lift1(entry,exit)
	    

        else:
	    cur_floor_lift2= move_lift2(cur_floor_lift2,entry)
            cur_floor_lift2= move_lift2(entry,exit)

	face_recognition.post("Img.png",user)

    elif database.find(user,entry)==-1:
#	print "Pss"
        exit = int(raw_input("Enter Destination :"))

        database.insert(user, entry, exit)

        if abs(entry - cur_floor_lift1) < abs(entry - cur_floor_lift2):
	    cur_floor_lift1= move_lift1(cur_floor_lift1,entry)
            cur_floor_lift1= move_lift1(entry,exit)

        else:
	    cur_floor_lift2= move_lift2(cur_floor_lift2,entry)
            cur_floor_lift2= move_lift2(entry,exit)
    else:

        exit=database.find(user,entry)

        if abs(entry - cur_floor_lift1) < abs(entry - cur_floor_lift2):
	    cur_floor_lift1= move_lift1(cur_floor_lift1,entry)
            cur_floor_lift1= move_lift1(entry,exit)
        else:
	    cur_floor_lift2= move_lift2(cur_floor_lift2,entry)
            cur_floor_lift2= move_lift2(entry,exit)
