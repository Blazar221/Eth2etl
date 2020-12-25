from domain.volutary_exit import VoluntaryExit


def json_item_to_volutary_exit(json_item):
    volutary_exit = VoluntaryExit()
    volutary_exit.epoch = json_item['exit']['epoch']
    volutary_exit.validator_index = json_item['exit']['validatorIndex']
    volutary_exit.signature = json_item['signature']
    return volutary_exit
