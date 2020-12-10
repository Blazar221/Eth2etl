import requests
from multiprocessing import Pool
from config import PRYSM_ADDRESS as ADDRESS

session = requests.Session()


def get_block(slot, page_token=None):
    url = f'{ADDRESS}/eth/v1alpha1/beacon/blocks?slot={slot}'
    if page_token:
        url = f'{url}&page_token={page_token}'
    return _make_get_request(url)


def get_validator(epoch, page_token=None):
    if page_token:
        return __vld_task(epoch, page_token)
    with Pool(processes=2) as p:
        return p.starmap(__vld_task, [(epoch, page) for page in range(20)])


def __vld_task(epoch, page_token=None):
    url = f'{ADDRESS}/eth/v1alpha1/validators?epoch={epoch}'
    if page_token:
        url = f'{url}&page_token={page_token}'
    return _make_vld_request(url, page_token)


def get_validator_balance(epoch, page_token=None):
    url = f'{ADDRESS}/eth/v1alpha1/validators/balances?epoch={epoch}'
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


def _make_vld_request(url, page):
    resp = session.get(url)
    if resp.status_code == 200:
        print(f'success at page{page}')
        return resp.json()
    else:
        print(f'fail at page{page}:{resp.status_code}')
        return {}


def _make_get_request(url):
    resp = session.get(url)
    if resp.status_code == 200:
        print('success')
        return resp.json()
    else:
        print(resp.status_code)
        return {}
