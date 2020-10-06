#! /usr/bin/python
import time
import requests
import json
import threading 

REMOTE_IP = ""
	
class calctest(threading.Thread):
    def __init__(self,len):
        super(calctest,self).__init__()
        self._len = len
        self._pyarr1 = []
        self._pyarr2 = []
        self._apival = 0.0
        self._localval = -1.0

    def _getrandom(self, retarr):
        tarr = None
        try:
            req = requests.get('http://{}/random/{}'.format(REMOTE_IP,self._len))
            tarr = req.json()
        except ValueError:
            tarr = None
            print("remote random failed")
            #print(req.text)
        except:
            tarr = None
            print("getrandom failed")
        if retarr ==1:
            self._pyarr1 = tarr
        if retarr ==2:
            self._pyarr2 = tarr

    def fullremote(self):
        print("start fullremote")
        ta1 = threading.Thread(target=self._getrandom,args=[1])
        ta2 = threading.Thread(target=self._getrandom,args=[2])
        ta1.start()
        ta2.start()
        ta1.join()
        ta2.join()

        if self._pyarr1 is None or self._pyarr2 is None:
            print("failed to get random from remote, quitting...")
            time.sleep(10)
        else:
            self._dodotprod()

    def _dodotprod(self):
        print(self._pyarr1[:5])
        print(self._pyarr2[:5])
        
        apidata = { "arr1":self._pyarr1,"arr2":self._pyarr2 }
        r_header = {'Content-Type':'application/json'}
        try:
            req = requests.post('http://{}/dotprod'.format(REMOTE_IP), data=json.dumps(apidata), headers=r_header)
            r_json = req.json()
            fval = float(r_json["result"])
            print("full remote:{}".format(fval))
        except requests.ConnectionError:
            print("full remote: connection FAILED!")
        except ValueError:
            print("full remote: JSON error FAILED!")
        except:
            print("full remote: error FAILED!")
        self._pyarr1 = None
        self._pyarr2 = None
           
    def run(self):
        self.fullremote()


def runten():
    threads = []
    for x in range(10):
        calc = calctest(500000)
        threads.append(calc)
        calc.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    while True:
        try:
            runten()
            time.sleep(10)
        except KeyboardInterrupt:
            print("Quitting...")
            break
        except Exception as e:
            print(e)
