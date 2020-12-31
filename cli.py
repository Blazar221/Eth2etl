from service.base_service import extract_block, extract_committee, extract_validator, quest_genesis, quest_chainhead


def cli(argv):
	assert(len(argv) == 3)    
	assert(is_num(argv[2]))

	command = argv[1]
	value = int(argv[2])
	if 'extract_block' == command:
		extract_block(value)
	elif 'extract_validator' == command:
		extract_validator(value)
	elif 'extract_committee' == command:
		extract_committee(value)
	elif 'quest_genesis' == command:
		quest_genesis()
	elif 'quest_chainhead' == command:
		quest_chainhead()
	else:
		print(f'Command not found:{command}')


def is_num(v):
	try:
		num = int(v)
		return True
	except ValueError:
		return False

