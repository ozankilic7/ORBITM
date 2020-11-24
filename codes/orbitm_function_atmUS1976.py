###########################################################
###########################################################
###    Created on Wed May 24 11:27:54 2017              ###
###    Updated on Thu Oct 22 15:55:15 2020              ###
###    By Samuel Low, DSO National Laboratories         ###
###    Atmospheric Density Model                        ###
###    U.S. Standard Atmosphere Table 1976              ###
###    Valid only for altitudes 86km to 1000km          ###
###########################################################
###########################################################

import math

def AtmosDensity(R):
    
    # Input R is the altitude from the surface of the Earth (km)
    
    co = [0,0,0,0,0] # Coefficient
    
    if R <= 86:
        co = [ 0.0000000000, 0.0000000000, 0.0000000000,-0.1523325,  0.202941]
    elif R <= 91:
        co = [ 0.0000000000,-3.322622e-06, 9.111460e-04,-0.2609971,  5.944694]
    elif R <= 100:
        co = [ 0.0000000000, 2.873405e-05,-0.008492037,  0.6541179, -23.62010]
    elif R <= 110:
        co = [-1.240774e-05, 0.005162063, -0.8048342,    55.55996,  -1443.338]
    elif R <= 120:
        co = [ 0.0000000000,-8.854164e-05, 0.03373254,  -4.390837,   176.5294]
    elif R <= 150:
        co = [ 3.661771e-07,-2.154344e-04, 0.04809214,  -4.884744,   172.3597]
    elif R <= 200:
        co = [ 1.906032e-08,-1.527799e-05, 0.004724294, -0.6992340,  20.50921]
    elif R <= 300:
        co = [ 1.199282e-09,-1.451051e-06, 6.910474e-04,-0.1736220, -5.321644]
    elif R <= 500:
        co = [ 1.140564e-10,-2.130756e-07, 1.570762e-04,-0.07029296,-12.89844]
    elif R <= 750:
        co = [ 8.105631e-12,-2.358417e-09,-2.635110E-06,-0.01562608,-20.02246]
    elif R <= 1000:
        co = [-3.701195e-12,-8.608611e-09, 5.118829e-05,-0.06600998,-6.137674]
    else:
        co = [0,0,0,0,0]
        
    # Compute the exponent term.
    AtmosExp  = co[0]*(R**4)
    AtmosExp += co[1]*(R**3)
    AtmosExp += co[2]*(R**2)
    AtmosExp += co[3]*(R)
    AtmosExp += co[4]*(1)
    
    # Return the atmospheric density (kg/m^3)
    return math.exp(AtmosExp)