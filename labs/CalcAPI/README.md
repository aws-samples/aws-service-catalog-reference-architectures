# Simple math C python API

This is for demo purposes to see how a program can be packaged and moved between lambda,
docker, kubernetes, etc...

## Build and Run

The makefile will compile the library and run the tests.  
```make all```  

To package for lambda:  
```make lambda```  

To install and run the flask api locally:  
```make local``` 


## Testing  
```./calctest``` C program that will test the libcalc library
```./pytest.py``` python program that will test the python wrapper and the libcalc library
```./testapi.sh``` will call the local API and run tests  

