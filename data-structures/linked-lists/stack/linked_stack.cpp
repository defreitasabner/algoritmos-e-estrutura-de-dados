#include "linked_stack.hpp"
#include <cstddef>

LinkedStack::LinkedStack()
{
    head = NULL;
}

LinkedStack::~LinkedStack()
{
    Node* temp;
    while (head != NULL)
    {
        temp = head;
        head = temp->next;
        delete temp;
    }
}

bool LinkedStack::isEmpty() const
{
    return head == NULL;
}

bool LinkedStack::isFull() const
{
    Node* temp;
    temp = new Node;
    delete temp;
    return false;
}

int LinkedStack::top() const
{
    if(head != NULL) return head->data;
}

void LinkedStack::push(char item)
{
    if(!isFull)
    {
        Node* newNode;
        newNode = new Node;
        newNode->data = item;
        newNode->next = head;
        head = newNode;
    }
    else
    {
        throw "Stack is full";
    }
}

int LinkedStack::pop()
{
    if(!isEmpty)
    {
        Node* temp;
        temp = head;
        char removedItem = temp->data;
        head = temp->next;
        delete temp;
        return removedItem;
    }
    else
    {
        throw "Stack is Empty";
    }
}
