#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "array_wrapper.h"

// Forward declarations

// Forward declarations for all classes
typedef struct Element Element;
typedef struct List List;
typedef struct LL LL;

// Forward declarations for vtable structs
struct Element_vtable;
struct List_vtable;
struct LL_vtable;

// Forward declarations for all methods
bool Element_Init(Element* this, int v_Age, int v_Salary, bool v_Married);
int Element_GetAge(Element* this);
int Element_GetSalary(Element* this);
bool Element_GetMarried(Element* this);
bool Element_Equal(Element* this, Element* other);
bool Element_Compare(Element* this, int num1, int num2);
int Element__decaf__init(Element* this);
bool List_Init(List* this);
bool List_InitNew(List* this, Element* v_elem, List* v_next, bool v_end);
List* List_Insert(List* this, Element* new_elem);
bool List_SetNext(List* this, List* v_next);
List* List_Delete(List* this, Element* e);
int List_Search(List* this, Element* e);
bool List_GetEnd(List* this);
Element* List_GetElem(List* this);
List* List_GetNext(List* this);
bool List_Print(List* this);
int List__decaf__init(List* this);
int LL_Start(LL* this);
int LL__decaf__init(LL* this);

typedef struct Element {
    int Salary;
    bool Married;
    struct Element_vtable *vptr;
} Element;

typedef struct List {
    Element* elem;
    List* next;
    bool end;
    struct List_vtable *vptr;
} List;

typedef struct LL {
    struct LL_vtable *vptr;
} LL;

struct Element_vtable {
    bool (*Init)(Element*, int, int, bool);
    int (*GetAge)(Element*);
    int (*GetSalary)(Element*);
    bool (*GetMarried)(Element*);
    bool (*Equal)(Element*, Element*);
    bool (*Compare)(Element*, int, int);
};

struct List_vtable {
    bool (*Init)(List*);
    bool (*InitNew)(List*, Element*, List*, bool);
    List* (*Insert)(List*, Element*);
    bool (*SetNext)(List*, List*);
    List* (*Delete)(List*, Element*);
    int (*Search)(List*, Element*);
    bool (*GetEnd)(List*);
    Element* (*GetElem)(List*);
    List* (*GetNext)(List*);
    bool (*Print)(List*);
};

struct LL_vtable {
    int (*Start)(LL*);
};

int Element__decaf__init(Element* this) {
    // Initialize vtable
    static struct Element_vtable vtable = {
        .Init = Element_Init,
        .GetAge = Element_GetAge,
        .GetSalary = Element_GetSalary,
        .GetMarried = Element_GetMarried,
        .Equal = Element_Equal,
        .Compare = Element_Compare,
    };
    this->vptr = &vtable;
    return 0;
}

bool Element_Init(Element* this, int v_Age, int v_Salary, bool v_Married) {
    Age = v_Age;
    this->Salary = v_Salary;
    this->Married = v_Married;
    return true;
}

int Element_GetAge(Element* this) {
    return Age;
}

int Element_GetSalary(Element* this) {
    return this->Salary;
}

bool Element_GetMarried(Element* this) {
    return this->Married;
}

bool Element_Equal(Element* this, Element* other) {
    bool ret_val;
    int aux01;
    int aux02;
    int nt;
    ret_val = true;
    aux01 = other->vptr->GetAge(other);
    if (!this->vptr->Compare(this, aux01, Age)) {
        ret_val = false;
    } else {
        aux02 = other->vptr->GetSalary(other);
        if (!this->vptr->Compare(this, aux02, this->Salary)) {
            ret_val = false;
        } else {
            if (this->Married) {
                if (!other->vptr->GetMarried(other)) {
                    ret_val = false;
                } else {
                    nt = 0;
                }
            } else {
                if (other->vptr->GetMarried(other)) {
                    ret_val = false;
                } else {
                    nt = 0;
                }
            }
        }
    }
    return ret_val;
}

bool Element_Compare(Element* this, int num1, int num2) {
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

int List__decaf__init(List* this) {
    // Initialize vtable
    static struct List_vtable vtable = {
        .Init = List_Init,
        .InitNew = List_InitNew,
        .Insert = List_Insert,
        .SetNext = List_SetNext,
        .Delete = List_Delete,
        .Search = List_Search,
        .GetEnd = List_GetEnd,
        .GetElem = List_GetElem,
        .GetNext = List_GetNext,
        .Print = List_Print,
    };
    this->vptr = &vtable;
    return 0;
}

bool List_Init(List* this) {
    this->end = true;
    return true;
}

bool List_InitNew(List* this, Element* v_elem, List* v_next, bool v_end) {
    this->end = v_end;
    this->elem = v_elem;
    this->next = v_next;
    return true;
}

List* List_Insert(List* this, Element* new_elem) {
    bool ret_val;
    List* aux03;
    List* aux02;
    aux03 = this;
    List* __tempvar1 = (List*)malloc(sizeof(List)) ;
    List__decaf__init(__tempvar1);
    aux02 = __tempvar1;
    ret_val = aux02->vptr->InitNew(aux02, new_elem, aux03, false);
    return aux02;
}

bool List_SetNext(List* this, List* v_next) {
    this->next = v_next;
    return true;
}

List* List_Delete(List* this, Element* e) {
    List* my_head;
    bool ret_val;
    bool aux05;
    List* aux01;
    List* prev;
    bool var_end;
    Element* var_elem;
    int aux04;
    int nt;
    my_head = this;
    ret_val = false;
    aux04 = -1;
    aux01 = this;
    prev = this;
    var_end = this->end;
    var_elem = this->elem;
    while ((!var_end) && (!ret_val)) {
        if (e->vptr->Equal(e, var_elem)) {
            ret_val = true;
            if (aux04 < 0) {
                my_head = aux01->vptr->GetNext(aux01);
            } else {
                printf("%d\n", -555);
                aux05 = prev->vptr->SetNext(prev, aux01->vptr->GetNext(aux01));
                printf("%d\n", -555);
            }
        } else {
            nt = 0;
        }
        if (!ret_val) {
            prev = aux01;
            aux01 = aux01->vptr->GetNext(aux01);
            var_end = aux01->vptr->GetEnd(aux01);
            var_elem = aux01->vptr->GetElem(aux01);
            aux04 = 1;
        } else {
            nt = 0;
        }
    }
    return my_head;
}

int List_Search(List* this, Element* e) {
    int int_ret_val;
    List* aux01;
    Element* var_elem;
    bool var_end;
    int nt;
    int_ret_val = 0;
    aux01 = this;
    var_end = this->end;
    var_elem = this->elem;
    while (!var_end) {
        if (e->vptr->Equal(e, var_elem)) {
            int_ret_val = 1;
        } else {
            nt = 0;
        }
        aux01 = aux01->vptr->GetNext(aux01);
        var_end = aux01->vptr->GetEnd(aux01);
        var_elem = aux01->vptr->GetElem(aux01);
    }
    return int_ret_val;
}

bool List_GetEnd(List* this) {
    return this->end;
}

Element* List_GetElem(List* this) {
    return this->elem;
}

List* List_GetNext(List* this) {
    return this->next;
}

bool List_Print(List* this) {
    List* aux01;
    bool var_end;
    Element* var_elem;
    aux01 = this;
    var_end = this->end;
    var_elem = this->elem;
    while (!var_end) {
        printf("%d\n", var_elem->vptr->GetAge(var_elem));
        aux01 = aux01->vptr->GetNext(aux01);
        var_end = aux01->vptr->GetEnd(aux01);
        var_elem = aux01->vptr->GetElem(aux01);
    }
    return true;
}

int LL__decaf__init(LL* this) {
    // Initialize vtable
    static struct LL_vtable vtable = {
        .Start = LL_Start,
    };
    this->vptr = &vtable;
    return 0;
}

int LL_Start(LL* this) {
    List* head;
    List* last_elem;
    bool aux01;
    Element* el01;
    Element* el02;
    Element* el03;
    List* __tempvar2 = (List*)malloc(sizeof(List)) ;
    List__decaf__init(__tempvar2);
    last_elem = __tempvar2;
    aux01 = last_elem->vptr->Init(last_elem);
    head = last_elem;
    aux01 = head->vptr->Init(head);
    aux01 = head->vptr->Print(head);
    Element* __tempvar3 = (Element*)malloc(sizeof(Element)) ;
    Element__decaf__init(__tempvar3);
    el01 = __tempvar3;
    aux01 = el01->vptr->Init(el01, 25, 37000, false);
    head = head->vptr->Insert(head, el01);
    aux01 = head->vptr->Print(head);
    printf("%d\n", 10000000);
    Element* __tempvar4 = (Element*)malloc(sizeof(Element)) ;
    Element__decaf__init(__tempvar4);
    el01 = __tempvar4;
    aux01 = el01->vptr->Init(el01, 39, 42000, true);
    el02 = el01;
    head = head->vptr->Insert(head, el01);
    aux01 = head->vptr->Print(head);
    printf("%d\n", 10000000);
    Element* __tempvar5 = (Element*)malloc(sizeof(Element)) ;
    Element__decaf__init(__tempvar5);
    el01 = __tempvar5;
    aux01 = el01->vptr->Init(el01, 22, 34000, false);
    head = head->vptr->Insert(head, el01);
    aux01 = head->vptr->Print(head);
    Element* __tempvar6 = (Element*)malloc(sizeof(Element)) ;
    Element__decaf__init(__tempvar6);
    el03 = __tempvar6;
    aux01 = el03->vptr->Init(el03, 27, 34000, false);
    printf("%d\n", head->vptr->Search(head, el02));
    printf("%d\n", head->vptr->Search(head, el03));
    printf("%d\n", 10000000);
    Element* __tempvar7 = (Element*)malloc(sizeof(Element)) ;
    Element__decaf__init(__tempvar7);
    el01 = __tempvar7;
    aux01 = el01->vptr->Init(el01, 28, 35000, false);
    head = head->vptr->Insert(head, el01);
    aux01 = head->vptr->Print(head);
    printf("%d\n", 2220000);
    head = head->vptr->Delete(head, el02);
    aux01 = head->vptr->Print(head);
    printf("%d\n", 33300000);
    head = head->vptr->Delete(head, el01);
    aux01 = head->vptr->Print(head);
    printf("%d\n", 44440000);
    return 0;
}

int main(int argc, char *argv[]) {
    LL* __tempvar8 = (LL*)malloc(sizeof(LL)) ;
    LL__decaf__init(__tempvar8);
    printf("%d\n", __tempvar8->vptr->Start(__tempvar8));
    // free(__tempvar1);
    // __tempvar1 = NULL;
    // free(__tempvar2);
    // __tempvar2 = NULL;
    // free(__tempvar3);
    // __tempvar3 = NULL;
    // free(__tempvar4);
    // __tempvar4 = NULL;
    // free(__tempvar5);
    // __tempvar5 = NULL;
    // free(__tempvar6);
    // __tempvar6 = NULL;
    // free(__tempvar7);
    // __tempvar7 = NULL;
    // free(__tempvar8);
    // __tempvar8 = NULL;
    return 0;
}
