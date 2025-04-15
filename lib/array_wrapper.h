/**
* ArrayWrapper is a data type as part of the decaf standard library.
* It is responsible for handling array operations for arrays allocated either in the heap
* and in the stack.
*/

#ifndef ARRAY_WRAPPER_H
#define ARRAY_WRAPPER_H

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int size;
} ArrayWrapper;

// Create a new array wrapper
static inline ArrayWrapper* create_array(int size) {
    if (size < 0) {
        printf("Invalid array size\n");
        exit(1);
    }
    
    ArrayWrapper* wrapper = (ArrayWrapper*)malloc(sizeof(ArrayWrapper));
    if (!wrapper) {
        printf("Failed to allocate array wrapper\n");
        exit(1);
    }
    
    wrapper->data = (int*)malloc(size * sizeof(int));
    if (!wrapper->data) {
        free(wrapper);
        printf("Failed to allocate array data\n");
        exit(1);
    }
    
    // Initialize array elements to 0
    for (int i = 0; i < size; i++) {
        wrapper->data[i] = 0;
    }
    
    wrapper->size = size;
    return wrapper;
}

// Get array length
static inline int array_length(ArrayWrapper* arr) {
    if (!arr) {
        printf("Null array reference\n");
        exit(1);
    }
    return arr->size;
}

// Access array element
static inline int* array_at(ArrayWrapper* arr, int index) {
    if (!arr) {
        printf("Null array reference\n");
        exit(1);
    }
    if (index < 0 || index >= arr->size) {
        printf("Array index out of bounds: %d\n", index);
        exit(1);
    }
    return &(arr->data[index]);
}

// Free array wrapper
static inline void free_array(ArrayWrapper* arr) {
    if (arr) {
        if (arr->data) {
            free(arr->data);
        }
        free(arr);
    }
}

#endif // ARRAY_WRAPPER_H