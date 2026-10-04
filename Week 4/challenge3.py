class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def build_list(values):
    head = None

    for v in reversed(values):
        head = Node(v, head)

    return head


def to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


#tests
assert to_list(reverse_list(build_list([1, 2, 3]))) == [3, 2, 1]
assert to_list(reverse_list(build_list([]))) == []
assert to_list(reverse_list(build_list([5]))) == [5]

print("Challenge 3: all tests passed.")
