/** Multi class scope management. */
class Main {
    public static void main(String[] args) {
        System.out.println(0);
    }
}

class A {

}

class B {
}
// Will log this: 
// SymTableVisitor - ERROR - Error: Class A already declared
class A {

}