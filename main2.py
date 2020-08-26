class Node:
    def __init__(self, year, highlight, nexet=None):
        self.year = year
        self.highlight = highlight
        self.nexet = nexet
    
    def get_year(self):
        return self.year
    
    def get_highlight(self):
        return self.highlight
    
    def set_year(self, year):
        self.year = year
    
    def set_highlight(self, highlight):
        self.highlight = highlight


class Linkedlist:
    def __init__(self, year, highlight):
        node = Node(year, highlight)
        self.head = node
        self.tail = node
        node.nexet = None        

    def add_tail(self, year, highlight):
        node = Node(year, highlight)
        self.tail.nexet = node
        #node.nexet = None
        self.tail = node

    def add_between(self, prev_node, current_node, year, highlight):
        node = Node(year, highlight, current_node)
        prev_node.nexet = node


    '''def search(self, item):
        current_node = self.head
        missed_years = []
        while current_node:
            if current_node.year == item or item in missed_years:
                pass
            else:
                missed_years.append(item)
            current_node = current_node.nexet
        return missed_years'''

    '''def search(self, item):
        current_node = self.head
        while current_node:
            if current_node.year != item:
                current_node = current_node.nexet
            else:
                exist = True
            
            if current_node == None:
                exist = False
        return exist'''

    def print_linkedlist(self):
        current_node = self.head
        while current_node:
            print(current_node.year, current_node.highlight)
            current_node = current_node.nexet

    def count_items(self):
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.nexet
        
        return counter



years_list = Linkedlist(1, "I was born")
years_list.add_tail(3, "I started walking")
years_list.add_tail(7, "I turned seven")

current_node = years_list.head
prev_node = current_node
new_node = current_node
counter = 1
age = int(input("Your age: "))

while counter <= age:

    if current_node.year != counter:
        
        memory = input(f"Good memories in {counter}: ")
        if current_node.nexet or current_node.year > counter:   
        #    print(f'between node{counter}')
            years_list.add_between(new_node, current_node, counter, memory)  
            new_node = prev_node.nexet 
            prev_node = new_node 
            current_node = new_node.nexet 
        else:
        #    print(f'tail node{counter}')
            years_list.add_tail(counter, memory) 
            new_node = current_node.nexet
            current_node = new_node
            
        
    else:
        prev_node = current_node
        if current_node.nexet:
        #    print(f'exist node{counter}')
            current_node = current_node.nexet #(i1)3  #(i3)7
        #else:
        #    print(f'exist node{counter}')
            
        new_node = prev_node
    counter += 1

years_list.print_linkedlist()


