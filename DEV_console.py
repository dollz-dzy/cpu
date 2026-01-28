# DEV_console.py

# 
# DEV_ , e doar pentru dev sau user sa vada info , stergerea sa , 
# nu afecteaza cu nimic performanta sau functionalitatea CPU-ului.
# 

def console(function_name , msg):
    print(f"{function_name} : {msg}")

# =================================================================================================
# Importam buss-urile pentru a le afisa 

from ex_address_buss import EX_ADDRESS_BUSS 
from ex_control_buss import EX_CONTROL_BUSS
from ex_data_buss import EX_DATA_BUSS

# printam 
print(f"EX_ADDRESS_BUSS : {EX_ADDRESS_BUSS}")
print(f"EX_CONTROL_BUSS : {EX_CONTROL_BUSS}")
print(f"EX_DATA_BUSS : {EX_DATA_BUSS}")

# =================================================================================================
# Importam CU 

from cpu import CU_comp

p = CU_comp()

console("CLU",p)