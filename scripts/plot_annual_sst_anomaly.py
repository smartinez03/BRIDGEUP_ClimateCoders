#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

	#Navigates to our data folder
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2017.nc')

	# Setting variables
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	#Slicing 
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]

	#Creates average temperature
	temp_mean = temp_sliced.mean()
	
	#Calculate anomalies
	temp_anom = temp[:,condition_depth,:,:] - temp_mean
	#temp_anom = (12,2,330,720)
	temp_anom_yr = temp_anom.mean(axis = 0)
	print(temp_anom_yr.shape)

#Execute main script
if __name__ == '__main__':
	main()
