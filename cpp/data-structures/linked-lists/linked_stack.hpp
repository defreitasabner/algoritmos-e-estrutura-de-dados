#pragma once
#include "node.hpp"

class LinkedStack
{
    private:
        Node* head;
    public:
        LinkedStack();
        ~LinkedStack();
        bool isEmpty() const;
        bool isFull() const;
        int top() const;
        void push(char item);
        int pop();
};