#!/usr/bin/python3

""" This module defines class 'Node' and class 'SinglyLinkedList'
an object of Node class with be the node of the singly linked list. """


class Node:
    """ a node that stores an integer and forms a singly-linked-list. """

    def __init__(self, data, next_node=None):
        """ Initializes a node of Node class by data and next_node """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ gets data value """
        return self.__data

    @property
    def next_node(self):
        """ gets next_node value"""

        return self.__next_node

    @data.setter
    def data(self, value):
        """ sets data to value """

        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ sets next_node to value """

        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ a class that defines a singly linked list formed of Nodes"""

    def __init__(self):
        """ Initializes the head of the list. """
        self.head = None

    def sorted_insert(self, value):
        """ Adds a node to the list in its sorted place. """

        if self.head is None:
            self.head = Node(value)
        elif self.head.data > value:
            new_node = Node(value, self.head)
            self.head = new_node
        elif self.head.next_node is None:
            new_node = Node(value)
            self.head.next_node = new_node
        else:
            node = self.head
            while (node):
                if node.next_node is None:
                    new_node = Node(value)
                    node.next_node = new_node
                    break
                elif node.next_node.data > value:
                    new_node = Node(value, node.next_node)
                    node.next_node = new_node
                    break
                else:
                    node = node.next_node

    def __str__(self):
        """ This what makes my linked list printable. """

        node_data = self.head
        str_to_print = ""
        if node_data is None:
            return str_to_print
        while node_data.next_node:
            str_to_print += str(node_data.data) + "\n"
            node_data = node_data.next_node
        str_to_print += str(node_data.data)
        return str_to_print
