
const double RANGE_MAX = 5000000.0;

// free a pointer
void free_ptr(void* ptr);

// call once to set the seed
void set_rand_seed();

// calculate the dot product of two arrays
double dot_product(double *arr1, double *arr2, int size);

// generate an array of random doubles 
double* gen_random_array(int size);
