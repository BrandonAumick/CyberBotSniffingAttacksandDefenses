from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)

while True:
    
    packet = radio.receive()

    if packet:
        print("Receive:", packet)
        display.show(getattr(Image, packet))
    except AttributeError:
        print("Receive:", packet)
        print("packet not image string")
