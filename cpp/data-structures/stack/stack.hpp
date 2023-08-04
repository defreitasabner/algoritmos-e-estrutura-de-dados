#pragma once

class Stack
{
    private:
        int length;
        int MAX_SIZE;
        int* data;
    public:
        Stack(int maxSize);
        ~Stack();
        bool isEmpty() const;
        bool isFull() const;
        int top() const;
        void push(int item);
        int pop();
};