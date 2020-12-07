import requests
from config import PRYSM_ADDRESS as ADDRESS


def get_block(slot, page_token=None):
    url = ADDRESS + f'eth/v1alpha1/beacon/blocks?{slot}'
    if page_token:
        url = url + f'&page_token={page_token}'
    return requests.get(url).json()


def get_validators(page_token=None):
    url = ADDRESS + 'eth/v1alpha1/validators'
    if page_token:
        url = url + f'?page_token={page_token}'
    return requests.get(url).json()


def get_committee(epoch):
    url = ADDRESS + f'eth/v1alpha1/beacon/committees?epoch={epoch}'
    return requests.get(url).json()


def get_genesis_detail():
    url = ADDRESS + 'eth/v1alpha1/beacon/blocks?genesis=true'
    return requests.get(url).json()


def get_chainhead():
    url = ADDRESS + 'eth/v1alpha1/beacon/chainhead/stream'
    return requests.get(url).json()
