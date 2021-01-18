from domain.attestation import Attestation
from base64 import standard_b64decode


def json_item_to_attestation(json_item):
    attestation = Attestation()
# Keep the raw aggregation_bits here, because the converting it to 01 combination is not verified yet. 
#   attestation.aggregation_bits = hex_to_aggregation_bits(json_item['aggregationBits'])
	attestation.aggregation_bits = json_item['aggregationBits']	

    raw_data = json_item['data']

    attestation.slot = raw_data['slot']
    attestation.index = raw_data['committeeIndex']
    attestation.beacon_block_root = raw_data['beaconBlockRoot']

    attestation.source_epoch = raw_data['source']['epoch']
    attestation.source_root = raw_data['source']['root']
    attestation.target_epoch = raw_data['target']['epoch']
    attestation.target_root = raw_data['target']['root']

    attestation.signature = json_item['signature']

    return attestation


def hex_to_aggregation_bits(hex_aggregation_bits):
    aggregation_bits = to_binary(hex_aggregation_bits)
    if len(aggregation_bits) >= 1:
        # The first set bit indicates the start of aggregation bits
        # The binary string returned by to_binary() always starts with 1
        aggregation_bits = aggregation_bits[1:]
    return aggregation_bits


# The correctness of the base64 decode is not verified yet
def to_binary(hex_data):
    if hex_data is None or len(hex_data) == 0:
        return hex_data

    if hex_data.startswith('0x'):
        hex_data = hex_data[2:]

    b = standard_b64decode(hex_data)

    binary = bin(int.from_bytes(b, byteorder='little'))

    if binary is not None and binary.startswith('0b'):
        binary = binary[2:]
    return binary
