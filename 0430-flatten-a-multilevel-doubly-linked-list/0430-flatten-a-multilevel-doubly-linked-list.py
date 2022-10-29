"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# Time: O(n); Space: O(n)
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Use a stack to dump remnant list after the node with a child
        st = []
        curr = head # start at the head of the DLL
        # Iterate the DLL till we reach the null node
        while curr:
            # Check if the current node has a child
            if curr.child:
                # Append the remnant after the node with a child
                if curr.next:
                    st.append(curr.next)
                # Update the next & prev pointers at the current node
                curr.next = curr.child
                if curr.next:
                    curr.next.prev = curr
                curr.child = None # nullify the child node
            else:
                # Check if we are at the penultimate node of the child list
                # Then pop from the stack is not empty and insert the remnant
                if curr.next is None and len(st) > 0:
                    # Insert and update the next & prev pointers
                    curr.next = st.pop()
                    if curr.next:
                        curr.next.prev = curr

            curr = curr.next # move the pointer

        return head # return the original head that is modified in-place