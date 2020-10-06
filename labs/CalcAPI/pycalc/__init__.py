from ctypes import *

LIBCALC = cdll.LoadLibrary("bin/libcalc.so")

def dot_prod(arr1, arr2):
    func_dp = LIBCALC.dot_product
    func_dp.restype = c_double
    func_dp.argtypes = [POINTER(c_double),POINTER(c_double),c_int]

    alen = len(arr1)
    arrdoubles = c_double * alen
    carr1 = arrdoubles()
    carr2 = arrdoubles()
    
    for i in range(alen):
    	carr1[i] = float(arr1[i])
    	carr2[i] = float(arr2[i])
    
    resp = func_dp(carr1,carr2,alen)
    return resp

def get_rand_array(size):
    func_getrand = LIBCALC.gen_random_array
    func_getrand.restype = POINTER(c_double)
    func_getrand.argtypes = [c_int]
    func_free = LIBCALC.free_ptr
    func_free.argtypes = [c_void_p]

    temparr = func_getrand(size)
    # have to copy from c pointer
    resp = [float(temparr[i]) for i in range(size)]
    func_free(temparr)
    return resp
