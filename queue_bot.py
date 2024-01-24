from typing import Any
from attr import dataclass
from queue_element import QueueElementType, QueueElement

TrackInfo = dict[str, Any]


@dataclass
class Queue_bot:
    the_queue: list[QueueElementType] = []
    current: QueueElementType = None

    def appendToQueue(self, element: QueueElementType) -> None:
        self.the_queue.append(element)

    def clearCurrent(self) -> None:
        self.current = None

    def shiftQueue(self) -> QueueElementType:
        if self.isQueueEmpty():
            return None

        self.current = self.the_queue.pop(0)
        return self.current

    def length(self) -> int:
        return len(self.the_queue)

    def first(self) -> QueueElementType:
        if len(self.the_queue) == 0:
            return None

        return self.the_queue[0]

    def get_current(self) -> QueueElementType:
        return self.current

    def isQueueEmpty(self) -> bool:
        return len(self.the_queue) == 0

    def isEmpty(self) -> bool:
        return self.get_current() is None and self.isQueueEmpty()

    def __str__(self):
        return "\n".join(f' • {elem["fulltitle"]}' for elem in self.the_queue)

    pass
