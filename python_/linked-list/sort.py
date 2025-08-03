from linked_list import LinkedList, Node

list1 = LinkedList()
list2 = LinkedList()

list1.insert_at_last(1)
list1.insert_at_last(2)
list1.insert_at_last(4)

list2.insert_at_last(1)
list2.insert_at_last(3)
list2.insert_at_last(4)

# list1.show_all_items()
# list2.show_all_items()

l3 = Node()
current = l3
list1 = list1.head
list2 = list2.head

while list1 and list2:
    if list1.val <= list2.val:
        current.next = list1
        list1 = list1.next
    else:
        current.next = list2
        list2 = list2.next
    current = current.next

if list1:
    current.next = list1
if list2:
    current.next = list2

if l3:
    print(l3.val)
    while (l3.next):
        print(l3.next.val)
        l3 = l3.next
else:
    print("Empty")
