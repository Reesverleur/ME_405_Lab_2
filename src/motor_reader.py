# PC Python file for lab 2

import serial
from matplotlib import pyplot
import time


def main():
    
   x_list = []
   y_list = []

   with serial.Serial('COM4', 115200,timeout = 3) as s_port:
       #
       # send kp value
       time.sleep(1)
       s_port.write(b'16384\r\n')
       time.sleep(1)
       s_port.write(b'0.2\r\n')
       
       while True:
           sline = s_port.readline()
           print(sline)
           if sline==b'done\r\n':
               break
        
           try:
                data1, data2 = sline.split(b',')
                data2 = data2.split(b'\r')[0]
                d1stat, d2stat = True, True
                
                try:
                    data1 = float(data1)
                except (ValueError):
                    d1stat = False
                    print("gaboobley")
                
                try:
                    data2 = float(data2)
                except(ValueError):
                    d2stat = False
                    print("bondo")

                if (d1stat and d2stat):
                    x_list.append(data1)
                    y_list.append(data2)
           except:
                # line not formatted correctly
                print("whoops")
                
            
            
       pyplot.plot(x_list, y_list, 'go-')
       pyplot.xlabel("Time [ms]")
       pyplot.ylabel("Position [enc counts]")
       pyplot.show()
            
        #for i in range(len(x_list)):
        #    print(x_list[i], ",", y_list[i])




if __name__ == "__main__":
    main()