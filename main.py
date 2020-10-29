#!usr/bin/python3
import api_service
import base_service
import time

if __name__ == '__main__':
	begin_time = time.time()
	print('begin')	
	base_service.save_block_epoch(0, 1)			
	print('end, time is {:.3f}s'.format(time.time() - begin_time))

