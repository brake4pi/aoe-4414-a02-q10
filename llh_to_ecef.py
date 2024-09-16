# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  When given LLH terms, returns the ECEF radius vector
# Parameters:
# lat_deg: latitude in degrees
# lon_deg: longitude in degrees
# Output:
# r_x_km: x radius in km
# r_y_km: y radius in km
# r_z_km: z radius in km
#
# Written by Lee Wallenfang
# Other contributors: None
#

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456
# helper functions

## function description
def D2R(deg):
    return deg*math.pi/180

# initialize script arguments
lat_deg = 'Nan' # Latitude in degrees
lon_deg = 'Nan' # Longigude in degrees
hae_km = 'Nan' # Height above ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
   lat_deg = float(sys.argv[1])
   lon_deg = float(sys.argv[2])
   hae_km = float(sys.argv[3])
else:
   print(\
    'Usage: '\
    'python3 arg1 arg2 ...'\
   )
   exit()

# write script below this line

lat_rad = D2R(lat_deg)
lon_rad = D2R(lon_deg)

C_E = R_E_KM/(math.sqrt(1-((E_E**2)*(math.sin(lat_rad)**2))))
S_E = R_E_KM*(1-(E_E**2))/(math.sqrt(1-(E_E**2)*(math.sin(lat_rad)**2)))

r_x_km = (C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (S_E+hae_km)*math.sin(lat_rad)

print('r_x_km:', +r_x_km)
print('r_y_km:', +r_y_km)
print('r_z_km:', +r_z_km)