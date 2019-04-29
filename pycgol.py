import sys
from os import system, name
from time import sleep

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
# The displayed simulation
playfield = [[False]*10]*10
nextfield = playfield
# Initially active cells in hexidecimal, 25 characters
'''
Default : 40080E0000000000000000000
 #
  #
###
'''
preset = str(sys.argv[2])
# Time between steps in milliseconds
timestep = sys.argv[1]/1000

