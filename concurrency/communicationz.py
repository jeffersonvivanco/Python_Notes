from queue import Queue
from threading import Thread, Event
import time

# Object that signals shutdown
_sentinel = object()


# A thread that produces data
def producer(out_q):
    c = 1
    while c <= 10:
        # produce some data
        data = 'Hello from producer ' + str(c)

        # Make a (data, event) pair and hand it to the consumer
        evt = Event()
        out_q.put((data, evt))

        # Wait for the consumer to process the item
        evt.wait()
        c += 1

    # Put the sentinel on the queue to indicate completion
    out_q.put((_sentinel, None))


# A thread that consumes data
def consumer(in_q):
    while True:
        # consume some data
        data, evt = in_q.get()

        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # process the data
        print(data)

        # Indicate completion
        in_q.task_done()
        time.sleep(.5)
        evt.set()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Wait for all produced items to be consumed
q.join()