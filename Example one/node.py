from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data: T = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None