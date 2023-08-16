#include "linked_queue.hpp"
#include <cstdlib>

LinkedQueue::LinkedQueue()
{
    front = NULL;
    rear = NULL;
}

LinkedQueue::~LinkedQueue()
{
    Node* temp;
    while(front != NULL)
    {
        temp = front;
        front = front->next;
        delete temp;
    }
    rear = NULL;
}

bool LinkedQueue::isEmpty() const
{
    return (front == NULL) && (rear == NULL);
}

bool LinkedQueue::isFull() const
{
    Node* location;
    location = new Node;
    delete location;
    return false;
}

void LinkedQueue::enqueue(char item)
{
    if(!isFull)
    {
        Node* newNode;
        newNode = new Node;
        newNode->data = item;
        newNode->next = NULL;
        if(rear == NULL) 
            front = newNode;
        else
            rear->next = newNode;
        rear = newNode;
    }
    else
    {
        throw "Queue is full!";
    }
}

char LinkedQueue::dequeue()
{
    if(!isEmpty)
    {
        Node* temp;
        temp = front;
        char removedItem = front->data;
        front = front->next;
        if(front == NULL)
            rear = NULL;
        delete temp;
        return removedItem;
    }
    else
    {
        throw "Queue is empty!";
    }
}
