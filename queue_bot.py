from typing import Any
from attr import dataclass
from queue_element import QueueElementType, QueueElement

TrackInfo = dict[str, Any]


@dataclass
class Queue_bot:
    the_queue: list[QueueElementType] = []

    def appendToQueue(self, element: QueueElementType):
        self.the_queue.append(element)
        pass

    def popFromQueue(self):
        if len(self.the_queue) == 0:
            return None

        return self.the_queue.pop(0)

    def length(self):
        return len(self.the_queue)

    def first(self):
        if len(self.the_queue) == 0:
            return None
        
        return self.the_queue[0]

    def __str__(self):
        return "\n".join(elem["fulltitle"] for elem in self.the_queue)

    pass
