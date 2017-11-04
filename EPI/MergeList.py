class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:

            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next

def main():
    F,L = None,None
    list1 = [2,6,9,18]
    list2 = [3,5,7,10]
    for l1 in reversed(range(len(list1))):
        temp = ListNode(list1[l1], None)
        temp.next = F
        F = temp
    for l2 in reversed(range(len(list1))):
        temp = ListNode(list2[l2], None)
        temp.next = L
        L = temp
    result = merge_two_sorted_lists(F, L)
    while result:
        print(result.data)
        result = result.next

if __name__ == '__main__':
    main()