################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------
"""
        This is SinglyLinkedListNode class
        
        """
class SinglyLinkedListNode:
    """
        SinglyLinkedListNode class is made
        
        It contains only initiations

        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """    
    
    def __init__(self, data):
        """
        This is constructor of SinglyLinkedListNode
        
        :param data: integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """
        This is parent function which finds parent element
        :return: integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        return str(self.data)

class SinglyLinkedList:
    """
        SinglyLinkedList class is made
        
        It contains initialization and functions- insert, find,deleteVal, printer, reverse and merge
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """ 
    def __init__(self):
        """
        This is constructor of SinglyLinkedList
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """
        This is insert function of SinglyLinkedList
        
        :param data: integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """
        This is find function of SinglyLinkedList
        
        :param data: integer
        :return: integer
    
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """
        This is deleteVal function of SinglyLinkedList
        
        :param data: integer
        :return bool
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep = ', '):
        """
        This is printer function of SinglyLinkedList
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """
        This is reverse function of SinglyLinkedList
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """
        This is merge function
        
        :param list1: List
        :param list2: List
        :return : List
    
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """
        This is DoublyLinkedListNode class

        It contains initializations
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
    def __init__(self, data):
        """
        This is constructor of DoublyLinkedListNode
        
        :param data: integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """
        This is merge function of SinglyLinkedList
        :return : Integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        return str(self.data) 

class DoublyLinkedList:
    """
        This is DoublyLinkedList class
        
        It contains initializations alongwith insert, printer and reverse 
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
    def __init__(self):
        """
        This is constructor of DoublyLinkedList
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """
        This is insert function of SinglyLinkedList
        
        :param data: Integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """
        This is printer function of DoublyLinkedList
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """
        This is reverse function of doublyLinkedList
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """
        This is BSTNode Class

        It contains initializations
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
    def __init__(self, info):
        """
        This is constructor of BSTNode
        :param info:String

        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """
        This is merge function of BSTNode
        :return : String
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        return str(self.info)

class BinarySearchTree:
    """
        This is BinarySearchTree class
        

        It contains initializations alongwith insert, traverse and height
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
    def __init__(self):
        """
        This is constructor of BinarySearchTree
        

        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        self.root = None
    
    def insert(self, val):
        """
        This is insert function of BinarySearchTree
        
        :param val : Integer
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """
        This is traverse function of BinarySearchTree
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        def preOrder(root):
            """
        This is preOrder function of traverse function in BinarySearchTree
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            """
        This is inOrder function of traverse function in BinarySearchTree
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            """
        This is postorder function of traverse function in BinarySearchTree
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """
        This is height function of BinarySearchTree
        :param root: List
            
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """
        This is Trie class


        It contains initializations alongwith find, insert, checkPrefix and reverse        
            
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
    def __init__(self):
        """
        This is constructor of Trie
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
        self.T = {}
    
    def find(self, root, c):
        """
        This is find function of Trie

        :param : root: List
        :param : c : Char
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
        return (c in root)
    
    def insert(self, s):
        """
        This is insert function of Trie
        
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
            """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """
        This is checkPrefix function of Trie
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """
        This is countPrefix function of Trie
        :Example:
        >>> from example import myfunc
        >>> myfunc(3, 'lol')
        'lollollol'
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0

class Heap:
    """
    Heap Class is made


    It contains initializations alongwith parent, left, right, insert, min, Heapify and deleteMin
    
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
    """
    def __init__(self, cap):
        """
        This is constructor
        
        :param cap: integer
        
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """
        This is parent function which finds parent element
        
        :param i: integer
        :return: integer
        
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        return (i - 1) // 2
    
    def left(self, i):
        """
        This is left function which finds left element
        
        :param i: integer
        :return: integer

    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        return (2 * i) + 1
    
    def right(self, i):
        """
        This is right function which finds right element
        
        :param i: integer
        :return: integer
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """
        This is insert function which performs insertion operation to insert element in heap.
        
        :param val: integer
        
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        if self.n != self.M:
            self.H[self.n] = val
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """
        This is min function which performs operation to extract minimum value from heap
        :return: integer
        
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """
        This is Heapify function which sorts Heap in bottom up or top down manner
        
        :param root: integer
        
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """
        This is deleteMin function which performs deletion operation to delete minimum value from heap.
        
    :Example:
    >>> from example import myfunc
    >>> myfunc(3, 'lol')
    'lollollol'
        """
        if n > 0:
            if n == 1:
                self.H = []
                n = 0
            else:
                n -= 1
                self.H[0] = self.H[n]
                self.Heapify(0)