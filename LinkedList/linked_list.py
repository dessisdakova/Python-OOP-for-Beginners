from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        """Create a new node and insert it as the head of the linked list"""
        new_node = Node(value)

        if self.head is None:  # if no head, the node becomes head
            self.head = new_node
        elif value <= self.head.value:  # Ascending order
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
             # create the pointers
            new_node.next = runner
            previous.next = new_node

    def print_items(self):
        if self.head is None:
            print("Empty")
        else:
            runner = self.head

            while runner is not None:
                print(f"{runner.value}", end=" ")
                runner = runner.next
            print()

    def count_nodes(self) -> int:
        count = 0
        runner = self.head

        while runner is not None:
            count += 1
            runner = runner.next
        return count

    def find_node(self, target_value) -> bool:
        runner = self.head

        while runner is not None:
            if runner.value == target_value:
                return  True
            else:
                runner = runner.next

        return False

    def delete_node(self, target_value) -> bool:
        if self.head is None:
            return False
        elif target_value == self.head.value:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (target_value != runner.value):
                previous = runner
                runner = runner.next

            if runner is None:
                return False
            else:
                previous.next = runner.next
                return True

    def print_items_reversed(self):
        self._print_reverse(self.head)

    def _print_reverse(self, node):
        if node is None:
            return
        self._print_reverse(node.next)
        print(node.value, end=" ")

