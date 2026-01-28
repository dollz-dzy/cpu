# psu.py

# impotam firele 

from clock import CLOCK_comp
from cpu import CU_comp

# =================================================================================================
# PSU

# dam drumu la clock

CLOCK_comp()

# dam drumu la CU_comp din cpu , sai zicem sa se trezeasca 
# si sa astepte semnal de la CLOCK_comp

CU_comp()

