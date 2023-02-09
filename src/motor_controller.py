"""!@file motor_controller.py
        This file uses the proportional control scheme in
        pro_control.py and the motor and encoder drivers from
        lab 1 to control a motor.
        
        The file works with motor_reader.py which should be run
        on a PC. That file sends the required setpoint and gain
        and then reads the data from the response.
"""
from motor_driver import MotorDriver
from encoder_driver import EncoderDriver
from pro_control import ProControl
import utime

def main():
    """!@brief	The main motor control function
    @details	This function uses the pro_control class
                to control the motor
    """
    u2 = pyb.UART(2, baudrate=115200, timeout = 65383)
    enc = EncoderDriver(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    motor = MotorDriver (pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
    con = ProControl()
    read = enc.read()
    pos = 0
    
    
    #con.set_setpoint(int(input('Enter setpoint: ')))
    while True:
        con.set_setpoint(int(u2.readline()))
        con.set_Kp(float(u2.readline()))
        #con.set_Kp(float(input('Enter gain: ')))
        read = enc.read()
        pos = 0
        start = utime.ticks_ms()
        time = []
        position = []
        for y in range(1024):
            read,pos = enc.update(read,pos)
            position.append(pos)
            time.append(utime.ticks_diff(utime.ticks_ms(),start))
            effort = con.run(pos)
            #print("Effort = ",effort)
            if effort<-100:
                effort = -100
            elif effort>100:
                effort = 100
                
            motor.set_duty_cycle(effort)
            utime.sleep_ms(10)
        motor.set_duty_cycle(0) 
        for x,y in zip(time,position):
            u2.write(f"{x},{y}\r\n")
            
        u2.write(b'done\r\n')
            
        
if __name__=='__main__':
    main()
        