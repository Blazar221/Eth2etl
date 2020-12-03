#!usr/bin/python3
import api_service
import base_service
import time


if __name__ == '__main__':	
	begin_time = time.time()
	print('begin')	
	blocks, attestations, deposits, exitings, slashingas, slashingps, cmts = base_service.request_block_epoch(10, 12)
	base_service.save_csv(blocks, 'block')
	base_service.save_csv(attestations, 'attestation')
	base_service.save_csv(deposits, 'deposit')
	base_service.save_csv(exitings, 'exiting')
	base_service.save_csv(slashingas, 'slashinga')
	base_service.save_csv(slashingps, 'slashingp')
	base_service.save_csv(cmts, 'committee')
	print('end, time is {:.3f}s'.format(time.time() - begin_time))

