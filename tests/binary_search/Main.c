#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "array_wrapper.h"

// Forward declarations

// Forward declarations for all classes
typedef struct BS BS;

// Forward declarations for vtable structs
struct BS_vtable;

// Forward declarations for all methods
int BS_Start(BS* this, int sz);
bool BS_Search(BS* this, int num);
int BS_Div(BS* this, int num);
bool BS_Compare(BS* this, int num1, int num2);
int BS_Print(BS* this);
int BS_Init(BS* this, int sz);
int BS__decaf__init(BS* this);

typedef struct BS {
    ArrayWrapper* number;
    int size;
    struct BS_vtable *vptr;
} BS;

struct BS_vtable {
    int (*Start)(BS*, int);
    bool (*Search)(BS*, int);
    int (*Div)(BS*, int);
    bool (*Compare)(BS*, int, int);
    int (*Print)(BS*);
    int (*Init)(BS*, int);
};

int BS__decaf__init(BS* this) {
    // Initialize vtable
    static struct BS_vtable vtable = {
        .Start = BS_Start,
        .Search = BS_Search,
        .Div = BS_Div,
        .Compare = BS_Compare,
        .Print = BS_Print,
        .Init = BS_Init,
    };
    this->vptr = &vtable;
    return 0;
}

int BS_Start(BS* this, int sz) {
    int aux01;
    int aux02;
    aux01 = this->vptr->Init(this, sz);
    aux02 = this->vptr->Print(this);
    if (this->vptr->Search(this, 8)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 19)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 20)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 21)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 37)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 38)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 39)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    if (this->vptr->Search(this, 50)) {
        printf("%d\n", 1);
    } else {
        printf("%d\n", 0);
    }
    return 999;
}

bool BS_Search(BS* this, int num) {
    bool bs01;
    int right;
    int left;
    bool var_cont;
    int medium;
    int aux01;
    int nt;
    aux01 = 0;
    bs01 = false;
    right = array_length(this->number);
    right = right - 1;
    left = 0;
    var_cont = true;
    while (var_cont) {
        medium = left + right;
        medium = this->vptr->Div(this, medium);
        aux01 = *array_at(this->number, medium);
        if (num < aux01) {
            right = medium - 1;
        } else {
            left = medium + 1;
        }
        if (this->vptr->Compare(this, aux01, num)) {
            var_cont = false;
        } else {
            var_cont = true;
        }
        if (right < left) {
            var_cont = false;
        } else {
            nt = 0;
        }
    }
    if (this->vptr->Compare(this, aux01, num)) {
        bs01 = true;
    } else {
        bs01 = false;
    }
    return bs01;
}

int BS_Div(BS* this, int num) {
    int count01;
    int count02;
    int aux03;
    count01 = 0;
    count02 = 0;
    aux03 = num - 1;
    while (count02 < aux03) {
        count01 = count01 + 1;
        count02 = count02 + 2;
    }
    return count01;
}

bool BS_Compare(BS* this, int num1, int num2) {
    bool retval;
    int aux02;
    retval = false;
    aux02 = num2 + 1;
    if (num1 < num2) {
        retval = false;
    } else {
        if (!(num1 < aux02)) {
            retval = false;
        } else {
            retval = true;
        }
    }
    return retval;
}

int BS_Print(BS* this) {
    int j;
    j = 1;
    while (j < (this->size)) {
        printf("%d\n", *array_at(this->number, j));
        j = j + 1;
    }
    printf("%d\n", 99999);
    return 0;
}

int BS_Init(BS* this, int sz) {
    int j;
    int k;
    int aux02;
    int aux01;
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
    BS* __tempvar1 = (BS*)malloc(sizeof(BS)) ;
    BS__decaf__init(__tempvar1);
    printf("%d\n", __tempvar1->vptr->Start(__tempvar1, 20));
    // free(__tempvar1);
    // __tempvar1 = NULL;
    return 0;
}
