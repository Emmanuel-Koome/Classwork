from queue import Queue

class PalindromeChecker:
    def __init__(self):
        self.stack = []           # LIFO stack using list
        self.queue = Queue()      # FIFO queue using queue.Queue

    def push(self, data):
        self.stack.append(data)

    def enqueue(self, data):
        self.queue.put(data)        # Enqueue to the queue

    def pop(self):
        return self.stack.pop()   # Pop from stack

    def dequeue(self):
        return self.queue.get()   # Dequeue from queue

if __name__ == "__main__":
    # Read input
    s = input("Input a word: ").strip()
    checker = PalindromeChecker()

    # Fill stack and queue
    for data in s:
        checker.push(data)
        checker.enqueue(data)

    # Check for palindrome
    is_palindrome = True
    for i in range(len(s) // 2):
        if checker.pop() != checker.dequeue():
            is_palindrome = False
            break

    # Print result
    if is_palindrome:
        print(f"The word, {s}, is a palindrome.")
    else:
        print(f"The word, {s}, is not a palindrome.")