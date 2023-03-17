from web3 import Web3,HTTPProvider
import json

def connect_with_data_blockchain(acc):
    blockchainServer='http://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchainServer))
    if acc==0:
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='build/contracts/data.json'
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
        contract_address=contract_json['networks']['5777']['address']
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    return (contract,web3)

def main(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    contract,web3=connect_with_data_blockchain(0)
    tx_hash=contract.functions.insertData(a,b,c).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Data Added to Blockchain')
    




