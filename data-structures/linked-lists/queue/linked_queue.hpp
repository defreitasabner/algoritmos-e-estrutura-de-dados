#pragma once
#include "node.hpp"

class LinkedQueue
{
    private:
        Node* front;
        Node* rear;
    public:
        LinkedQueue();
        ~LinkedQueue();
        bool isEmpty() const;
        bool isFull() const;
        void enqueue(char item);
        char dequeue();
};