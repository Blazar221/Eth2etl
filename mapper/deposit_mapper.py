from domain.deposit import Deposit


def json_item_to_deposit(json_item):
    deposit = Deposit()
    deposit.pubkey = json_item['data']['publicKey']
    deposit.withdrawal_credentials = json_item['data']['withdrawalCredentials']
    deposit.amount = json_item['data']['amount']
    deposit.signature = json_item['data']['signature']
    return deposit
