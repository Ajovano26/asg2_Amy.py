#!/usr/bin/env python
# coding: utf-8

# In[104]:


#Amy Jovanovic 30003069


# In[105]:


#Question 1


# In[ ]:


# I defined the function evalPostFix to accept e as an argument
#The stack is LIFO format 
# The split function separates inputs by a space so please enter the postfix expression with spaces between each value
def evalPostFix(e):
    stack = []
    entries = e.split(" ")
    for i in entries:
        if i in '0123456789': #Checking that the entries are digits or an error is returned
            stack.append(i)
        else:
            if len(stack) == 1:
                stack.pop()
            elif len(stack) > 1:
                entry1 = stack.pop()
                entry2 = stack.pop()
                
                operators=set(['*','-','+','/']) #Checking that the operators are as specified in the assignment or an error is returned
                if i not in operators:
                               return "Error"
                elif i == "+":
                    entry3 = int(entry2) + int(entry)
                elif i == "-":
                    entry3 = int(entry2) - int(entry1)
                elif i == "*":
                    entry3 = int(entry2) * int(entry1)
                elif i == "/":
                    entry3 = int(entry2) / int(entry1)
                stack.append(entry3)
                
            else:
                    return "Error"

    if len(stack) == 1:
        print(stack.pop())
    else:
        return "Error"
e=input("The postix arithmetic expression to evaluate is ") #Please enter the postfix expression here (with spaces between entries)


evalPostFix(e)




# In[ ]:


#Question 2


# In[ ]:


#This portion of code is found in the Tutorial of Week 4 Class 2 on how to implement a linked list


# In[ ]:


class Node:
    def __init__(self,assign_value): 
        self.value = assign_value
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None         
    def insert_first(self,value):
        new_node = Node(value) # Create a new node 
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node 
        else:
            temp = self.head
            new_node.next = temp 
            self.head = new_node           
    def insert_last(self,value): 
        new_node = Node(value)
        if self.head == None and self.tail == None: 
            self.head = new_node  
            self.tail = new_node 
        else:
            temp = self.tail 
            temp.next = new_node 
            self.tail = new_node  
    def insert_middle(self, target, value):
        new_node = Node(value)
        temp = self.head
        while temp.next:
            if temp.value == target:  
                new_node.next = temp.next 
                temp.next = new_node
                break 
            else:
                temp = temp.next
    def delete_first(self):
        temp = self.head
        temp = temp.next 
        self.head = temp 
    def delete_last(self):
        p = self.head  
        q = self.head.next 
        while q: 
            p=p.next 
            q=q.next  
        p.next = None 
        self.tail = p
    def delete_value(self,value):
        p = self.head 
        q = self.head.next
        while q: 
            if q.value ==value:
                p.next = q.next
                break
            else:
                p=p.next
                q=q.next                 
    def print(self):
        if self.head == None:
            print("Linked list is empty")
        else: 
            temp = self.head 
            while temp: 
                print(temp.value, end=' ') 
                temp = temp.next  

#Part 1: Counting List elements:

    def count(self):
        temp = self.head
        count = 0
        if temp == None:
            return "0 elements"
        while temp !=None:
            count += 1
            temp = temp.next
        print(f'The number of elements in the list are {count}')

 #Part2:
    def addelement(self, value, location):
        temp = self.head
        if temp == None:
            return("The list is not initalized")
        else:
            if location == 0:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node
                print("Successful Operation")
                return True
            else:
                position = 0
                location = location - 1
                while temp != None and position < location:
                    temp = temp.next
                    position = position + 1
                if temp is None:
                    print("Provided location is outside list boundaries")
                else:
                    new_node = Node(value)
                    new_node.next = temp.next
                    temp.next = new_node
                    print("Successful Operation")
                    return True
                
   #Part 3: Printing the contents of the list
    def println(self):
        temp = self.head
        mainlist = []
        if temp == None:
            print("The list is not initialized")
        else:
            while temp != None:
                mainlist.append(temp.value)
                temp = temp.next
            if mainlist:
                print(mainlist)    
            else:
                print("Empty List")

    #Part 4: Reading the list to decipher if an element exists in the list

    def readlist(self, value):
        temp = self.head
        check = False
        if temp == None:
            print("The list is not initialized")
        else:
            while temp != None and check==False:
                if temp.value == value:
                    check = True
                else:
                    temp = temp.next
            if check == True:
                print(value, "The element exists within the linked list")
            else:
                print(value, "The element does not exist in the linked list")

##The following sample list entries are from tutorial week 4 class 2
my_list = linked_list() 

my_list.insert_first(20) # 20 
my_list.insert_first(50) # 50 20
my_list.insert_last(55) # 50 20 55 
my_list.insert_middle(20, 45) # 50 20 45 55
my_list.insert_middle(50, 25) #50 25 20 45 55
my_list.insert_middle(22, 3) # 25 22 55

#To execute part 1 of counting the elements in the list:
my_list.count()

#To execute part 2 please enter the value to insert into 'a' and the location into 'b'
a=14 
b=3
my_list.addelement(a,b)

#To execute part 3 of printing the list items like the way printed in python:
my_list.println()

#To execute part 4 of determining if an element exists within the list:
c=input("Does the following element exist in the list:")
my_list.readlist(c) # 55 is in the linked list

   


# 

# In[ ]:




