#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "array_wrapper.h"

// Forward declarations

// Forward declarations for all classes
typedef struct Fac Fac;

// Forward declarations for vtable structs
struct Fac_vtable;

// Forward declarations for all methods
int Fac_ComputeFac(Fac* this, int num);
int Fac__decaf__init(Fac* this);

typedef struct Fac {
    struct Fac_vtable *vptr;
} Fac;

struct Fac_vtable {
    int (*ComputeFac)(Fac*, int);
};

int Fac__decaf__init(Fac* this) {
    // Initialize vtable
    static struct Fac_vtable vtable = {
        .ComputeFac = Fac_ComputeFac,
    };
    this->vptr = &vtable;
    return 0;
}

int Fac_ComputeFac(Fac* this, int num) {
    int num_aux;
    if (num < 1) {
        num_aux = 1;
    } else {
        num_aux = num * (this->vptr->ComputeFac(this, num - 1));
    }
    return num_aux;
}

int main(int argc, char *argv[]) {
    Fac* __tempvar1 = (Fac*)malloc(sizeof(Fac)) ;
    Fac__decaf__init(__tempvar1);
    printf("%d\n", __tempvar1->vptr->ComputeFac(__tempvar1, 5));
    // free(__tempvar1);
    // __tempvar1 = NULL;
    return 0;
}
