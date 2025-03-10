from node import Node
from linked_list import LinkedList

my_linked_list = LinkedList()

my_linked_list.insert_node(5)
my_linked_list.insert_node(1)
my_linked_list.insert_node(3)
my_linked_list.insert_node(15)

my_linked_list.print_items_reversed()

"""my_linked_list.print_items()
print(f"count: {my_linked_list.count_nodes()}")

print(my_linked_list.delete_node(15))
print(my_linked_list.head.value)
print(my_linked_list.head.next.value)
print(my_linked_list.head.next.next.value)
my_linked_list.print_list_items()
print(f"count after: {my_linked_list.count_nodes()}")"""

