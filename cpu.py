# cpu.py

# =================================================================================================
# Importam firele ce vin legate in CPU, si restu componentelor.

from ex_data_buss import EX_DATA_BUSS
from ex_control_buss import EX_CONTROL_BUSS
from ex_address_buss import EX_ADDRESS_BUSS

# importam clock

from clock import CLOCK_SIGNAL

# =================================================================================================
# CU -  Control Unit

# comp = component

"""
microcode_rom =  aici salvam instructiunile hex, ce is only read, in CU ,
acestea pot fi citite doar de CU_comp, ce in fucntei de ele , trimite anumite 
date ex , read,write , etc... 
"""
MICROCODE_ROM = {
    "0x00" : [ # LOAD
        "MOVE_DATA_ON__IN_ADDRESS_BUSS",
        "ENABLE_MEM_READ",
        "CLOSE_REG_A_GATE"
    ]
}

def CU_comp(hex_code):
    pass

# =================================================================================================
# ALU - Arithmetic Logic Unit

"""
ALU -  in el se afla diferite componente logice mici , AND,OR,XOR ,
el find doar o locatie ce le tine pe toate intr-un loc.

ALU - are 2 parit, AU si LU ,
AU - atihemtic unit (mate mica , aduanre,minus,inmultire,impartire)
LU - logic Unit , (verificari de tip fals adevarat doar)

ALU - salveaza rezultautl in reg_a, dar seteaza si niste flaguri pentru CU 
"""

def ALU_comp(data_a , data_b , control_signal):
    pass 

# =================================================================================================
# REGS -  registri

regs  = {
    # special regs 
    "PC" : "", # program counter
    "IR" : "", # instruction register
    "FLAGS" : "", # flagurile 

    # registri
    "reg_a" : "",
    "reg_b" : ""
}

def REGS_comp():
    pass 


# =================================================================================================
# CACHE 

"""
Cautam in L_1 , daca nu e acolo mergem in L_2 apoi in L_3.
"""

LS = {
    # fast
    #"L_1" : "", L_1 , e impartit in 2 componente mai mici.
    "L_1_i" : "",
    "L_1_d" : "",
    # medium
    "L_2" : "",
    # slow
    "L_3" : ""
}

def CACHE_comp():
    pass

# =================================================================================================
# _BUS - buzuri de transportare date intre copmponente ,ALU,CU,Etc...

# IN - internel buss , in interiorul unei componente
# EX - external buss , in exteriorul unei componente cu alte componente

"""
logica : 

[dute]
address_buss , primeste adresa ce sa apleze 
control_buss ,  primeste instrucitunea ce sa faca la acea adrsa 

[vino]
data_buss , primeste oputputl de la ce a facut mai sus .

"""

def IN_DATA_BUSS():
    pass 

def IN_ADDRESS_BUSS():
    pass 

def IN_CONTROL_BUSS():
    pass 

