class Queue
{
    private:
        int first;
        int last;
        int MAX_SIZE;
        int* data;
    public:
        Queue(int maxSize);
        ~Queue();
        bool isEmpty() const;
        bool isFull() const;
        void enqueue(int item);
        int dequeue();
};