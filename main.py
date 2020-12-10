#!usr/bin/python3
from service.base_service import extract_block, extract_committee, extract_validator
import service.api_service as api
import time

if __name__ == '__main__':	
	begin_time = time.time()
	print('begin')
	extract_validator(1000)
	print('time is {:.3f}s'.format(time.time() - begin_time))
