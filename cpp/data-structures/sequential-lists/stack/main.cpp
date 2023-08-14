#include <iostream>

#include "stack.hpp"

using namespace std;

int main()
{
    int input;
    
    cout << "Pilha" << endl;
    cout << "Insira o tamanho desejado para a pilha:" << endl; 
    cin >> input;
    Stack stack(input);
    while (!stack.isFull())
    {
        cout << "Insira um valor na pilha:" << endl;
        cin >> input;
        stack.push(input);
    }
    cout << "Desempilhando:" << endl;
    while (!stack.isEmpty())
    {
        cout << stack.pop() << endl;
    }
    cout << "Todos elementos removidos da pilha. Finalizando." << endl;

    return 0;
}