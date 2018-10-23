# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:34:00 2018

@author: Ricardo
"""
# Course: CS2302
# Author: Ricardo Godoy
# Assignment: Lab 2 B
# T.A: Saha, Manoj
# Instructor: Diego Aguirre
# Date of last modification: 10/22/18


# This program reads a file that contains username and passwords and stores the password in a linked
# list. If a password is repeated, the program increments the count in the respective node. If not,
# a new node is created with the respective properties and added to the linked list. The list is
# sorted using bubble sort and merge sort. Along with that solution, a dictionary is also
# created to store the 20 most repeated passwords and identify them in the linked list. Finally,
# the program return the 20 most repeated passwords in descending order.

# Node class
class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None


# Reads the file, split and stores all passwords
def read(password_list):
    with open('10-million-combos.txt', 'r') as file:
        for line in file:
            line = line.split()
            if len(line) > 1:
                add_Password(password_list, line[1])


# Adds all passwords to a linked list
def add_Password(password_List, password):
    node = password_List.head
    while node != None:
        if node.password == password:
            node.count += 1
            return
        node = node.next
    password_List.head = Node(password, 1, password_List.head)


# Computes the size of the linked list
def get_List_Size(password_List):
    node = password_List.head
    list_Size = 0
    while node != None:
        list_Size += 1
        node = node.next
    return list_Size

# Adds all passwords to dictionary
def add_Password_to_Dictionary(password, Dict):
    if password in Dict:
        Dict[password] += 1
    else:
        Dict[password] = 1


# Inserts all passwords into the dictionary
def insert(password_List, Dict):
    for password in Dict:
        node = Node(password, Dict[password], password_List.head)
        password_List.head = node
        
 
def read_dict(password_List, Dictionary):       
    with open('10-million-combos.txt', 'r') as infile:
        for line in infile:
            read = line.split()
            if len(read) > 1:
                add_Password_to_Dictionary(read[1], Dictionary)


# Prints the list of the passwords most repeated
def print_List(password_List):
    node = password_List.head
    count = 0
    while node != None and count < 20:
        print(node.password + ":", node.count)
        node = node.next
        count += 1


# Sorts the list in descending order, with bubble sort algorithm
def bubble_Sort(password_List, list_Size):
    for i in range(list_Size):
        curr_Node = password_List.head
        next_Node = curr_Node.next

        for j in range(list_Size - 1):
            if curr_Node.count < next_Node.count:
                temp_Count = curr_Node.count
                curr_Node.count = next_Node.count
                next_Node.count = temp_Count
                temp_Password = curr_Node.password
                curr_Node.password = next_Node.password
                next_Node.password = temp_Password
            curr_Node = next_Node
            next_Node = next_Node.next
            
    
    
# The following three methods form part of the merge sort algorithm 
# Time complexity: O(log n)
def merge_Sort(password_List):

    if password_List == None or password_List.next == None:
        return password_List

    left_Half, right_Half = split(password_List)
    return merge_Lists(left_Half, right_Half)


# Splits the list in two
def split(password_List):
    if password_List == None or password_List.next == None:
        left_Half = password_List
        right_Half = None
        return left_Half, right_Half
    else:
        mid = password_List
        front = password_List.next
        while front != None:
            front = front.next
            if front != None:
                front = front.next
                mid = mid.next
    left_Half = password_List
    right_Half = mid.next
    mid.next = None
    return left_Half, right_Half


# Merge the two lists created above
def merge_Lists(left_Half, right_Half):
    new = Node("", -1, None)
    curr = new
    while left_Half and right_Half:
        if left_Half.count < right_Half.count:
            curr.next = right_Half
            right_Half = right_Half.next
        else:
            curr.next = left_Half
            left_Half = left_Half.next
        curr = curr.next
    if left_Half == None:
        curr.next = right_Half
    elif right_Half == None:
        curr.next = left_Half
    return new.next




def main():
    #Create list
    password_List = LinkedList()
    
    #Read file
    read(password_List)
    list_Size = get_List_Size(password_List)

    #Sort list with bubble sort and print
    bubble_Sort(password_List, list_Size)
    print_List(password_List)
    print("List size:", list_Size)
    
    #Sort list with merge sort and print
    new_Head = merge_Sort(password_List.head)
    new_List = LinkedList()
    new_List.head = new_Head
    print("Merge Sort:")
    print_List(new_List)
    
    #Create dictionary and print list sorted with bubble sort.
    list_Size = 0
    Dictionary = {}
    password_List = LinkedList()
    read_dict(password_List, Dictionary)
    insert(password_List, Dictionary)
    list_Size = len(Dictionary)
    bubble_Sort(password_List, list_Size)
    print("My dictionary, bubble sort: " )
    print_List(password_List)
    print("List size: " + str(list_Size))
    
    #Merge sort list created with dictionary
    new_head = merge_Sort(password_List.head)
    new_list = LinkedList()
    new_list.head = new_head
    print("Dictionary Merge Sort:")
    print_List(new_list)
    print("List size: " + str(list_Size))

main()
    