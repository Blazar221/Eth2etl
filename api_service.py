#!usr/bin/python3
import requests
import encode
from config import PRYSM_ADDRESS as address


def attestations_epoch(epoch, pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/beacon/attestations?epoch={}'.format(epoch)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)
	return requests.get(url).json()
	

def attestations_genesis(pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/beacon/attestations?genesisEpoch=true'
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)
	return requests.get(url).json()
	

def attestations_epoch_indexed(epoch, pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/beacon/attestations/indexed?epoch={}'.format(epoch)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)
	return requests.get(url).json()
	

def attestations_genesis_indexed(genesis, pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/beacon/attestations/indexed?genesisEpoch={}'.format(genesis)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)
	return requests.get(url).json()

	
def attestations_pool():
	url = address + 'eth/v1alpha1/beacon/attestations/pool'
	return requests.get(url).json()
	
	
def block_single(root):
	url = address + 'eth/v1alpha1/beacon/blocks?root={}'.format(root)
	return requests.get(url).json()
	

def block_slot(slot, pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/beacon/blocks?slot={}'.format(slot)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)
	return requests.get(url).json()
	 

def block_epoch(epoch, pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/beacon/blocks?epoch={}'.format(epoch)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)
	return requests.get(url).json()
	

def block_genesis():
	url = address + 'eth/v1alpha1/beacon/blocks?genesis=true'
	return requests.get(url).json()
	
	
def chainhead():
	url = address + 'eth/v1alpha1/beacon/chainhead/stream'
	return requests.get(url).json()
	

def committees_epoch(epoch):
	url = address + 'eth/v1alpha1/beacon/committees?epoch={}'.format(epoch)
	return requests.get(url).json()
	

def committees_genesis():
	url = address + 'eth/v1alpha1/beacon/committees?genesis=true'
	return requests.get(url).json()


def config():
	url = address + 'eth/v1alpha1/beacon/config'
	return requests.get(url).json()


def individual_votes(public_keys, indices, epoch = 0):
	url = address + 'eth/v1alpha1/beacon/individual_votes?epoch={}'.format(epoch)
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	return requests.get(url).json()


def validator_index(index):
	url = address + 'eth/v1alpha1/validator?index={}'.format(index)
	return requests.get(url).json()


def validator_public_key(public_key):
	url = address + 'eth/v1alpha1/validator?publicKey={}'.format(encode.safe_url_base64(public_key))
	return requests.get(url).json()


def validators_epoch(epoch, active = False, indices = [], public_keys = [], pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/validators?epoch={}'.format(epoch)
	if active:
		url = url + '&active=true'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)	
	return requests.get(url).json()


def validators_default():
	url = address + 'eth/v1alpha1/validators'
	return requests.get(url).json()
	

def validators_genesis(active = False, indices = [], public_keys = [], pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/validators?genesis=true'
	if active:
		url = url + '&active=true'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)	
	return requests.get(url).json()


def validators_activesetchanges_epoch(epoch):
	url = address + 'eth/v1alpha1/validators/activesetchanges?epoch={}'.format(epoch)
	return requests.get(url).json()
	

def validators_activesetchanges_genesis():
	url = address + 'eth/v1alpha1/validators/activesetchanges?genesis=true'
	return requests.get(url).json()


def validators_assignments_epoch(epoch, indices = [], public_keys = [], pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/validators/assignments?epoch={}'.format(epoch)
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)	
	return requests.get(url).json()
	
	
def validators_assignments_genesis(indices = [], public_keys = [], pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/validators/assignments?genesis=true'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)	
	return requests.get(url).json()
	

def validators_balances_epoch(epoch, indices = [], public_keys = [], pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/validators/balances?epoch={}'.format(epoch)
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)	
	return requests.get(url).json()
	
	
def validators_balances_genesis(indices = [], public_keys = [], pageSize = None, pageToken = None):
	url = address + 'eth/v1alpha1/validators/balances?genesis=true'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	if pageSize:
		url = url + '&pageSize={}'.format(pageSize)
	if pageToken:
		url = url + '&pageToken={}'.format(pageToken)	
	return requests.get(url).json()
	
	
def validators_participation_epoch(epoch):
	url = address + 'eth/v1alpha1/validators/participation?epoch={}'.format(epoch)
	return requests.get(url).json()


def validators_participation_genesis():
	url = address + 'eth/v1alpha1/validators/participation?genesis=true'
	return requests.get(url).json()
	
def validators_performance(public_keys, indices):
	url = address + 'eth/v1alpha1/validators/performance?'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	print(url.replace('&', '', 1))
	return requests.get(url.replace('&', '', 1)).json()
	

def validators_queue():
	url = address + 'eth/v1alpha1/validators/queue'
	return requests.get(url).json()
	
	
def node_genesis():
	url = address + 'eth/v1alpha1/node/genesis'
	return requests.get(url).json()
	

def node_peers():
	url = address + 'eth/v1alpha1/node/peers'
	return requests.get(url).json()
	
	
def node_services():
	url = address + 'eth/v1alpha1/node/services'
	return requests.get(url).json()
	
	
def node_syncing():
	url = address + 'eth/v1alpha1/node/syncing'
	return requests.get(url).json()
	

def node_version():
	url = address + 'eth/v1alpha1/node/version'
	return requests.get(url).json()
	

def validator_activation_stream(public_keys):
	url = address + 'eth/v1alpha1/validator/activation/stream?'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	return requests.get(url.replace('&', '', 1)).json()
	 
			
def validator_aggregate():
	url = address + 'eth/v1alpha1/validator/aggregate'
	return requests.post(url).json()


def validator_block():
	url = address + 'eth/v1alpha1/validator/block'
	return requests.post(url).json()
	
	
def validator_chainstart_stream():
	url = address + 'eth/v1alpha1/validator/chainstart/stream'
	return requests.get(url).json()


def validator_domain():
	url = address + 'eth/v1alpha1/validator/domain'
	return requests.get(url).json()


def validator_duties():
	url = address + 'eth/v1alpha1/validator/duties/stream?epoch=1'
	return requests.get(url).json()


def validator_exit():
	url = address + 'eth/v1alpha1/validator/exit'
	return requests.post(url).json()
	

def validator_key2index(public_keys):
	url = address + 'eth/v1alpha1/validator/index?'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(item)
	print(url.replace('&', '', 1))
	return requests.get(url.replace('&', '', 1)).json()
	

def validator_status(public_keys):
	url = address + 'eth/v1alpha1/validator/status?'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	return requests.get(url.replace('&', '', 1)).json()
	
	
def validator_statuses(public_keys, indices):
	url = address + 'eth/v1alpha1/validator/statuses?'
	for item in public_keys:
		url = url + '&publicKeys={}'.format(encode.safe_url_base64(item))
	for item in indices:
		url = url + '&indices={}'.format(item)
	print(url.replace('&', '', 1))
	return requests.get(url.replace('&', '', 1)).json()
	

def validator_subnet_subscribe():
	url = address + 'eth/v1alpha1/validator/subnet/subscribe'
	return requests.post(url).json()
	

def validator_synced_stream():
	url = address + 'eth/v1alpha1/validator/synced/stream'
	return requests.get(url).json()
	
	
if __name__ == '__main__':
	print('begin')
	print(chainhead())	
	print('end')

