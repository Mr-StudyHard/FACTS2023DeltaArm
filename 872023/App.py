#imports
import RPi.GPIO as GPIO
import threading

#Classes and Objects
from time import sleep
from Motor import Motor
from MultiMotor import Multiplemotors

#Put in data for ClockWise and CounterClockWise, On or Off, Pulse Speed for each motor
#later will entered according to the robot needs

CW_Or_CCW = int(input("1 for Clockwise or 0 for CounterClockWise: "))
print("The value in the main function for CW_Or_CCW: " + str(CW_Or_CCW) +"\n")

On_Or_Off = int(input("1 for ON or 0 for OFF: "))
print("The value in the main function for On_Or_Off: " + str(On_Or_Off) +"\n")

Pulse_Speed = int(input("Enter Pulse Speed around 5000 - 8000: "))
print("The value in the main function for Pulse Speed: " + str(Pulse_Speed) +"\n")

Different_Case = int(input("Enter the case you want 1 - 3, 1 for individual, 2 for all \n"))
print("The Case that you entered was" + str(Different_Case) +"\n")


#Set Up pins for Motors
MotorA = Motor(11,7,13,36)
MotorB = Motor(29,15,31,38)
MotorC = Motor(35,33,37,40)

MotorA.LeftOrRight(CW_Or_CCW)
MotorB.LeftOrRight(CW_Or_CCW)
MotorC.LeftOrRight(CW_Or_CCW)

MotorA.OnorOff(On_Or_Off)
MotorB.OnorOff(On_Or_Off)
MotorC.OnorOff(On_Or_Off)

MotorA.SetPulseSpeed(Pulse_Speed) #Pulse_Speed
MotorB.SetPulseSpeed(Pulse_Speed) #Pulse_Speed1
MotorC.SetPulseSpeed(Pulse_Speed) #Pulse_Speed2

MotorA.SetAngle(SomeAngle)
MotorB.SetAngle(SomeAngle)
MotorC.SetAngle(SomeAngle)

#Run Motors
#MotorA.RunMotor()
#MotorB.RunMotor() 
#MotorC.RunMotor()

MultiMultor1 = Multiplemotors()
MultiMultor1.RunBothMotors(MotorA,MotorB,MotorC,Different_Case)


