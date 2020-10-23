#!usr/bin/python3
import api_service
import base_service
import data_service


if __name__ == '__main__':
	print('begin')
	raw_data = api_service.block_epoch(1, pageSize = 2)
	for each in raw_data['blockContainers']:
		for key in each.keys():
			if key == 'block':
				for k in each[key][key].keys():
					print('{}:{}'.format(k, each[key][key][k]))
			else:
				print('{}:{}'.format(key, each[key]))
			print('-------------------------------------------')
	print('end')

