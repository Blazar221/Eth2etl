from domain.committee import Committee
from utils.time_util import get_timestamp_epoch

def json_to_committees(json, epoch):
    committee_array = []

    epoch_timestamp = get_timestamp_epoch(epoch)
    raw_committees = json['committees']
    for key in raw_committees.keys():
        slot = int(key)
        for json_item in raw_committees[key]:

    for json_item in json['committees']:
        for slot in json['']
        committee = Committee()
        committee.epoch = epoch
        committee.epoch_timestamp = epoch_timestamp
        committee.slot
