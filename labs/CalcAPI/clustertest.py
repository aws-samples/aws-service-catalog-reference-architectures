#! /usr/bin/python
import random
import requests
import json
import threading 
from pycalc import dot_prod, get_rand_array

REMOTE_IP = ""
	
class calctest(threading.Thread):
    def __init__(self,len):
        super(calctest,self).__init__()
        self._len = len
        self._pyarr1 = self._getrandom()
        self._pyarr2 = self._getrandom()
        self._apival = 0.0
        self._localval = -1.0

    def _getrandom(self):
        #return [random.uniform(-5000000.0,5000000.0) for x in range(self._len)]
        return get_rand_array(self._len)

    def getremoterandom(self):
        print("get remote random")
        req = requests.get('http://{}/random/{}'.format(REMOTE_IP,self._len))
        r_json = req.json()
        return r_json

    def fullremote(self):
        print("fullremote")
        arr1 = self.getremoterandom()
        arr2 = self.getremoterandom()
        apidata = { "arr1":arr1,"arr2":arr2 }
        r_header = {'Content-Type':'application/json'}
        req = requests.post('http://{}/dotprod'.format(REMOTE_IP), data=json.dumps(apidata), headers=r_header)
        r_json = req.json()
        fval = float(r_json["result"])
        print("full remote:{}".format(fval))

    def getlocal(self):
        print("calc locally")
        self._localval = dot_prod(self._pyarr1,self._pyarr2)        

    def getremote(self):
        print("Sending request")
        apidata = { "arr1":self._pyarr1,"arr2":self._pyarr2 }
        r_header = {'Content-Type':'application/json'}
        req = requests.post('http://{}/dotprod'.format(REMOTE_IP), data=json.dumps(apidata), headers=r_header)
        r_json = req.json()
        self._apival = float(r_json["result"])
        
    def run(self):
        t1 = threading.Thread(target=self.getremote)
        t1.start()        
        t2 = threading.Thread(target=self.getlocal)
        t2.start()
        t3 = threading.Thread(target=self.fullremote)
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        print("{} passed:{}".format(self._apival, self._localval==self._apival))


if __name__ == "__main__":
    threads = []
    for x in range(10):
        calc = calctest(500000)
        threads.append(calc)
        calc.start()

    for t in threads:
        t.join()
