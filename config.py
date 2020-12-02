# local port config
PRYSM_ADDRESS = 'http://localhost:3500/'
# database config
DB = {
	'HOST': 'localhost',
	'NAME': 'eth2data',
	'USER': 'root',
	'PASSWORD': 'root',
	'PORT': 3306
}
# persistence method
METHOD = {'csv':0, 'db':1}
USE_METHOD = METHOD['csv']
# CSV spawning target location
CSV_PATH = './'


