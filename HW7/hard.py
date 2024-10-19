""" 

1. If a Node has no child cases, then those "missing" values become None signaling an absence of a child value, the parent value will now become None as well. 
2. If a Node has one Child, then the child value that exists will replace the parent node.
3. If the Node has two child cases, then we find the greater value to the right of the subtree and replace the parent value with that child value. We can then delete the child value. 

Edge cases

1. Deletetion can alter the balance of a tree leading to inefficiencies when querying for data within them.


"""