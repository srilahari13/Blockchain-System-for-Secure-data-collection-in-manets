from flask import Flask, render_template, request
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

app=Flask(__name__)

@app.route('/')
def displaySensoryData():
    contract,web3=connect_with_data_blockchain()
    a,b,c=contract.functions.viewData().call()
    data=[]
    for i in range(len(a)):
        dummy=[]
        dummy.append(a[i].decode('utf-8'))
        dummy.append(b[i].decode('utf-8'))
        dummy.append(c[i].decode('utf-8'))
        data.append(dummy)
    l=len(data)
    return render_template('index.html',dashboard_data=data,len=l)

if __name__=="__main__":
    app.run()