from hashlib import md5, sha1
import json

def response(sts = 0, data = None, token = None):
    return json.dumps({sts: 0, data: data, _token: token})

def hash(data, type='md5'):
    if type == 'md5':
        return md5(data.encode()).hexdigest()
    elif type == 'sha1':
        return sha1(data.encode()).hexdigest()