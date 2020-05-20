#!/usr/bin/python3
"""a class Node that defines a node of a singly linked list
"""


class Node:
    """a class Node that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Instantiation

        Arguments:
            data {int} -- number to be inputed in node
            next_node {node} -- next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrives the data fo the noe

        Returns:
            int -- returns the data in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """sets new value to the data

        Arguments:
            value {int} -- new value for data

        Raises:
            TypeError: Raises if value is not int type
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next node to be added

        Returns:
            Node -- next node to be added
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class of SinglyLinkedList
    """
    def __init__(self):
        """Instantiation
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserts a sorted linked list

        Arguments:
            value {int} -- value to be inputted to node
        """
        if self.__head is None:
            self.__head = Node(value, self.__head)
            return
        new = Node(value, self.__head)
        self.__head = new

    def __str__(self):
        ls = []
        tmp = self.__head
        while tmp is not None:
            ls.append(tmp.data)
            tmp = tmp.next_node
        ls.sort()
        return '\n'.join(str(i) for i in ls)
