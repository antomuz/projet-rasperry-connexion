# custom_image.py - show how to define and use a custom image

import microbit
import time

# BANANA = microbit.Image("00090:00090:00990:09900:99000")
def show_wrong():
    wrong = microbit.Image("90009:09090:00900:09090:90009")
    microbit.display.show(wrong)
    time.sleep(4)

def show_right():
    right = microbit.Image("09990:90009:90009:90009:09990")
    microbit.display.show(right)

def show_happy():
    happy = microbit.Image("09090:09090:09090:90009:09990")
    microbit.display.show(happy)

def show_access_granted(rep=1):
    for i in range(0,rep):
        microbit.display.scroll("ACCESS GRANTED")
        show_right()

def show_access_denied(rep=1):
    for i in range(0,rep):
        microbit.display.scroll("ACCESS DENIED")
        show_wrong()
        
def clear():
    clear = microbit.Image("0000:00000:00000:00000:00000")
    microbit.display.show(clear)

def loading():
    frame1 = microbit.Image("67890:50000:40900:30000:21000")
    frame2 = microbit.Image("54789:40000:30900:20000:10000")
    frame3 = microbit.Image("45678:30009:20900:10000:00000")
    frame4 = microbit.Image("34567:20008:10909:00000:00000")
    frame5 = microbit.Image("23456:10007:00908:00009:00000")
    frame6 = microbit.Image("12345:00006:00907:00008:00009")
    frame7 = microbit.Image("01234:00005:00906:00007:00098")
    frame8 = microbit.Image("00123:00004:00905:00006:00987")
    frame9 = microbit.Image("00012:00003:00904:00005:09876")
    frame10 = microbit.Image("00001:00002:00903:00004:98765")
    frame11 = microbit.Image("00000:00001:00902:90003:87654")
    frame12 = microbit.Image("00000:00000:90901:80002:76543")
    frame13 = microbit.Image("00000:90000:80900:70001:65432")
    frame14 = microbit.Image("90000:80000:70900:60000:54321")
    frame15 = microbit.Image("89000:70000:60900:50000:43210")
    frame16 = microbit.Image("78900:60000:50900:40000:32100")
    
    while True:
        microbit.display.show(frame1)
        time.sleep(0.125)
        microbit.display.show(frame2)
        time.sleep(0.125)
        microbit.display.show(frame3)
        time.sleep(0.125)
        microbit.display.show(frame4)
        time.sleep(0.125)
        microbit.display.show(frame5)
        time.sleep(0.125)
        microbit.display.show(frame6)
        time.sleep(0.125)
        microbit.display.show(frame7)
        time.sleep(0.125)
        microbit.display.show(frame8)
        time.sleep(0.125)
        microbit.display.show(frame9)
        time.sleep(0.125)
        microbit.display.show(frame10)
        time.sleep(0.125)
        microbit.display.show(frame11)
        time.sleep(0.125)
        microbit.display.show(frame12)
        time.sleep(0.125)
        microbit.display.show(frame13)
        time.sleep(0.125)
        microbit.display.show(frame14)
        time.sleep(0.125)
        microbit.display.show(frame15)
        time.sleep(0.125)
        microbit.display.show(frame16)
        time.sleep(0.125)

#show_access_granted(5)
#for i in range(0,100):
#   pass
#    show_right()
#    show_wrong()
#    show_happy()
#    loading()
# END

