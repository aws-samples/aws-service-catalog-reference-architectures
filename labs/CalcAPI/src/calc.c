#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "calc.h"

static double RAND_DIVISOR, RANGE_MIN;
static int bool_is_seeded = 0;

void set_rand_seed() {
        if (bool_is_seeded == 0) {
            time_t t;
            srand(time(&t));
            bool_is_seeded = 1; 
            RANGE_MIN = RANGE_MAX * -1;
            double range = RANGE_MAX - RANGE_MIN;
            RAND_DIVISOR = RAND_MAX / range;
            printf("div=%f\r\n",RAND_DIVISOR);
        }
}

// calculate the dot product of two arrays
double dot_product(double *arr1, double *arr2, int size) {
	double res = 0;
	for (int i =0; i < size; i++) {
		double v = arr1[i];	
		double u = arr2[i];	
		double prod = 0;
		if (v != 0 && u != 0) {
			prod = v * u;
		}
		res += prod;
		//printf("%f * %f = %f\t%f\r\n",v,u, prod, res);
	}
	return res;
}

void free_ptr(void* ptr) {
        free(ptr);
}

double* gen_random_array(int size) {
        set_rand_seed();
	double* rarr = (double*)malloc(sizeof(double)*size);
	for (int i =0; i < size; i++) {
		double rd = RANGE_MIN + (rand()/RAND_DIVISOR);
		rarr[i] = rd;
	}	
	return rarr;
}

