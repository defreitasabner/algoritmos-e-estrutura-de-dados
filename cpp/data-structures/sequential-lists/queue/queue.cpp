#include "queue.hpp"

Queue::Queue(int maxSize)
{
    first   = 0;
    last    = 0;
    data    = new int[maxSize];
}

Queue::~Queue()
{
    delete [] data;
}

bool Queue::isEmpty() const
{
    return (first == last);
}

bool Queue::isFull() const
{
    return (first - last == MAX_SIZE);
}
