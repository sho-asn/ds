""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is 
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert
            it. After insertion, performs sub-tree rotation whenever it becomes
            unbalanced.
            returns the new root of the subtree.

            Approach Taken:
            This method recursively find the place to insert item depending on the size of key.
            If the key is smaller than the key of current, current will move to the left node,
            and the number of the current's left-hand-side node increases by one.
            If the key is bigger than the key of current, current will move to the right node,
            and the number of the current's right-hand-side node increases by one.
            After the height of the current is updated, the tree will be re-balanced with
            the rebalance method. It returns the new root of the subtree.

            Worst Case Time Complexity :
            O(log n), where n is the total number of the node
            Worst case occurs when the item is inserted into the place that is the farthest from the root.
            """
        if current is None:
            current = AVLTreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.leftCount += 1
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.rightCount += 1
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError("Inserting duplicate item")
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        return self.rebalance(current)

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete. After deletion,
            performs sub-tree rotation whenever it becomes unbalanced.
            returns the new root of the subtree.

            Approach Taken:
            This method recursively find the key to delete and delete the item from the tree.
            If the key is smaller than the key of current, current will move to the left node,
            and the number of the current's left-hand-side node decreases by one.
            If the key is larger than the key of current, current will move to the right node,
            and the number of the current's right-hand-side node decreases by one.
            When the key is same as the key of the current, each implementation is conducted
            following by the node that attaches to the current node.
            After the height of the current is updated, the tree will be re-balanced with
            the rebalance method. It returns the new root of the subtree.

            Worst Case Time Complexity :
            O(log n), where n is the total number of the node
            When the item that is the farthest from the root is deleted.
        """
        if current is None:
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.leftCount -= 1
            current.left = self.delete_aux(current.left, key)
        elif key > current.key:
            current.rightCount -= 1
            current.right = self.delete_aux(current.right, key)
        else:  # key == current.key
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left
            else:  # (current.left is not None) and (current.right is not None)
                successor = self.get_successor(current)
                current.key = successor.key
                current.item = successor.item
                current.right = self.delete_aux(current.right, successor.key)

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        return self.rebalance(current)

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

            :complexity: O(1)

            Approach Taken:
            This method conducts the left rotation. The current root changes to the current root's right-hand-side node.
            It updates the number of the current's right-hand-side node and new root's left-hand-side node accordingly.
            It also updates the height of current and the new root. It returns the new root of the subtree.

            Worst Case Time Complexity:
            O(1) since equals and max is constant time complexity
        """
        new_root = current.right
        current.rightCount = current.right.leftCount
        new_root.leftCount = current.leftCount + 1 + new_root.leftCount
        temp = new_root.left
        new_root.left = current
        current.right = temp
        current.height = 1 + max(self.get_height(current.right), self.get_height(current.left))
        new_root.height = 1 + max(self.get_height(new_root.right), self.get_height(new_root.left))

        return new_root

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            Approach Taken:
            This method conducts the right rotation. The current root changes to the current root's left-hand-side node.
            It updates the number of the current's left-hand-side node and new root's right-hand-side node accordingly.
            It also updates the height of current and the new root. It returns the new root of the subtree.

            Worst Case Time Complexity:
            O(1) since equals and max is constant time complexity
        """
        new_root = current.left
        current.leftCount = current.left.rightCount
        new_root.rightCount = current.rightCount + 1 + new_root.rightCount
        temp = new_root.right
        new_root.right = current
        current.left = temp
        current.height = 1 + max(self.get_height(current.right), self.get_height(current.left))
        new_root.height = 1 + max(self.get_height(new_root.right), self.get_height(new_root.left))

        return new_root

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.

            complexity: O(1)
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def kth_largest(self, k: int) -> AVLTreeNode:
        """
        Returns the kth largest element in the tree.
        k=1 would return the largest.

        Approach Taken:
        Since k should not be 0 and k must be smaller than the length of the tree its length, it's first checked.
        The value of kth_largest_aux will be returned. We use an auxiliary function to pass a parameter into the
        kth_largest.

        worst complexity: O(log n), where n is the total number of nodes.
        when the kth largest is in the farthest place from the root.
        """
        if k == 0:
            raise ValueError("cannot enter 0")
        if k > len(self):
            ValueError("k must be smaller than the length of tree")
        return self.kth_largest_aux(self.root, k)

    def kth_largest_aux(self, current: AVLTreeNode, k: int) -> AVLTreeNode:
        """
        Approach Taken:
        This method is the real implementations to get the AVLTreeNode of the kth largest.
        When the k is smaller than current.rightCount + 1, the current moves to right.
        When the k is larger than current.rightCount + 1, the k has changed accordingly,
        and the current moves to left. When the k equals to current.rightCount + 1, it returns the
        current AVLTreeNode.

        worst complexity: O(log n), where n is the total number of nodes
        when the kth largest is in the farthest place from the root.
        """
        num_of_right = current.rightCount + 1
        if k == num_of_right:
            if current is None:
                return current
            return current
        elif k < num_of_right:
            if current.right is None:
                return current
            return self.kth_largest_aux(current.right, k)
        else:  # k > current.rightCount + 1
            if current.left is None:
                return current
            k = k - num_of_right
            return self.kth_largest_aux(current.left, k)
