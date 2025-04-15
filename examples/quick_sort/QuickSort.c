#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "array_wrapper.h"

// Forward declarations

// Forward declarations for all classes
typedef struct QS QS;

// Forward declarations for vtable structs
struct QS_vtable;

// Forward declarations for all methods
int QS_Start(QS* this, int sz);
int QS_Sort(QS* this, int left, int right);
int QS_Print(QS* this);
int QS_Init(QS* this, int sz);
int QS__decaf__init(QS* this);

typedef struct QS {
    ArrayWrapper* number;
    int size;
    struct QS_vtable *vptr;
} QS;

struct QS_vtable {
    int (*Start)(QS*, int);
    int (*Sort)(QS*, int, int);
    int (*Print)(QS*);
    int (*Init)(QS*, int);
};

int QS__decaf__init(QS* this) {
    // Initialize vtable
    static struct QS_vtable vtable = {
        .Start = QS_Start,
        .Sort = QS_Sort,
        .Print = QS_Print,
        .Init = QS_Init,
    };
    this->vptr = &vtable;
    return 0;
}

int QS_Start(QS* this, int sz) {
    int aux01;
    aux01 = this->vptr->Init(this, sz);
    aux01 = this->vptr->Print(this);
    printf("%d\n", 9999);
    aux01 = this->size - 1;
    aux01 = this->vptr->Sort(this, 0, aux01);
    aux01 = this->vptr->Print(this);
    return 0;
}

int QS_Sort(QS* this, int left, int right) {
    int v;
    int i;
    int j;
    int nt;
    int t;
    bool cont01;
    bool cont02;
    int aux03;
    t = 0;
    if (left < right) {
        v = *array_at(this->number, right);
        i = left - 1;
        j = right;
        cont01 = true;
        while (cont01) {
            cont02 = true;
            while (cont02) {
                i = i + 1;
                aux03 = *array_at(this->number, i);
                if (!(aux03 < v)) {
                    cont02 = false;
                } else {
                    cont02 = true;
                }
            }
            cont02 = true;
            while (cont02) {
                j = j - 1;
                aux03 = *array_at(this->number, j);
                if (!(v < aux03)) {
                    cont02 = false;
                } else {
                    cont02 = true;
                }
            }
            t = *array_at(this->number, i);
            this->number->data[i] = *array_at(this->number, j);
            this->number->data[j] = t;
            if (j < (i + 1)) {
                cont01 = false;
            } else {
                cont01 = true;
            }
        }
        this->number->data[j] = *array_at(this->number, i);
        this->number->data[i] = *array_at(this->number, right);
        this->number->data[right] = t;
        nt = this->vptr->Sort(this, left, i - 1);
        nt = this->vptr->Sort(this, i + 1, right);
    } else {
        nt = 0;
    }
    return 0;
}

int QS_Print(QS* this) {
    int j;
    j = 0;
    while (j < (this->size)) {
        printf("%d\n", *array_at(this->number, j));
        j = j + 1;
    }
    return 0;
}

int QS_Init(QS* this, int sz) {
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
    QS* __tempvar1 = (QS*)malloc(sizeof(QS)) ;
    QS__decaf__init(__tempvar1);
    printf("%d\n", __tempvar1->vptr->Start(__tempvar1, 10));
    // free(__tempvar1);
    // __tempvar1 = NULL;
    return 0;
}
