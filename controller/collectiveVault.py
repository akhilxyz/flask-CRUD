import json
from core.models.chainsModel import chainDetails
from core.models.predictionsModel import Perdictions
from core.models.resolvedPredictionsModel import ResolvedPerdictions
from service.contractService import CallContract
from config.web3Config import CollectiveVault_Address
from service.web3 import W3


class CollectiveVaultController(object):
    def __init__(self):
        # getting network details
        network = chainDetails.objects.get(chainId=4)
        # importing ABI
        abiArray = json.load(open("./config/abi/ABI_CollectiveVault.json"))
        # current Block number
        blockNo = W3.eth.block_number
        if blockNo > network.perBlockNo:
            self.perdictionsEvent(network.perBlockNo, abiArray)

        if blockNo > network.resolvePerBlockNo:
            self.resolvePerdictionsEvent(network.resolvePerBlockNo, abiArray)

    # function for call Perdictions event
    def perdictionsEvent(self, blockNo, abiArray):
        try:

            # calling Contract
            contract = CallContract(CollectiveVault_Address, abiArray)

            # calling Contract Event
            blockDiff = blockNo + 500
            _blockNo = W3.eth.block_number
            if _blockNo > blockDiff:
                _blockNo = blockDiff

            transferEvent = contract.events.Predictions()
            event_filter = transferEvent.createFilter(
                fromBlock=blockNo, toBlock=_blockNo)

            # fetching all enteries of contract event
            eventlist = event_filter.get_all_entries()

            # fetching Event Details one by one
            for x in eventlist:
                decimals = contract.functions.getDecimals(x.args.token).call()
                amount = x.args.amount / 10 ** 18
                price = x.args.price / 10 ** int(decimals)
                totalAmount = x.args.totalAmount / 10 ** 18

                event = Perdictions(
                    counter=x.args.counter,
                    predictionType=x.args.predictionType,
                    amount=amount,
                    price=price,
                    token=x.args.token,
                    totalAmount=totalAmount,
                    endTime=x.args.endTime,
                    status=False,  # default status
                    chainId=4,  # static
                    transactionHash=x.transactionHash.hex(),
                    user=x.args.user,
                    blockNumber=x.blockNumber,
                )
                event.save()

            BlockNumber = chainDetails.objects(chainId=4)
            BlockNumber.update(perBlockNo=_blockNo)
            print("Perdictions Event Updated")

        except Exception as e:
            return print("An exception occurred", e)

     # function for call Resove Predictions event

    def resolvePerdictionsEvent(self, blockNo, abiArray):
        try:
            # calling Contract
            contract = CallContract(CollectiveVault_Address, abiArray)

            # calling Contract Event
            blockDiff = blockNo + 500
            _blockNo = W3.eth.block_number
            if _blockNo > blockDiff:
                _blockNo = blockDiff
            # else:
            #     _blockNo = blockNo

            resolveEvent = contract.events.ResolvedPredictions()
            event_filter = resolveEvent.createFilter(
                fromBlock=blockNo, toBlock=_blockNo)

            # fetching all enteries of contract event
            eventlist = event_filter.get_all_entries()

            # fetching Event Details one by one
            for x in eventlist:
                decimals = contract.functions.getDecimals(x.args.token).call()
                amount = x.args.amount / 10 ** 18
                price = x.args.price / 10 ** int(decimals)
                finalPrice = x.args.finalPrice / 10 ** int(decimals)
                totalAmount = x.args.totalAmount / 10 ** 18

                event = ResolvedPerdictions(
                    counter=x.args.counter,
                    predictionType=x.args.predictionType,
                    amount=amount,
                    price=price,
                    token=x.args.token,
                    finalPrice=finalPrice,
                    totalAmount=totalAmount,
                    resolvedTime=x.args.resolvedTime,
                    status=False,  # default status
                    chainId=4,  # static chainId
                    transactionHash=x.transactionHash.hex(),
                    user=x.args.user,
                    blockNumber=x.blockNumber
                )
                event.save()

            BlockNumber = chainDetails.objects(chainId=4)
            BlockNumber.update(resolvePerBlockNo=_blockNo)
            print("Resolve Perdictions Event Updated")

        except Exception as e:
            return print("An exception occurred", e)
