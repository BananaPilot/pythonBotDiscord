from typing import Any
from attr import dataclass


@dataclass
class Queue_bot:

  queue: list[str] = []

  def appendToQueue(self, element: str):
    self.queue.append(element)
    pass

  def popFromQueue(self):
    self.queue.pop()
    pass

  def findAndDelete(self, element: str):
    for url in self.queue:
      if url == element:
        self.queue.remove(url)
    pass

  
  
  pass