#!usr/bin/python3
import api_service
import base_service
import data_service
import time

if __name__ == '__main__':	
	begin_time = time.time()
	print('begin')	
	base_service.save_attestation_csv()
	print('end, time is {:.3f}s'.format(time.time() - begin_time))
