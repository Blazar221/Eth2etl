from mapper.beacon_block_mapper import json_to_single_block
from service.api_service import get_block, get_committee
from service.csv_service import save_blocks


def extract_block(slot_head, slot_end):
    blocks = [json_to_single_block(get_block(slot), slot)
              for slot in range(slot_head, slot_end)]
    save_blocks(blocks, slot_head, slot_end)


def extract_committee(epoch_head, epoch_end):
    committees = [json_to_committee(get_committee(epoch))
                  for epoch in range(epoch_head, epoch_end)]
