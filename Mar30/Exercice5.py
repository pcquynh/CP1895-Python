from dataStructure import Queue


def stutter(number_queue):
    for i in range(number_queue.size()):
        num = number_queue.dequeue()
        number_queue.enqueue(num)
        number_queue.enqueue(num)

def main():
    number_queue = Queue()
    number_queue.enqueue(1)
    number_queue.enqueue(2)
    number_queue.enqueue(3)
    stutter(number_queue)

    print(number_queue)

if __name__ == '__main__':
    main()