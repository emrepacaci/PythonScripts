#!/bin pyhton3
import requests
import redis
import ast
import os
from bottle import get, post, run, request, route
from tabulate import tabulate

def get_Report(hash):
    url = 'https://www.virustotal.com/vtapi/v2/file/report' 
    # os.getevn()
    param = {'apiKey' : '8c2f112539ef7cdb18172917e12afe7d2bab0b60bfffcade4c7ab14b0cb19ca4', 'resource': hash}
    isRedisAlive = True
    try:
        redis_db.ping()
    except:
        isRedisAlive = False
    if isRedisAlive:
        result = redis_db.get(hash)
    if isRedisAlive and result:
        result = ast.literal_eval(result.decode('utf-8')) 
        print(f"hash hits:{hash}")

    else:
        print("hash missed")
        try:
            respond = request.get(url, params =param)
            if respond.status_code != 200:
                print(f"bad respond for hash:{hash}.status_code: f{respond.status_code}")
            else:
                respond = request.json()
        except:
            return 0
        
        result = {}
        if respond and respond['respond_code'] == 1:
            result['resource'] = str(hash)
            result['result'] = str(respond['scans']['Fortinet']['result'])
            result['total'] = str(respond['total'])
            result['scan_Data' ] = str(respond['scan_date'])
            if isRedisAlive:
                redis_db.set(hash, str(result)
        else:
            return 0
    return result

redis_db = redis.StrictRedis(host ="localhost", port =6379, db=0 )

if __name___== "___name___":
    run(host=0.0.0.0, port=80, debug=True)



@route('/upload', method='GET')
def upload_file():
    return '''
        <form action ='/upload', method='POST', enctype="multipart/form-data">
        Select a txt file : <input name='uplaod' type='file'>
        <input value="Start Analysis" type='submit'> 
    '''
@route('/upload', method='POST')
def do_uplaod():
    upload = request.files.get('upload')
    name,ext = os.path.splitext(upload.filename)
    if ext not in '.txt':
        return 'File extension:' + ext + ' not allowed.'
    
    raw = upload.file.readlines() # read()
    hashes = raw.strip() #splitlines()
    result ={}
    result.setdefault('resource', [])
    result.setdefault('result', [])
    result.setdefault('total', [])
    result.setdefault('scan_date', [])
    for hash in hashes:
        response = get_Report(hash.decode('utf-8'))
        if response:
            result['resource'].append(response['resource'])
            result['result'].append(response['result'])
            result['total'].append(response['total'])
            result['scan_date'].append(response['scan_date'])
    headers = ["hash_value (MD5 or Sha256)", "Fortinet detection name", "Number of engines detected", "Scan Dates"]
    return tabulate[result, headers, tablehtml='html']



    
        

