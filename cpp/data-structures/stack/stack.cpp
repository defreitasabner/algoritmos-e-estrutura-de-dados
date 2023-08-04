#include "stack.hpp"

Stack::Stack(int maxSize)
{
    length = 0;
    MAX_SIZE = maxSize;
    data = new int[maxSize];
}

Stack::~Stack()
{
    delete [] data;
}

bool Stack::isEmpty() const
{
    return (length == 0);
}

bool Stack::isFull() const
{
    return (length == MAX_SIZE);
}

int Stack::top() const
{
    return data[length - 1];
}

void Stack::push(int item)
{
    if(isFull())
    {
        throw "Stack is full";
    }
    else
    {
        data[length] = item;
        length++;
    }
}

int Stack::pop()
{
    if(isEmpty())
    {
        throw "Stack is empty";
    }
    else
    {
        int copy = top();
        length--;
        return copy;
    }
}