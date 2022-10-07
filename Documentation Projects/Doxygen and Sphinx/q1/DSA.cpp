#include <bits/stdc++.h>
#define ll long long int
#define vi vector<int>
#define vll vector<ll>
using namespace std;

/**
*@file DSA.cpp
*@author Yash Kulkarni
*@date Sep 21 2022
*@brief It is about various Linked List Nodes
*/
/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------
/*! \brief Brief Description of SinglyLinkedListNode.
 *         Brief Description continued.
 *         
 *  Detailed description starts here.
 */
class SinglyLinkedListNode {

    public:
    /// @brief This is about Singly Linked List Node
        ll data;
        SinglyLinkedListNode* next;
        
        SinglyLinkedListNode () {
            ///@param[out] data
            ///
            /// @brief This is constructor w/o parameter 
            data = -1;
            next = NULL;
        }
        
        SinglyLinkedListNode (ll val) {
            ///@param[in] val
            ///@param[out] data
            ///
            /// @brief This is destructor with parameter val
            data = val;
            next = NULL;
        }

};

ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}
/*! \brief Brief Description about SinglyLinkedList.
 *
 *         Brief Description continued.
 *         
 */
class SinglyLinkedList {

    public:
        
        SinglyLinkedListNode *head, *tail;
        /// @brief This is about Singly Linked List
        SinglyLinkedList () {
            ///@param[out] head
            ///
            /// @brief This is constructor w/o parameter
            /*! 
            * @brief head - One of the variables used
            *
            * @brief tail - Another variable used
            *
            * @brief data - Another variable used  
            *
            * @brief ptr - Another variable used
            *
            * @brief Functions- insert,find, deleteVal, printer, reverse
            */
            
            head = NULL;
            tail = NULL;
        }
        
        void insert (ll data) {
            ///@param[in] data
            ///
            ///@brief This is member function insert
            SinglyLinkedListNode *node = new SinglyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
            }
            tail = node;
        }
        
        SinglyLinkedListNode* find (ll data) {
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL && ptr -> data != data) {
                prev = ptr;
                ptr = ptr -> next;
            }
            ///@param[in] data
            ///@param[out] prev
            ///
            ///@brief This is member function
            return prev;
        }
        
        bool deleteVal (ll data) {
            ///@param[in] data
            ///
            ///@brief This is member function deleteVal
            SinglyLinkedListNode *prev = find(data);
            if (prev -> next == NULL) {
                return false;
            }
            prev -> next -> next = prev -> next;
            return true;
        }
        
        void printer (string sep = ", ") {
            ///
            ///@brief This is member function printer
            SinglyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        
        void reverse () {
            ///
            ///@brief This is member function reverse
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL) {
                SinglyLinkedListNode *ptr2 = ptr -> next;
                ptr -> next = prev;
                prev = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = prev;
        }

};

SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2) {

            ///@param[in] list1
            ///@param[in] list2
            ///@param[out] merged
            ///
            ///@brief This is function merge
    SinglyLinkedList merged;
    SinglyLinkedListNode *head1 = list1.head, *head2 = list2.head;
    while (head1 != NULL && head2 != NULL) {
        if (head1 -> data < head2 -> data) {
            merged.insert(head1 -> data);
            head1 = head1 -> next;
        }
        else {
            merged.insert(head2 -> data);
            head2 = head2 -> next;
        }
    }
    if (head1 == NULL && head2 != NULL) {
        merged.tail -> next = head2;
    }
    if (head2 == NULL && head1 != NULL) {
        merged.tail -> next = head1;
    }
    return merged;
}

/*! \brief Brief Description of DoublyLinkedListNode.
 *         Brief Description continued.
 *         
 *  Detailed description starts here.
 */
// ------------------------------- Doubly Linked List -----------------------------

class DoublyLinkedListNode {

    public:
        
        ll data;
        DoublyLinkedListNode *next, *prev;
        
        DoublyLinkedListNode () {
            /**
            *This is a constructor
            *
            */
            data = -1;
            next = NULL;
            prev = NULL;
        }
        
        DoublyLinkedListNode (ll val) {
            /**
            *This is a constructor
            *
            */
            data = val;
            next = NULL;
            prev = NULL;
        }

};

ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}
/*! \brief Brief Description of DoublyLinkedList.
 *         Brief Description continued.
 *         
 *  Detailed description starts here.
 */
class DoublyLinkedList {

    public:
        
        DoublyLinkedListNode *head, *tail;
        
        DoublyLinkedList () {
            ///This is a constructor
            ///
            ///DoublyLinkedListNode functions-  insert, printer, reverse
            head = NULL;
            tail = NULL;
        }
        
        void insert (ll data) {
            DoublyLinkedListNode *node = new DoublyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
                node -> prev = tail;
            }
            tail = node;
        }
        
        void printer (string sep = ", ") {
            DoublyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        
        void reverse () {
            DoublyLinkedListNode *ptr = head, *pr = NULL;
            while (ptr != NULL) {
                DoublyLinkedListNode *ptr2 = ptr -> next;
                if (ptr2 != NULL) {
                    ptr2 -> prev = ptr;
                }
                ptr -> next = pr;
                ptr -> prev - ptr2;
                pr = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = pr;
        }

};

// ------------------------------- Binary Search Tree -----------------------------
/*! \brief Brief Description of BSTNode.
 *         Brief Description continued.
 *         
 *  Detailed description starts here.
 */
class BSTNode {

    public:

        ll info, level;
        BSTNode *left, *right;
        
        BSTNode (ll val) {
            ///This is a constructor
            ///
            info = val;
            level = 0;
            left = NULL;
            right = NULL;
        }

};

ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}
/*! \brief Brief Description of BinarySearchTree.
 *         Brief Description continued.
 *         
 *  Detailed description starts here.
 */
class BinarySearchTree {

    public:
        
        BSTNode *root;
        
        enum order {PRE, IN, POST};
        
        BinarySearchTree () {
             ///This is a constructor
             ///
             ///BinarySearchTree Functions- insert, traverse, height 
            root = NULL;
        }
        
        void insert(ll val) {
            if (root == NULL) {
                root = new BSTNode(val);
            }
            else {
                BSTNode *ptr = root;
                while (true) {
                    if (val < ptr -> info) {
                        if (ptr -> left != NULL) {
                            ptr = ptr -> left;
                        }
                        else {
                            ptr -> left = new BSTNode(val);
                            break;
                        }
                    }
                    else if (val > ptr -> info) {
                        if (ptr -> right != NULL) {
                            ptr = ptr -> right;
                        }
                        else {
                            ptr -> right = new BSTNode(val);
                            break;
                        }
                    }
                    break;
                }
            }
        }
        
        void traverse (BSTNode* T, order tt) {
            if (tt == PRE) {
                cout << T << endl;
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == IN) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                cout << T << endl;
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == POST) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
                cout << T << endl;
            }
        }
        
        ll height(BSTNode *T) {
            if (T -> left == NULL && T -> right == NULL) {
                return 0;
            }
            else if (T -> right == NULL) {
                return 1 + height(T -> left);
            }
            else if (T -> left == NULL) {
                return 1 + height(T -> right);
            }
            return max(1 + height(T -> left),1 + height(T -> right));
        }

};

// ------------------------------- Suffix Trie -----------------------------
/*! \brief Brief Description of Trie.
 *         Brief Description continued.
 *         
 *  Detailed description starts here.
 */
class Trie {

    public:
        
        ll count;
        map<char,Trie*> nodes;
        
        Trie () {
            ///This is a constructor
            ///
            ///Trie Functions- find, insert, checkPrefix, countPrefix
            count = 0;
            nodes = map<char,Trie*>();
        }
        
        bool find(Trie* T, char c) {
            return ((T -> nodes).find(c) != (T -> nodes).end());
        }
        
        void insert(string s) {
            Trie* ptr = this;
            for (auto c: s) {
                if (!find(ptr,c)) {
                    (ptr -> nodes)[c] = new Trie();
                }
                ptr = (ptr -> nodes)[c];
                (ptr -> count)++;
            }
        }
        
        bool checkPrefix(string s) {
            Trie* ptr = this;
            for (ll i = 0; i < s.length(); i++) {
                if (!find(ptr,s[i])) {
                    if (i == s.length() - 1) {
                        (ptr -> nodes)[s[i]] = NULL;
                    }
                    else {
                        (ptr -> nodes)[s[i]] = new Trie();
                    }
                }
                else if ((ptr -> nodes)[s[i]] == NULL or i == s.length() - 1) {
                    return true;
                }
                ptr = (ptr -> nodes)[s[i]];
            }
            return false;
        }
        
        ll countPrefix(string s) {
            bool found = true;
            Trie* ptr = this;
            for (auto c: s) {
                if (find(ptr,c)) {
                    ptr = (ptr -> nodes)[c];
                }
                else {
                    found = false;
                    break;
                }
            }
            if (found) {
                return ptr -> count;
            }
            return 0;
        }

};
//********************************************************************

/*! \brief Brief Description of Heap.
 *         Used to do operations on Heap Data Structure.
 *         
 *  It has various functions like left, right, parent, Heapify, insert,deletemin,min
 * 
 */
class Heap {
   private:
   vector <int> heap;
   public:
   int left(int parent);
   int right(int parent);
   int parent(int child);
   void Heapify(int index);
      Heap() {}
      void insert(int element);
      void deletemin();
      int min();
};
int main() {
   Heap h;
   while (1) {
      cout<<"1.Insert Element"<<endl;
      cout<<"2.Delete Minimum Element"<<endl;
      cout<<"3.Extract Minimum Element"<<endl;
      cout<<"4.Exit"<<endl;
      int c, e;
      cout<<"Enter your preference: ";
      cin>>c;
      switch(c) {
         case 1:
            cout<<"Enter the element to be inserted: ";
            cin>>e;
            h.Insert(e);
         break;
         case 2:
            h.DeleteMin();
         break;
         case 3:
            if (h.ExtractMin() == -1) {
               cout<<"Heap is Empty"<<endl;
            }
            else
            cout<<"Minimum Element: "<<h.ExtractMin()<<endl;
         break;
         case 4:
            exit(1);
            default:
            cout<<"Enter Correct Choice"<<endl;
      }
   }
   return 0;
}

void Heap::insert(int ele) {
      /*! \brief Brief Description of Insert function.
 *       
 *         
 *  It is used to insert a element in Heap.
 */
   heap.push_back(ele);
   heapify(heap.size() -1);
}
void Heap::deletemin() {
      /*! \brief Brief Description of deletemin function.
 *   
 *         
 *  It is used to delete the minimum value from Heap 
 */
   if (heap.size() == 0) {
      cout<<"Heap is Empty"<<endl;
      return;
   }
   heap[0] = heap.at(heap.size() - 1);
   heap.pop_back();
   heapify(0);
   cout<<"Element Deleted"<<endl;
}
int Heap::min() {
    /*! \brief Brief Description of min function.
 *   
 *         
 *  It is used to return the minimum value from Heap 
 */
   if (heap.size() == 0) {
      return -1;
   }
   else
   return heap.front();
}

int Heap::left(int parent) {
    /*! \brief Brief Description of left function.
 *   
 *         
 *  It is used to find the left element of child from Heap
 */
   int left = 2 * parent + 1;
   if (left < heap.size())
      return left;
   else
      return -1;
}
int Heap::right(int parent) {
/*! \brief Brief Description of right function.
 *   
 *         
 *  It is used to find the right element of child from Heap
 */
   int right = 2 * parent + 2;
   if (right < heap.size())
      return right;
   else
      return -1;
}
int Heap::parent(int child) {
    /*! \brief Brief Description of parent function.
 *   
 *         
 *  It is used to find the parent element from Heap
 */
   int parent = (child - 1)/2;
   if (child == 0)
      return -1;
   else
      return parent;
}
void Heap::Heapify(int in) {
    /*! \brief Brief Description of Heapify function.
 *   
 *         
 *  It is used to Heapify the elements from Heap
 */
   int child = l(in);
   int child1 = r(in);
   if (child >= 0 && child1 >= 0 && heap[child] > heap[child1]) {
      child = child1;
   }
   if (child > 0 && heap[in] > heap[child]) {
      int t = heap[in];
      heap[in] = heap[child];
      heap[child] = t;
      Heapify(child);
   }
}