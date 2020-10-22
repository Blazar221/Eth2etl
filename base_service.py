from entity import *


# Parse raw json from prysm api to attestion entity array
def json_to_attestation_array(json):
	res = []
	for each in json['attestations']:
		raw_data = each['data']
		item = attestation(each['aggregationBits'], raw_data['slot'], raw_data['committeeIndex'], raw_data['beaconBlockRoot'], raw_data['source']['epoch'], raw_data['source']['root'], raw_data['target']['epoch'], raw_data['target']['root'], each['signature'])
		res.append(item)
	return res

