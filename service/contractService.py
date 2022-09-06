from service.web3 import W3


def CallContract(Contract_Address, Contract_ABI):
    contract = W3.eth.contract(address=Contract_Address, abi=Contract_ABI)
    return contract
