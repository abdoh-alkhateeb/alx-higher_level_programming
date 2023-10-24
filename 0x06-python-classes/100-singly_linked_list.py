#!/usr/bin/python3
"""Module that defines Node and SinglyLinkedList"""


class Node:
    """Class that represents Node"""
    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data attribute, with data type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node attribute, with data type validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that represents SLL"""
    def __init__(self):
        """Initialize a SinglyLinkedList with a head that's initially None."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in list."""
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list for printing."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
