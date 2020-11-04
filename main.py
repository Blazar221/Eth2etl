#!usr/bin/python3
import api_service
import base_service
import data_service
import time

if __name__ == '__main__':	
	begin_time = time.time()
	print('begin')	
	print(base_service.read_validator(id = 0))
	print('end, time is {:.3f}s'.format(time.time() - begin_time))
