#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "src/calc.h"

bool runrandom() {
        double* ptarr1 = gen_random_array(10);
        double* ptarr2 = gen_random_array(10);
        for (int i=0; i<10; i++) {
                printf("%f - %f\t", ptarr1[i], ptarr2[i]);
        }
        printf("\r\n");

        double dp = dot_product(ptarr1, ptarr2, 10);
        printf("array result: %f\r\n", dp);
        free(ptarr1);
        free(ptarr2);
}

bool runtest() {
	double tarr1[10];
	double tarr2[10];
	for (int i=0; i<10; i++) {
		tarr1[i] = i + 1;
		tarr2[i] = i + 1;		
		printf("%d\t",i+1);
	}
	printf("\r\n");
	
	double dp = dot_product(tarr1, tarr2, 10);
	bool pass = dp == 385.0;
	printf("array result: %f passed:%s\r\n", dp,pass ? "true" : "false");		
	return pass;
}

int main(void) {
        runrandom();
	if (runtest()) {
		return 0;
	}		
	return 1;
}
