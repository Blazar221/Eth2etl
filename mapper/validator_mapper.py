from domain.validator import Validator


def json_array_to_validators(json_vld_array, json_balance_array):
    validators = []
    #balance_dict = _get_balance_dict(json_balance_array)
    for item in json_vld_array:
        validator = Validator()

        vld_data = item['validator']

        validator.pubkey = vld_data['publicKey']
        validator.validator_index = int(item['index'])
        #validator.balance = balance_dict[item['index']]
        validator.balance = 21
        validator.withdrawal_credentials = vld_data['withdrawalCredentials']
        validator.effective_balance = vld_data['effectiveBalance']
        validator.slashed = vld_data['slashed']
        validator.activation_eligibility_epoch = vld_data['activationEligibilityEpoch']
        validator.activation_epoch = vld_data['activationEpoch']
        validator.exit_epoch = vld_data['exitEpoch']
        validator.withdrawable_epoch = vld_data['withdrawableEpoch']
        validators.append(validator)
    return validators


def _get_balance_dict(json_balance_array):
    balance_dict = {}
    for item in json_balance_array:
        balance_dict[item['index']] = item['balance']
    return balance_dict
