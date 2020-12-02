#!usr/bin/python3
import api_service
import base_service
import time

if __name__ == '__main__':	
	begin_time = time.time()
	print('begin')	
	(blocks, _, _, _, _, _) = base_service.request_block_epoch(0, 0)
	base_service.save_blocks_csv(blocks, 0)
	print('end, time is {:.3f}s'.format(time.time() - begin_time))
