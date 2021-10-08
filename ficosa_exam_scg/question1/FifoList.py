from datetime import datetime as dt


class FifoList:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append((item, dt.now()))

    def pop(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def times(self):
        for i in self.queue:
            print(
                "Element: {}\n"
                "Time: {}\n".format(i[0], i[1])
            )
        return "Done"