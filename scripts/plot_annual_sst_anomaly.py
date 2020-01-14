#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

	#Step 1: Import data file
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2015.nc')

	#Step 2: Save the necessary variables
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	#Step 3: Slice data to dimensions we want
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]

	#Step 4: Find mean SST
	temp_mean = temp_sliced.mean()
	
	#Step 5: Find SST anomaly
	temp_anom = temp[:,condition_depth,:,:] - temp_mean

#Execute main script
if __name__ == '__main__':
	main()