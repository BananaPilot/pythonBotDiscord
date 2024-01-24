from typing import Any
from attr import dataclass
from queue_element import QueueElementType, QueueElement

TrackInfo = dict[str, Any]


@dataclass
class Queue_bot:
    the_queue: list[QueueElementType] = []
    current: QueueElementType = None

    def appendToQueue(self, element: QueueElementType):
        self.the_queue.append(element)
        pass

    def clearCurrent(self):
        self.current = None

    def shiftQueue(self):
        if len(self.the_queue) == 0:
            return None
        
        self.current = self.the_queue.pop(0)
        return self.current

    def length(self):
        return len(self.the_queue)

    def first(self):
        if len(self.the_queue) == 0:
            return None
        
        return self.the_queue[0]
    
    def get_current(self):
        return self.current

    def __str__(self):
        return "\n".join(elem["fulltitle"] for elem in self.the_queue)

    pass
