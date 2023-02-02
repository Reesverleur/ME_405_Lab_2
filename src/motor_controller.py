from motor_driver import MotorDriver
from encoder_driver import EncoderDriver
from pro_control import ProControl
import utime

def main():
    """!@brief	The main motor control function
    @details	This function uses the pro_control class
                to control the motor
    """
    u2 = pyb.UART(2, baudrate=115200)
    enc = EncoderDriver(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    motor = MotorDriver (pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
    con = ProControl()
    read = enc.read()
    pos = 0
    
    con.set_setpoint(int(input("Enter Setpoint")))
    while True:
        con.set_Kp(float(input("Enter Gain")))
        pos = 0
        utime.
        time = []
        position = []
        for y in range(128):
            read,pos = enc.update(read,pos)
            position.append(pos)
            time.append(utime.ticks_ms())
            effort = con.run(pos)
            #print("Effort = ",effort)
            if effort<-100:
                effort = -100
            elif effort>100:
                effort = 100
                
            motor.set_duty_cycle(effort)
            utime.sleep_ms(10)
            
        for x in range(len(time)):
            u2.write(time[x],',',position[x])
        
if __name__=='__main__':
    main()
        