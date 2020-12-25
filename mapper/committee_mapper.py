from domain.committee import Committee
from utils.time_util import get_timestamp_epoch


def json_to_committees(json, epoch):
    committee_array = []

    epoch_timestamp = get_timestamp_epoch(epoch)

    raw_committees = json['committees']
    for key in raw_committees.keys():
        slot = int(key)
        index = 0
        for item_array in raw_committees[key]['committees']:
            assert 1 == len(item_array)
            vld_array = item_array['validatorIndices']
            cmt = Committee()
            cmt.epoch = epoch
            cmt.epoch_timestamp = epoch_timestamp
            cmt.slot = slot
            cmt.index = index
            cmt.committee = [int(vld) for vld in vld_array]
            committee_array.append(cmt)
            index += 1

    return committee_array
