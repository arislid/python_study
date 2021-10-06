#include <iostream>

using namespace std;

class Hello
{
    private:
        int count = 0;
        char *name = "minji";
    public:
        void printHello(void);
        int countHello();
};

int Hello::countHello()
{
    return count;
}
void Hello::printHello(void)
{
    // make_class.cpp:9:22: warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]
    //      char *name = "minji";
    printf("Hello %s\n", *name);
    // result.... Hello Segmentation fault!!!!!! 
    count++;
}

int main(void)
{
    Hello h;

    h.printHello();
    printf("count number of printHello.... %d\n", h.countHello());
}