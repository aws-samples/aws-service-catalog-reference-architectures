#! /usr/bin/python

from pycalc import dot_prod
	
if __name__ == "__main__":
    pyarr = [float(x) for x in range(1,11)]
    rval = dot_prod(pyarr,pyarr)
    print("{} passed:{}".format(rval, rval==385.0))



