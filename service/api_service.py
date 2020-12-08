import requests
from config import PRYSM_ADDRESS as ADDRESS

session = requests.Session()


def get_block(slot, page_token=None):
    url = f'{ADDRESS}/eth/v1alpha1/beacon/blocks?slot={slot}'
    if page_token:
        url = f'{url}&page_token={page_token}'
    return _make_get_request(url)


def get_validators(epoch, page_token=None):
    url = f'{ADDRESS}/eth/v1alpha1/validators?epoch={epoch}'
    if page_token:
        url = f'{url}&page_token={page_token}'
    return _make_get_request(url)


def get_committee(epoch):
    url = f'{ADDRESS}/eth/v1alpha1/beacon/committees?epoch={epoch}'
    return _make_get_request(url)


def get_genesis_detail():
    url = f'{ADDRESS}/eth/v1alpha1/node/genesis'
    return _make_get_request(url)


def get_chainhead():
    url = f'{ADDRESS}/eth/v1alpha1/beacon/chainhead/stream'
    return _make_get_request(url)


def _make_get_request(url):
    return session.get(url).json()
