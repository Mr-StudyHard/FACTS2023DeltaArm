#imports
import RPi.GPIO as GPIO
import threading

#Class and Objects
from time import sleep
from Motor import Motor



class Multiplemotors:
            

        def RunBothMotors(self,MotorA,MotorB,MotorC,Different_Case):
            
            if(Different_Case == 1):
                  print("Runing AlL Motors Individually")
                  t1 = threading.Thread(target=MotorA.RunMotorIndividually)
                  t2 = threading.Thread(target=MotorB.RunMotorIndividually)
                  t3 = threading.Thread(target=MotorC.RunMotorIndividually)

                  t1.start()
                  t2.start()
                  t3.start()

                  t1.join()
                  t2.join()
                  t3.join()
            
            elif(Different_Case == 2):
                  print("Runing All Motors")
                  t1 = threading.Thread(target=MotorA.RunALLMotor)
                  t2 = threading.Thread(target=MotorB.RunALLMotor)
                  t3 = threading.Thread(target=MotorC.RunALLMotor)

                  t1.start()
                  t2.start()
                  t3.start()

                  t1.join()
                  t2.join()
                  t3.join()
            
                

    

