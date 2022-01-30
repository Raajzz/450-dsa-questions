# CAN WE REVERSE A LINKED LIST IN LESS THAT O(N)?

A. 
- No, reversing a singly linked list in particular is not posssible in any time less than O(N), as we need to reach the last node atleast to either reverse iteratively or recursively.
- However a memory efficient doubly linked list with head and tail pointers can be reversed by swapping the head and tail pointers with O(1).
- But you really can't reverse a double linked list in O(1) because we have to exchange the pointers of each and every element so, it takes us O(N) atleast.