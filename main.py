#FIXME recive x & y of joystick for control  
 
 
import rpiLeds

ledRow = rpiLeds.Leds()

#here put in condition for entablished connection
while(False):
    ledRow.blink()
    #TODO: make sure it repeats
#turns the leds on when connection established
ledRow.stayOn() 

 # drive = drive()
 # blah blah blah 