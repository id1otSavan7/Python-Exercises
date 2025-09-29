import RPi.GPIO as GPIO
import time
import threading
from gpiozero import Servo

# Define GPIO pins for input buttons
buttonMainFrame = 2  # Button for Main Frame
buttonNonBioContainer = 3  # Button for Non-Biodegradable Container
buttonRecyclableContainer = 4  # Button for Recyclable Container
buttonBioComposter = 5  # Button for Bio Composter

# Define GPIO pins for controlling container lids
inMainFrame = 6  # Output signal for Main Frame
inNonBioContainer = 7  # Output signal for Non-Biodegradable Container
inRecyclableContainer = 8  # Output signal for Recyclable Container
inBioComposter = 9  # Output signal for Bio Composter

recieveSignal = 13  # Input signal to check compost state

# Define GPIO pins for servo control buttons
buttonServo1 = 10  # Servo Control Button 1
buttonServo2 = 11  # Servo Control Button 2
buttonServo3 = 12  # Servo Control Button 3

# Define GPIO pins for servo motors
servoPin1 = 14  # Servo Motor 1
servoPin2 = 15  # Servo Motor 2
servoPin3 = 16  # Servo Motor 3

# Debounce and timing settings
debounceDelay = 0.3  # Debounce delay to prevent false triggering
mf_TimeOutStart = 0
nb_TimeOutStart = 0
bd_TimeOutStart = 0
rc_TimeOutStart = 0
lastDebounceTime = 0

# Servo auto-close timing
servoTimeout = 15
servoState = {"servo1": False, "servo2": False, "servo3": False}

# State variables for lid control
mf_state = False
nb_state = False
rc_state = False
bd_state = False

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(recieveSignal, GPIO.IN)
GPIO.setup(buttonMainFrame, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonNonBioContainer, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonRecyclableContainer, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonBioComposter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonServo1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonServo2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonServo3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(inMainFrame, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(inNonBioContainer, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(inRecyclableContainer, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(inBioComposter, GPIO.OUT, initial=GPIO.HIGH)

# Initialize Servo Motors
servo1 = Servo(servoPin1)
servo2 = Servo(servoPin2)
servo3 = Servo(servoPin3)

# Function to read button states
def initialize_button_reading():
    global bmfState, bnbcState, brcState, bbcState, servo1State, servo2State, servo3State
    bmfState = GPIO.input(buttonMainFrame)
    bnbcState = GPIO.input(buttonNonBioContainer)
    brcState = GPIO.input(buttonRecyclableContainer)
    bbcState = GPIO.input(buttonBioComposter)
    servo1State = GPIO.input(buttonServo1)
    servo2State = GPIO.input(buttonServo2)
    servo3State = GPIO.input(buttonServo3)

# Function to check if composting is active
def check_compost_state():
    return GPIO.input(recieveSignal) == GPIO.HIGH

# Function to control servo movement
def control_servo(servo, servoName):
    servo.max()  # Open servo
    servoState[servoName] = True
    time.sleep(servoTimeout)
    if servoState[servoName]:  # Auto-close if still open
        servo.min()
        servoState[servoName] = False

# Main function loop
def main():
    global mf_state, nb_state, rc_state, bd_state, mf_TimeOutStart, nb_TimeOutStart, rc_TimeOutStart, bd_TimeOutStart, lastDebounceTime
    
    print("Setup Complete. Monitoring...")
    try:
        while True:
            initialize_button_reading()
            currentTime = time.time()
            
            # Check if any button is pressed and toggle the respective lid
            if not check_compost_state() and bmfState and currentTime - lastDebounceTime > debounceDelay:
                mf_state = not mf_state
                GPIO.output(inMainFrame, GPIO.HIGH if mf_state else GPIO.LOW)
                mf_TimeOutStart = currentTime
                lastDebounceTime = currentTime
            elif not check_compost_state() and bnbcState and currentTime - lastDebounceTime > debounceDelay:
                nb_state = not nb_state
                GPIO.output(inNonBioContainer, GPIO.HIGH if nb_state else GPIO.LOW)
                nb_TimeOutStart = currentTime
                lastDebounceTime = currentTime
            elif not check_compost_state() and brcState and currentTime - lastDebounceTime > debounceDelay:
                rc_state = not rc_state
                GPIO.output(inRecyclableContainer, GPIO.HIGH if rc_state else GPIO.LOW)
                rc_TimeOutStart = currentTime
                lastDebounceTime = currentTime
            elif not check_compost_state() and bbcState and currentTime - lastDebounceTime > debounceDelay:
                bd_state = not bd_state
                GPIO.output(inBioComposter, GPIO.HIGH if bd_state else GPIO.LOW)
                bd_TimeOutStart = currentTime
                lastDebounceTime = currentTime
            
            # Auto-close lids after 5 seconds
            for state, timeout, pin in [(mf_state, mf_TimeOutStart, inMainFrame),
                                        (nb_state, nb_TimeOutStart, inNonBioContainer),
                                        (rc_state, rc_TimeOutStart, inRecyclableContainer),
                                        (bd_state, bd_TimeOutStart, inBioComposter)]:
                if state and currentTime - timeout > 5:
                    state = False
                    GPIO.output(pin, GPIO.LOW)
            
            # Servo button press handling
            if servo1State and not servoState["servo1"]:
                threading.Thread(target=control_servo, args=(servo1, "servo1")).start()
            if servo2State and not servoState["servo2"]:
                threading.Thread(target=control_servo, args=(servo2, "servo2")).start()
            if servo3State and not servoState["servo3"]:
                threading.Thread(target=control_servo, args=(servo3, "servo3")).start()
            
            time.sleep(0.1)  # Small delay to prevent excessive CPU usage
    
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program terminated. GPIO cleaned up.")

if __name__ == "__main__":
    main()
