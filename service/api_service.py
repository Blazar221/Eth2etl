import requests
from config import PRYSM_ADDRESS as ADDRESS

session = requests.Session()


def get_block(slot, page_token=None):
    url = '{}/eth/v1alpha1/beacon/blocks?slot={}'.format(ADDRESS, slot)
    if page_token:
        url = '{}&page_token={}'.format(url, page_token)
    return _make_get_request(url)


def get_validator(epoch, page_token=None):
    if page_token:
        return [_vld_task(epoch, page_token)]
    resp_array = []
    resp = _vld_task(epoch)
    while resp['nextPageToken']:
        resp_array.append(resp)
        resp = _vld_task(epoch, resp['nextPageToken'])
    resp_array.append(resp)
    return resp_array


def get_validator_balance(epoch, page_token=None):
    if page_token:
        return [_vld_balance_task(epoch, page_token)]
    resp_array = []
    resp = _vld_balance_task(epoch)
    while resp['nextPageToken']:
        resp_array.append(resp)
        resp = _vld_balance_task(epoch, resp['nextPageToken'])
    resp_array.append(resp)
    return resp_array


def get_committee(epoch):
    url = '{}/eth/v1alpha1/beacon/committees?epoch={}'.format(ADDRESS, epoch)
    return _make_get_request(url)


def get_genesis_detail():
    url = '{}/eth/v1alpha1/node/genesis'.format(ADDRESS)
    return _make_get_request(url)


def get_chainhead():
    url = '{}/eth/v1alpha1/beacon/chainhead/stream'.format(ADDRESS)
    return _make_get_request(url)


def _vld_task(epoch, page_token=None):
    url = '{}/eth/v1alpha1/validators?epoch={}'.format(ADDRESS, epoch)
    if page_token:
        url = '{}&page_token={}'.format(url, page_token)
    return _make_get_request(url)


def _vld_balance_task(epoch, page_token=None):
    url = '{}/eth/v1alpha1/validators/balances?epoch={}'.format(ADDRESS, epoch)
    if page_token:
        url = '{}&page_token={}'.format(url, page_token)
    return _make_get_request(url)


def _make_get_request(url):
    resp = session.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print('failed on {} with code:{}, {}'.format(url, resp.status_code, resp.json()))
        return {}
