
from config.web3Config import RPC
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


W3 = Web3(HTTPProvider(RPC))
W3.middleware_onion.inject(geth_poa_middleware, layer=0)
