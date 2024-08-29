class MinStack(object):

    def __init__(self):
        self.stack = [] #main stack
        self.min_stack = []#holds the min values from main stack

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val) #adds value to top of stack
        if not self.min_stack or val <= self.min_stack[-1]: 
            #checks if min_stack empty, if empty if so add val to stack
            #if next value added to main stack is smaller than min value add to min stack and pop of main
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:#checks if empty before attempting a pop
            popped = self.stack.pop()#removes the top element of main stack
            if self.min_stack and popped == self.min_stack[-1]:
            #check if min stack is empty and see if current popped element is the new last element minstack
                self.min_stack.pop()
            #if theres more than one element in min check if main stack pop last element in main
            #if popped is same as last element in min stack remove that too
            #ensures that min value is only one element

    def top(self):
        """
        :rtype: int
        """
        if self.stack:#if stack is not empty
            return self.stack[-1]#return the last element
        return -1 #returns -1 if stack empty raises and error
        
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack: #if min stack not empty
            return self.min_stack[-1]#get last element
        return -1 #if its empty raise an error


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()