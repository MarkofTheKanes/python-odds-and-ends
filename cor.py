#! /usr/bin/env python3

import json
import pandas as pd

def getNodeUtil(nodeFileName):
    with open(nodeFileName, encoding='utf-8') as inputfile:
        data = json.loads(inputfile.read())

        nodeData= pd.json_normalize(data, record_path='nodes')
        clusterData=pd.json_normalize(data['clusterTotals'])

    nodeData.to_csv('node-utilization.csv', encoding='utf-8', index=False)
    clusterData.to_csv('cluster-utilization.csv', encoding='utf-8', index=False)

    return None

def getPodUtil(podFileName):
    with open(podFileName, encoding='utf-8') as inputfile:
        data = json.loads(inputfile.read())

        podData= pd.json_normalize(data, record_path=['nodes', 'pods'], meta=[['nodes', 'name']])

    podData.to_csv('pod-utilization.csv', encoding='utf-8', index=False)

    return None

getNodeUtil('nodes.json')
getPodUtil('pods.json')
