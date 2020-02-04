#Import packages

#Create functions
<<<<<<< HEAD

#Main script
def main():

	#Step 1: Import data file
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2017.nc')

	#Step 2: Save the necessary variables
	lon = data.variables['lon'][:]
	lat = data.variables['lat'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean']
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	#Step 3: Find mean SST
	temp_mean = temp[:,:,:,:].mean()

	#Step 4: Find SST anomaly
	temp_anom = temp - temp_mean

#Execute main script
=======
def hello(name):
	print('Hello',name)

#Main script
def main():
	
	name = 'Beyonce'
	hello(name)

#Run script
>>>>>>> a57bc8fe50f771c6a1333be74be4eb04c12f155d
if __name__ == '__main__':
	main()