#include <iostream>
#include <string>

using namespace std;

class Hello
{
    private:
        int count = 0;
        const char *name1 = "minji";
        string name = "minji";
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
    //       char *name = "minji"; (x)
    // const char *name = "minji"; (o)
    cout << "Hello " << name1 << endl;
    count++;
    cout << "string type " << name << endl;
    count++;
    // printf("Hello %s\n", name);
    // result.... Hello Segmentation fault!!!!!! 
    
}

int main(void)
{
    Hello h;

    h.printHello();
    printf("count number of printHello.... %d\n", h.countHello());
}