from linked_list import LinkedList

l = LinkedList()
for val in range(10, 25):
    l.insert_at_last(val)

l.insert(0, 40)

l.show_all_items()
print(l.length)
#print(l.get(0))
#print(l.get(1))
#print(l.get(2))
#print(l.get(7))
#print(l.get(20))
