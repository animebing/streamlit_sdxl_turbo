import queue
import threading
import uuid


class TaskQueue:
    def __init__(self, func):
        self.func = func
        self.queue = queue.Queue()
        self.results = {}
        self.thread = threading.Thread(target=self.process)

    def process(self):
        while True:
            item = self.queue.get()
            if item is None:
                break

            task_id = item[0]
            event = item[1]
            result = self.func(*item[2:])
            self.results[task_id] = result
            self.queue.task_done()
            event.set()

    def start(self):
        self.thread.start()
        print(f'thread id: {self.thread.ident}')

    def put(self, *args):
        task_id = str(uuid.uuid4())
        event = threading.Event()
        self.queue.put((task_id, event) + args)

        return task_id, event

    def get(self, task_id):
        return self.results.pop(task_id)
