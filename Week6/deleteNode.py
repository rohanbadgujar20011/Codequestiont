class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
  while (node != None):
    print(node.data, end=' ');
    node = node.next;
    
def insertEnd(head, data):
  new_node = Node(data)
  if head is None:
    head = new_node
    return head;
    
  last = head
  while (last.next):
    last = last.next
    
  last.next =  new_node
  return head;
def deleteNode(node):
    printList(node)
    if(node!=None):
        flag=0
        temp=node
        if(node.next==None):
            node=None
            temp=None
        else:
            while (node.next !=None):
                flag=1
                temp=node
                node=node.next
                temp.data=node.data
            temp.next=None
  
        printList(node)

def main():
    t = int(input().strip());
    for i in range(t):
        head = None;
        n = int(input().strip());
        k = 0;
        if(n!=0):
            inp = input().strip().split();
            print(inp)
            for j in inp:
                head = insertEnd(head,int(j.strip()));
            k = int(input().strip());
            node = head;
        if(k>0):
            while(k>0):
                node = node.next;
                k = k-1;
            deleteNode(node);
            printList(head);
            print();
if __name__ == "__main__":
  main();