# Decaf

Decaf is a lightweight transpiler that converts a subset of Java—called Mini Java—into C, enabling native binary generation. I built this project from the ground up to deepen my understanding of compiler design, systems programming, and language semantics.

Decaf walks through the full compiler pipeline—lexical analysis, parsing, semantic analysis, and code generation—offering a clear and practical look at how high-level code is transformed into low-level instructions. This project reflects my ability to design robust tooling, write safe and efficient C output, and work with systems-level concerns such as memory layout, type systems, and object-oriented dispatch in a lower-level language.

While all Mini Java programs are valid Java, the reverse isn't true—allowing for focused experimentation and safe compilation boundaries.

## Table of Contents

- [Example Outputs](#example-outputs)
- [Architecture & Implementation](#architecture--implementation)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Useful refrences](#useful-refrences)
- [Contributing](#contributing)
- [License](#license)


## Example Outputs

Here’s a simple factorial program written in Mini Java:


```java
class Fac {
    public int ComputeFac(int num) {
        int num_aux;
        if (num < 1)
            num_aux = 1;
        else
            num_aux = num * (this.ComputeFac(num - 1));
        return num_aux;
    }
}
```

This gets transpiled to the following C code with virtual method table support:



```C
typedef struct Fac Fac;

struct Fac_vtable;

int Fac_ComputeFac(Fac* this, int num);
int Fac__decaf__init(Fac* this);

typedef struct Fac {
    struct Fac_vtable *vptr;
} Fac;

struct Fac_vtable {
    int (*ComputeFac)(Fac*, int);
};

int Fac__decaf__init(Fac* this) {
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
```

You can find more examples [here](https://github.com/Amirali-Amirifar/decaf/tree/main/examples).

## Architecture & Implementation
### Compiler Phases

The compiler is divided into the following phases:

#### Grammar Definition (ANTLR4)
- Custom Mini Java grammar for parsing object-oriented constructs, control structures, array operations, and expressions.

#### Semantic Analysis
- Scoped symbol tables track declarations, variable lifetimes, and basic type information. Includes hierarchical scoping and shadowing.

#### Code Generation
- Uses a visitor pattern to generate C code, simulating Java-style OOP with C structs and vtables. Supports method dispatch, constructors, and control flow.

#### Compilation
- The generated C code can be compiled with gcc to produce efficient native binaries.

### Known Limitations

* Type checking is minimal (future enhancement planned)
* Memory deallocation not yet implemented
* Some false positives in semantic checks

### Key Features
- Mini Java to C transpilation
- Object-oriented constructs (classes, methods, inheritance)
- Virtual method dispatch via vtables
- dynamic and static array allocations 
- Basic type checking and error reporting
- Real-world compiler phases modeled cleanly


## Getting Started

To get started with the Decaf transpiler, follow these steps:

1. Clone the repository:
   ```bash
   # Clone the repo
   git clone https://github.com/Amirali-Amirifar/decaf.git
   cd decaf

   # Set up virtualenv
   python3 -m venv .venv
   source .venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt

   # Run the transpiler
   python3 main.py ./examples/quick_sort/Main.java
   ```
   an executable, a C and assembly output, required lib headers and a view of symbol table as json will be emitted in the target directory.

## Useful Refrences 
- [MiniJava Language Reference Manual](https://www.cs.tufts.edu/~sguyer/classes/comp181-2006/minijava.html)
- [Virtual Method Table](https://en.wikipedia.org/wiki/Virtual_method_table)
## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
