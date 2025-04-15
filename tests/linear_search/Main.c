#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "array_wrapper.h"

// Forward declarations

// Forward declarations for all classes
typedef struct LS LS;

// Forward declarations for vtable structs
struct LS_vtable;

// Forward declarations for all methods
int LS_Start(LS* this, int sz);
int LS_Print(LS* this);
int LS_Search(LS* this, int num);
int LS_Init(LS* this, int sz);
int LS__decaf__init(LS* this);

typedef struct LS {
    ArrayWrapper* number;
    int size;
    struct LS_vtable *vptr;
} LS;

struct LS_vtable {
    int (*Start)(LS*, int);
    int (*Print)(LS*);
    int (*Search)(LS*, int);
    int (*Init)(LS*, int);
};

int LS__decaf__init(LS* this) {
    // Initialize vtable
    static struct LS_vtable vtable = {
        .Start = LS_Start,
        .Print = LS_Print,
        .Search = LS_Search,
        .Init = LS_Init,
    };
    this->vptr = &vtable;
    return 0;
}

int LS_Start(LS* this, int sz) {
    int aux01;
    int aux02;
    aux01 = this->vptr->Init(this, sz);
    aux02 = this->vptr->Print(this);
    printf("%d\n", 9999);
    printf("%d\n", this->vptr->Search(this, 8));
    printf("%d\n", this->vptr->Search(this, 12));
    printf("%d\n", this->vptr->Search(this, 17));
    printf("%d\n", this->vptr->Search(this, 50));
    return 55;
}

int LS_Print(LS* this) {
    int j;
    j = 1;
    while (j < (this->size)) {
        printf("%d\n", *array_at(this->number, j));
        j = j + 1;
    }
    return 0;
}

int LS_Search(LS* this, int num) {
    int j;
    bool ls01;
    int ifound;
    int aux01;
    int aux02;
    int nt;
    j = 1;
    ls01 = false;
    ifound = 0;
    while (j < (this->size)) {
        aux01 = *array_at(this->number, j);
        aux02 = num + 1;
        if (aux01 < num) {
            nt = 0;
        } else {
            if (!(aux01 < aux02)) {
                nt = 0;
            } else {
                ls01 = true;
                ifound = 1;
                j = this->size;
            }
        }
        j = j + 1;
    }
    return ifound;
}

int LS_Init(LS* this, int sz) {
    int j;
    int k;
    int aux01;
    int aux02;
    this->size = sz;
    this->number = create_array(sz);
    j = 1;
    k = this->size + 1;
    while (j < (this->size)) {
        aux01 = 2 * j;
        aux02 = k - 3;
        this->number->data[j] = aux01 + aux02;
        j = j + 1;
        k = k - 1;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    LS* __tempvar1 = (LS*)malloc(sizeof(LS)) ;
    LS__decaf__init(__tempvar1);
    printf("%d\n", __tempvar1->vptr->Start(__tempvar1, 10));
    // free(__tempvar1);
    // __tempvar1 = NULL;
    return 0;
}
