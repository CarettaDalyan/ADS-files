#Usual header comments here, please

#Create the Node class
class Node: 
#Initialise the node object using the usual constructor 
#this will have 3 attributes - the payload, next and prev pointers
#pass the payload in as an argument and assign to the payload attribute
#initialise next and prev to None
         
          
#Create the Stack, but it will be made of nodes, not individual items
class Stack: 
#intialize head using the usual contructor, set head to None 

          
#Add an element data in the stack  
    def push(self):
		#prompt for the payload to be added to the stack
        #if the head == None, i.e. there is nothing in the stack yet,head = a new Node
		#else -
		#make a temp_node with the data supplied
		#set self.head.prev to the temp_node
		#set temp_node.next to self.head
        #set temp_node.prev to None
		#set self.head to temp_node

#Remove an item and display which item was removed  
    def pop(self): 
		#if self.head = None, i.e. stack is empty, return None
		#else-
		#make a temp, set it to self.head.payload
		#set self.head to self. head.next
		#set self.head.prev to None
		#return the temp variable value
    
#Return the size of the stack  
    def getSize(self): 
		#make a temp var and set it to self.head
		#set count to zero
		#loop while temp != None
		#add 1 to count, set temp to temp.next
		#return count
      
#Check if the stack is empty or not   
    def isEmpty(self): 
		#if head = None then stack must be empty
		#or else it's not
		#return whether empty or not empty
 
#Display the stack 
    def showStack(self): 
		#set temp to self.head
		#loop while temp != None
		#print temp.payload, then set temp to temp.next     

#Initialize the stack
stack = Stack()

#Main program loop
while True:
	#display menu of options
	#1 displays status of stack (empty or not)
	#2 to push
	#3 to pop
	#4 to get size
	#5 to show contents
	#0 to quit
	#anything else is an error, loop should continue to run
	
   
  
