# Mecanum-Wheel-Car

This is an omnidirectional electric car with mecanum wheels and it is controlled with a ps4 controller. For the car itself, Jetson nano or a Raspberry Pi can be used in order to control the dual H-Bridge motor controllers and a battery to power them up. If you are not using a jetson nano, you might have to change the GPIO setmode that is in the code. In this code example, Jetson nano was used, so the GPIO is different since the pins on Jetson nano are slightly different than the pins on Raspberry Pi. This code was also tested on a Raspberry Pi, and it will soon be available here.

<table>
  <tr>
    <td> <img height="246" width="400" src="https://user-images.githubusercontent.com/111835151/186298406-e8ddf1d1-b236-41f0-bd1e-2b4a5d7ea72b.gif"></td>
    <td> <img height="246" width="500" src="https://user-images.githubusercontent.com/111835151/186312911-40ec8e2b-0487-4fad-b969-f473dbea69d2.jpg"></td>
  </tr>
</table>

Four motors are used and one H-Bridge motor driver controls two motors. They can also control more than two motors, but in this case since the mecanum wheels are used, we need to control each of the wheels seperatly. There are only two PWM pins on Jetson Nano, so the EN pins on the motor drivers were not used in this example. As can be seen in the picture below, there are multiple PWM pins on Raspberry Pi which allows us to use the EN pins and control the speed of the car. Two GND pins on the board are connected to the motor drivers in order to communicate with them. Raspberry Pi is not powering the motor controllers, so a seperate power supply is used to power up the drivers.

NOTE: YOU SHOULD USE A DIFFERENT POWER SUPPLY FOR MOTOR DRIVERS AND ONLY CONNECT THE GNDs OF RASPBERRY PI OR (JETSON) TO THE MOTOR DRIVERS FOR THEM TO COMMUNICATE TO EACH OTHER SINCE YOUR BOARD MIGHT GET DEMAGED!! 

