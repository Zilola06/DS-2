"""Challenge 8: Validate a Binary Search Tree"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#Time: O(n); auxiliary space: O(h) call stack (O(n) for a skewed tree).
def is_valid_bst(root, low=None, high=None):
    if root is None:
        return True
    if low is not None and root.val <= low:
        return False
    if high is not None and root.val >= high:
        return False
    return (
        is_valid_bst(root.left, low, root.val)
        and is_valid_bst(root.right, root.val, high)
    )


if __name__ == "__main__":
    assert is_valid_bst(Node(5, Node(1), Node(8, Node(6), Node(9))))
    assert not is_valid_bst(Node(5, Node(1), Node(8, Node(4), Node(9))))
    assert is_valid_bst(None)
    assert not is_valid_bst(Node(5, Node(5), Node(8)))
    assert is_valid_bst(Node(0, Node(-10), Node(10)))
    print("Challenge 8: all tests passed.")
