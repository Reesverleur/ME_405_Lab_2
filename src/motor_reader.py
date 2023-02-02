# PC Python file for lab 2

import serial
from matplotlib import pyplot
import time


def main():
    
    x_list = []
    y_list = []
    
    with serial.Serial('COMx', 115200) as s_port:
        #
        # send kp value
        s_port.write(b'0.2')
        
        
        sline = s_port.readline()
        while(sline != ""):
        
            try:
                data1, data2 = s_port.readline().split(b',')
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
                
            sline = s_port.readline()
            
            
        pyplot.plot(x_list, y_list, 'go-')
        pyplot.xlabel("x")
        pyplot.ylabel("y")
        pyplot.show()
            
        #for i in range(len(x_list)):
        #    print(x_list[i], ",", y_list[i])




if __name__ == "__main__":
    main()