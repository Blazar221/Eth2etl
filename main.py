#!usr/bin/python3
from service.base_service import extract_block
import service.api_service as api
import time

if __name__ == '__main__':	
	begin_time = time.time()
	print('begin')
	print(api.get_committee(20))
	print('time is {:.3f}s'.format(time.time() - begin_time))
