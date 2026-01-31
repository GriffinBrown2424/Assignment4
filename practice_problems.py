"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support
removing tasks from the front.
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
        if not self.queue:
            return None
        return self.queue.popleft()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return
the number of unique values seen so far.
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)
