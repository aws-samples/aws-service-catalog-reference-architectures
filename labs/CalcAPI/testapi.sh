#!/bin/bash

curl http://localhost:8080/random/10
curl http://localhost:8080/dotprodtest
curl -H "Content-Type: application/json" -X POST -d '{"arr1":[1,2,3,4,5,6,7,8,9,10],"arr2":[1,2,3,4,5,6,7,8,9,10]}' http://localhost:8080/dotprod
