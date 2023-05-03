## Nerdy Druid



#### Introduction

This project is my long term project. 

At this point, it's 8 years already and it finally got a readme :)

So what is nerdy druid's shenanigans?

Druid cares about nature, means plants,animals and environment.

And a nerdy druid cares them by using machine,

because programming is nerdy druid's magic.



With a glim smiling, "The life and the death matters", the droid said.



#### A simple solution for simple question.

Before we talk about dts, pinctrl, wifi, zigbee.. or other software/linux stuff.

Image we are on a spaceship and heading to the new Eden.

What a druid will do his work in the spaceship as a adventure team member?

Simple, he water the plants, talk with hamsters, and have a aquarium with platy fish.



Problem is: in the spaceship, there can be only one druid with his bio-lab.

The space in the spaceship is too exspensive, so the druid can't take care all his plants and animal friends.  Luckly, the druid knows SoC and have some IoT knowledges.



For Aquarium:

The druid have a simple plan to just use GPIO / Relay and crontab.

When the timing is right, the full specturm light is on.

Same goes air pimping and water filter.



The python that controls GPIO pin is like the following (or simpleGPIO.py)

```python
import RPi.GPIO as GPIO

GPIO setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)
```

Wire up PIN 7 and corrosponding RELAY, 

Now we can issue pi to make GPIO output 0(LOW) or 1(HIGH)

And The  RELAY will trigger real electric device like airpump on/off.



Combined with crontab like the following:

```bash
0 21 * * * /usr/bn/python /home/pi/Projects/fishtank/lightON.py
0 9 * * * /usr/bin/python /home/pi/Projects/fishtank/lightOFF.py
30 23 * * * /usr/bin/python /home/pi/Projects/fishtank/airPumpON.py
0 0 * * * /usr/bin/python /home/pi/Projects/fishtank/airPumpOFF.py
0 6 * * * /usr/bin/python /home/pi/Project/fishtank/feederON.py
1 6 * * * /usr/bin/python /home/pi/Project/fishtank/feederOFF.py
```

Simple explain for the above schedule:

0 21 * * * /usr/bn/python /home/pi/Projects/fishtank/lightON.py

light on at 9 P.M. every day.

0 9 * * * /usr/bin/python /home/pi/Projects/fishtank/lightOFF.py

light off at 9 A.M. every day.

30 23 * * * /usr/bin/python /home/pi/Projects/fishtank/airPumpON.py

pump air into the tank at 11:30 every day.

0 0 * * * /usr/bin/python /home/pi/Projects/fishtank/airPumpOFF.py

stop pumping air into the tank at 12:00 P.M.

0 6 * * * /usr/bin/python /home/pi/Project/fishtank/feederON.py

open the feeder's gate at 6:00 A.M. (defult drop fish food for 5 secs)

1 6 * * * /usr/bin/python /home/pi/Project/fishtank/feederOFF.py

force close the feeder's gate at 6:01 A.M. (this is a safe check)

#### The video of above implementation on real hardware





#### Level up the complexity

So, the above solition is a solid one which I experiene by very long time and it keeps stable until some fish escape the tank and the water splash to the power adapter...



But the system is still health and working, actually, the device in the video is exactly the same device I am using 8 years ago.



Back to the complexity things.

We can now add a new logical model for the solid simple solution.



Think: Instead of regularly doing something, how about we do somthing by reflcting some enviornement changing?

In short :

```bash
If A then B
```

Our nerdy druid programming language will become something like:



"If the the temperture read above 30, we change cool water or open the cooler for the tank"



or even fuzzier things like:

"If it is dark enough, then we switch the light on"



To be continue 


