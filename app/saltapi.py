import urllib3,json
import sys

URL="localhost:8000/login"
USER="adefyer"
PASSWORD='112358'

class SaltRestFul(object):
    def __init__(self):
        self.URL=URL
        self.USER=USER
        self.PASSWORD=PASSWORD
        self.http  = urllib3.PoolManager()
        self.AUTHTOKEN=self._getToken()
        self.requestHeader={'Accept':'application/json','Content-Type':'application/json','X-Auth-Token':self.AUTHTOKEN}
    def _getToken(self):
        data  = {"username":self.USER,"password":self.PASSWORD,"eauth":"pam"}
        dataj = json.dumps(data)
        try:
            r     = self.http.urlopen('POST',url=self.URL,headers={'Content-Type':'application/json'},body=dataj)
            result=json.loads(r.data)
            return result['return'][0]['token']
        except:
            print 'request error'
    def getGrains(self):
        print self.AUTHTOKEN
        r     = self.http.urlopen('GET',url="localhost:8000/minions/",headers={'Accept':'application/json','Content-Type':'application/json','X-Auth-Token':self.AUTHTOKEN})
        result= json.loads(r.data)

        return result
    def Run(self,client,tgt,fun,arg):
        data   =  [{"client":client,"tgt":tgt,"fun":fun,"arg":arg,"username":"adefyer","password":"112358","eauth":"pam"}]
        dataj  = json.dumps(data,allow_nan=True)
        r     = self.http.urlopen(method="POST",url="localhost:8000/run",headers=self.requestHeader,body=dataj)
        return r.data 


    def _logout(self):
        r     = self.http.urlopen('POST',url='localhost:8000/logout',headers=self.requestHeader)
        result = json.loads(r.data)
        print result

