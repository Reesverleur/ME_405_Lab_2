{\rtf1\ansi\ansicpg1252\cocoartf2707
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red25\green28\blue31;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c12941\c14510\c16078;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww15640\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs28 \cf0 # ME 405 Lab 2\
## Created by Rees Verleur, Tristan de Lemos, and Trenten Spicer\
\
\
Our closed loop controller takes in a set point, a point at which to stop the motor, and a gain, a value to which how fast the motor should get to this position. If the gain is 1 or greater, the motor will become unstable and oscillate over the set point and gradually grow larger. \
\
We have made a separate class file, pro_control.py, that defines all of the functions we need for our closed loop controller. When initialized, the gain is set to 1 and the set point is 0, so the motor will not move.\
Our three test cases show under damped, over damped, and just right.\cf2 \cb3 \expnd0\expndtw0\kerning0
\
\
motor_controller.py is considered our main python file, using all of the classes together to perform the lab. motor_reader.py is the program we used on the terminal to set the set point and gain, and also obtain plots of our motor performance.\
\
\cf0 \cb1 \kerning1\expnd0\expndtw0 \
!\cf2 \cb3 \expnd0\expndtw0\kerning0
[Under damped Case](ExcessiveOscillation.png)\
\
![Over damped\cf0 \cb1 \kerning1\expnd0\expndtw0  Case\cf2 \cb3 \expnd0\expndtw0\kerning0
](Overdamped.png)\cf0 \cb1 \kerning1\expnd0\expndtw0 \
\cf2 \cb3 \expnd0\expndtw0\kerning0
\
![Perfect Case](GoodPerformance.png)}