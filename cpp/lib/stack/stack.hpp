#pragma once

class Stack
{
    private:
        int length;
        int MAX_SIZE;
    public:
        Stack();
        ~Stack();
        bool isEmpty() const;
        bool isFull() const;
        int top() const;
        void push(int item);
        int pop();
};