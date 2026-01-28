# clock.py

import time

# =================================================================================================
# CLOCK

# HI - Hight - 1 
# LO - Low - 0

HI = 1
LO = 0
CLOCK_SIGNAL = 0
HZ = 1  # 1 instructiune pe secunda


"""
Dc HZ / 2? 

finca intro secunda executam 2 chesti .

0.5 s , HI     
0.5 s , LO  

1s = HI,LO

"""

def CLOCK_comp():
    global CLOCK_SIGNAL

    while True:

        CLOCK_SIGNAL = HI  # 1 
        print("HI")

        time.sleep(HZ / 2)

        CLOCK_SIGNAL = LO # 0 
        print("LO")

        time.sleep(HZ / 2)

