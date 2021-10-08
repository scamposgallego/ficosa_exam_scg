import unittest
import datetime
from FifoList import FifoList


class FifoListTest(unittest.TestCase):
    def test_push(self):
        fifo_list = FifoList()
        for i in range(0, 5):
            fifo_list.push(i)
        self.assertTrue(len(fifo_list.queue) == 5)

    def test_pop(self):
        fifo_list = FifoList()
        for i in range(0, 5):
            fifo_list.push(i)
        fifo_list.pop()
        self.assertTrue(len(fifo_list.queue) == 4)

    def test_size(self):
        fifo_list = FifoList()
        for i in range(0, 5):
            fifo_list.push(i)
        self.assertTrue(fifo_list.size() == 5)

    def test_time(self):
        fifo_list = FifoList()
        times = []
        for i in range(0, 5):
            fifo_list.push(i)
            times.append(fifo_list.queue[i][1])
        for t in times:
            self.assertTrue(type(t) is datetime.datetime)

if __name__ == '__main__':
    unittest.main()
