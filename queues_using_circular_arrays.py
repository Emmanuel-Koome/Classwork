class CircularArrayQueue:
    default_capacity= 10


    def __init__(self):
        self.data = [None] * CircularArrayQueue.default_capacity
        self.size = 0
        self.front = 0


    def __len__(self):
        return self.size


    def is_empty(self):
        return self.size == 0


    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.data[self.front]


    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        item_to_dequeue = self.data[self.front]

        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)

        self.size -= 1
        return item_to_dequeue


    def enqueue(self, element):
        if self.size == len(self.data):
           self.resize(2 * len(self.data))

        back_of_the_queue = (self.front + self.size) % len(self.data)

        self.data[back_of_the_queue] = element
        self.size += 1


    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity

        current_index = self.front
        for item in range(self.size):
            current_index = (current_index + 1) % len(old_data)
            self.front = 0

class Empty(Exception):
    def __init__(self, message='Queue is empty'):
        self.message= message
        super().__init__(self.message)
if __name__=='__main__':
        queue= CircularArrayQueue()
        print('Queues using circular arrays')
        print(f'The initial queue size is: {len(queue)}')
        print(f'is queue empty? {queue.is_empty()}')

        print("\n Enqueueing our queue")
        elements_to_enqueue= ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']

        for person in elements_to_enqueue:
            queue.enqueue(person)
            print(f"Added {person}. Queue size is now: {len(queue)}")

            print("\n serving people from the front of the queue:")

            for i in range(3):
                served_person= queue.dequeue()
                print(f"Served: {served_person}Queue size is now: {len(queue)}")

                print("\n Adding more people to induce a wrap around in the array")
                more_people= ['Frank', 'Linda', 'Ford']

                for person in more_people:
                  print(f"\nPerson currently at the front: {queue.first()}")
                  print(f"Total people still in queue: {len(queue)}")

                  print(f"\nInternal details:")
                  print(f"Front index: {queue.front}")
                print(f"Array contents: {queue.data}")



