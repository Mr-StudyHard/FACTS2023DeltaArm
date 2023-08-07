import RPi.GPIO as GPIO
from time import sleep

class Motor:
    PulseSpeed = 1
    AngleToMove = 1
    
    #set pin numbering system
    GPIO.setmode(GPIO.BOARD)
    
    #to Disable warnings
    GPIO.setwarnings(False)
        
        
    def __init__(self,PulsePin,Direction,Enable,Limit_Switch):
        self.PulsePin = PulsePin
        self.Direction = Direction
        self.Enable = Enable
        self.Limit_Switch = Limit_Switch
        
        
         #setup pins for GPIO output for Pulse
        GPIO.setup(self.PulsePin,GPIO.OUT)
    
    #Clockwise or Counter Clock Wise
    def LeftOrRight(self,Value):
        
        GPIO.setup(self.Direction,GPIO.OUT)
       
        if (Value >= 0):
           
            GPIO.output(self.Direction,Value)
            
        elif (Value == 1):
            
            GPIO.output(self.Direction,Value)
            
       #turn on or off motor     
    def OnorOff(self,Value):
        
        #setup Enable pin for output
        GPIO.setup(self.Enable,GPIO.OUT)
        
        if (Value >= 0):
           
            GPIO.output(self.Enable,Value)
            
        elif (Value == 1):
            
            GPIO.output(self.Enable,Value)
        
        #set Speed of pulse
    def SetPulseSpeed(self,Value):
        global PulseSpeed
        PulseSpeed = Value
        
    def SetAngle(self,Value):
        global AngleToMove
        AngleToMove = Value
            
        
    def RunMotorIndividually(self):
        #setup pins for GPIO output for Pulse
        GPIO.setup(self.PulsePin,GPIO.OUT)
        
        #create PWM instance with frequency
        pi_pwm = GPIO.PWM(self.PulsePin,PulseSpeed)
    
        #start PWM of required Duty Cycle
        pi_pwm.start(0)
        
        GPIO.setup(self.Limit_Switch,GPIO.IN, pull_up_down=GPIO.PUD_UP)
       
        while True:
            for duty in range(0,101,1):
                
                GPIO.output(self.Enable,GPIO.LOW)
                pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100 
                sleep(0.01)
                
                input_state = GPIO.input(self.Limit_Switch)
                
                #should be the angle that mainly stop it
                if (input_state == True):
                    print("Limit Switch Triggered")
                    GPIO.output(self.Enable,0)
                    return
                
                #PUT A CASE where if it hit a certain angle it stops moving
                #varable for angle "AngleToMove"
        
        
        #run Motor
    def RunALLMotor(self):
    
        #setup pins for GPIO output for Pulse
        GPIO.setup(self.PulsePin,GPIO.OUT)
        
        #create PWM instance with frequency
        pi_pwm = GPIO.PWM(self.PulsePin,PulseSpeed)
    
        #start PWM of required Duty Cycle
        pi_pwm.start(0)
        
        GPIO.setup(36,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(38,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            for duty in range(0,101,1):
                
                GPIO.output(self.Enable,GPIO.LOW)
                pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100 
                sleep(0.01)
                
                input_state = GPIO.input(36)
                input_state1 = GPIO.input(38)
                input_state2 = GPIO.input(40)
                
                if (input_state == True):
                    print("Limit Switch A Triggered")
                    GPIO.output(self.Enable,0)
                    return
                    
                elif (input_state1 == True):
                    print("Limit Switch B Triggered")
                    GPIO.output(self.Enable,0)
                    return
                    
                elif (input_state2 == True):
                    print("Limit Switch C Triggered")
                    GPIO.output(self.Enable,0)
                    return
