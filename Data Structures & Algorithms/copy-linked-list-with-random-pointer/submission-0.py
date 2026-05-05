class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # 1) create all nodes
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 2) wire next/random using the map
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)      # None if cur.next is None
            old_to_new[cur].random = old_to_new.get(cur.random)  # None if cur.random is None
            cur = cur.next

        return old_to_new[head]
