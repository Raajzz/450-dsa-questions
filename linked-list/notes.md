If there's a way to get the address of a node of a lined list. One way of finding whether the LinkedList is circular would be to do this.

```python
return_check = -1
while(True):
  if(head_id == id(node)):
    return_check = 1
  if(node.next is None):
    return_check = 0
  node = node.next
```