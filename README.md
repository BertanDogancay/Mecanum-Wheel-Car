# Mecanum-Wheel-Car

This is an omnidirectional electric car with mecanum wheels and it is controlled with a ps4 controller. For the car itself, Jetson nano or a Raspberry Pi can be used in order to control the dual H-Bridge motor controllers and a battery to power-up them. If you are not using a jetson nano, you might have to change the GPIO setmode that is in the code. In this code example, Jetson nano was used, so the GPIO is different since the pins on Jetson nano are slightly different than the pins on Raspberry Pi. This code was also tested on a Raspberry Pi, and it will soon be available here.

![demo_video](https://user-images.githubusercontent.com/111835151/186298406-e8ddf1d1-b236-41f0-bd1e-2b4a5d7ea72b.gif) ![IMG-19313](https://user-images.githubusercontent.com/111835151/186303367-60fcdc0e-f79b-420b-a187-e835dc04c255.jpg)

NOTE: YOU SHOULD USE A DIFFERENT POWER SUPPLY FOR MOTOR CONTROLLERS AND ONLY CONNECT THE GNDs OF RASPBERRY PI OR (JETSON) TO THE MOTOR CONTROLLERS FOR THEM TO COMMUNICATE TO EACH OTHER SINCE YOUR BOARD MIGHT GET DEMAGED!! 
