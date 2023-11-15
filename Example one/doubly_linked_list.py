from __future__ import annotations
from typing import TypeVar, Generic
from node import Node

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def append(self, data: T):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.size += 1

    # Tuve que modificar la forma en la que se recorria la estructura
    def transversal(self) -> str:
        result = ''
        if self.is_empty() is False:
            current = self.head
            polynomial_grade = self.size - 1
            while current is not self.tail:

                signe = '+' if current.data > 0 else ''
                result += str(current.data) + f'x^{polynomial_grade} '
                current = current.next
                polynomial_grade -= 1

            signe = '+' if self.tail.data > 0 else ''
            result += signe + str(self.tail.data)
        return result

    # Cree un nuevo transversal para la evaluación de los polinomios

    def evaluate_transversal(self, evaluate_number) -> str:
        result = ''
        self.evaluate_number = evaluate_number

        if self.is_empty() is False:
            current = self.head
            polynomial_grade = self.size - 1
            while current is not self.tail:
                signe = '+' if current.data > 0 else ''
                result += str(current.data) + f'({self.evaluate_number})^{polynomial_grade} '
                current = current.next
                polynomial_grade -= 1

            signe = '+' if self.tail.data > 0 else ''
            result += signe + str(self.tail.data)
        return result

    def reverse_transversal(self) -> str:
        current = self.tail
        result = ''

        while current is not None:
            result += str(current.data)
            if current is not self.head:
                result += '->'

            current = current.prev

        return result

    def prepend(self, data: T):
        new_node = Node(data)

        if self.is_empty():
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node
        self.size += 1

    def find_at(self, pos: int) -> Node:
        current_pos = 0
        ref = self.head

        while ref is not None:
            if current_pos == pos:
                return ref

            else:
                ref = ref.next
                current_pos += 1

        raise Exception('No existe la posicion')

    def insert_at_prev(self, pos: int, data: T):

        if self.is_empty():
            self.prepend(data)

        elif pos == 0:
            self.prepend(data)

        elif pos == self.size:
            self.insert_at_post(self.size - 2, data)

        else:
            self.insert_at_post(pos - 1, data)

    def insert_at_post(self, pos: int, data: T):

        if self.is_empty() and pos == 0:
            self.append(data)

        elif pos == self.size - 1:
            self.append(data)

        else:
            ref = self.find_at(pos)
            new_node = Node(data)
            new_node.next = ref.next
            new_node.prev = ref
            if ref.next is not None:
                ref.next.prev = new_node
            ref.next = new_node
            self.size += 1

    def unshift(self) -> Node:

        if self.is_empty():
            raise Exception('La lista esta vacia')

        elif self.head is self.tail:
            ref = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return ref

        else:
            ref = self.head
            self.head = ref.next
            ref.next = None
            self.head.prev = None
            self.size -= 1
            return ref

    # Modifique que el pop nos devolviera un T y no un Node
    def pop(self) -> T:
        if self.is_empty():
            raise Exception('La lista está vacia')

        elif self.size == 1:
            ref = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
            return ref.data

        else:
            ref = self.tail
            self.tail = ref.prev
            self.tail.next = None
            ref.prev = None
            self.size -= 1
            return ref.data

    def remove_at(self, pos: int) -> Node:

        if self.is_empty():
            raise Exception('La lista está vacia')

        elif pos == 0:
            self.unshift()

        elif pos == self.size-1:
            self.pop()

        elif self.head is self.tail:
            ref = self.tail
            self.head = None
            self.tail = None
            self.size = 0
            return ref
        else:
            ref = self.find_at(pos)
            anterior = ref.prev
            siguiente = ref.next
            ref.prev = None
            ref.next = None
            anterior.next = siguiente
            siguiente.prev = anterior
            self.size -= 1
            return ref