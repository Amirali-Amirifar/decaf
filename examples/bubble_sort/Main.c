#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "array_wrapper.h"

// Forward declarations

// Forward declarations for all classes
typedef struct BBS BBS;

// Forward declarations for vtable structs
struct BBS_vtable;

// Forward declarations for all methods
int BBS_Start(BBS* this, int sz);
int BBS_Sort(BBS* this);
int BBS_Print(BBS* this);
int BBS_Init(BBS* this, int sz);
int BBS__decaf__init(BBS* this);

typedef struct BBS {
    ArrayWrapper* number;
    int size;
    struct BBS_vtable *vptr;
} BBS;

struct BBS_vtable {
    int (*Start)(BBS*, int);
    int (*Sort)(BBS*);
    int (*Print)(BBS*);
    int (*Init)(BBS*, int);
};

int BBS__decaf__init(BBS* this) {
    // Initialize vtable
    static struct BBS_vtable vtable = {
        .Start = BBS_Start,
        .Sort = BBS_Sort,
        .Print = BBS_Print,
        .Init = BBS_Init,
    };
    this->vptr = &vtable;
    return 0;
}

int BBS_Start(BBS* this, int sz) {
    int aux01;
    aux01 = this->vptr->Init(this, sz);
    aux01 = this->vptr->Print(this);
    printf("%d\n", 99999);
    aux01 = this->vptr->Sort(this);
    aux01 = this->vptr->Print(this);
    return 0;
}

int BBS_Sort(BBS* this) {
    int nt;
    int i;
    int aux02;
    int aux04;
    int aux05;
    int aux06;
    int aux07;
    int j;
    int t;
    i = this->size - 1;
    aux02 = -1;
    while (aux02 < i) {
        j = 1;
        while (j < (i + 1)) {
            aux07 = j - 1;
            aux04 = *array_at(this->number, aux07);
            aux05 = *array_at(this->number, j);
            if (aux05 < aux04) {
                aux06 = j - 1;
                t = *array_at(this->number, aux06);
                this->number->data[aux06] = *array_at(this->number, j);
                this->number->data[j] = t;
            } else {
                nt = 0;
            }
            j = j + 1;
        }
        i = i - 1;
    }
    return 0;
}

int BBS_Print(BBS* this) {
    int j;
    j = 0;
    while (j < (this->size)) {
        printf("%d\n", *array_at(this->number, j));
        j = j + 1;
    }
    return 0;
}

int BBS_Init(BBS* this, int sz) {
    this->size = sz;
    this->number = create_array(sz);
    this->number->data[0] = 20;
    this->number->data[1] = 7;
    this->number->data[2] = 12;
    this->number->data[3] = 18;
    this->number->data[4] = 2;
    this->number->data[5] = 11;
    this->number->data[6] = 6;
    this->number->data[7] = 9;
    this->number->data[8] = 19;
    this->number->data[9] = 5;
    return 0;
}

int main(int argc, char *argv[]) {
    BBS* __tempvar1 = (BBS*)malloc(sizeof(BBS)) ;
    BBS__decaf__init(__tempvar1);
    printf("%d\n", __tempvar1->vptr->Start(__tempvar1, 10));
    // free(__tempvar1);
    // __tempvar1 = NULL;
    return 0;
}
