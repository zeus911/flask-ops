import urllib3,json

http = urllib3.PoolManager()
data   =  [{"client":"local","tgt":"*","fun":"test.ping"}]
dataj  = json.dumps(data)
r     = http.urlopen(method="POST",url="localhost:8000/run",headers={"Accept":"application/x-yaml","Content-Type":"application/json"},body=dataj)
print r.data
