from service.base_service import extract_block, extract_committee, extract_validator, quest_genesis, quest_chainhead, \
    check_time, check_slot

HELP = 'The usage is below:\n' \
       'extract_block [slot]:      extract the blocks of slot as csv to output dir\n' \
       'extract_validator [epoch]: extract the validator of epoch as csv to output dir\n' \
       'extract_committee [epoch]: extract the committee of epoch as csv to output dir\n' \
       'quest_genesis:             quest the genesis information for the current beacon chain\n' \
       'quest_chainhead:           quest the chain head information for the current beacon chain\n' \
       'check_time:                check whether the current timestamp config is right\n' \
       'check_slot [slot]:         check whether the slot is available, if not print the current head slot'


def cli(argv):
    if len(argv) == 3:
        assert (is_num(argv[2]))
        command = argv[1]
        value = int(argv[2])
        if 'extract_block' == command:
            extract_block(value)
        elif 'extract_validator' == command:
            extract_validator(value)
        elif 'extract_committee' == command:
            extract_committee(value)
        elif 'check_slot' == command:
        	check_slot(value)
        else:
            print('Command not found:{}'.format(argv))
            print(HELP)
    elif len(argv) == 2:
        command = argv[1]
        if 'quest_genesis' == command:
            quest_genesis()
        elif 'quest_chainhead' == command:
            quest_chainhead()
        elif 'check_time' == command:
            check_time()
        elif '-h' == command or '--help' == command:
            print(HELP)
        else:
            print('Command not found:{}'.format(argv))
            print(HELP)
    else:
        print('Command not found:{}'.format(argv))
        print(HELP)


def is_num(v):
    try:
        num = int(v)
        return True
    except ValueError:
        return False
