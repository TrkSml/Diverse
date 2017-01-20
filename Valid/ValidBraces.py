class Validator :
    #fix the nature of the input components
    open=['(','[','{']
    close=[')',']','}']
    stack=[]
    
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        self.stack.pop()
        
    def valid(self,list):
        FLAG=True
        if all(el in self.open for el in list) or all(el in self.close for el in list) :
            return False
        for el in list :
          try :
              if el in self.open:
                  self.push(el)
              if el in self.close:
	      #At this level we're checking whether the found component is the perfect opposite of the one at the top of the stack
                  if not(self.open.index(self.stack[len(self.stack)-1])==self.close.index(el)):                      
                      FLAG=not(FLAG)
                      break
                  self.pop()
                
          except IndexError:
              return False
            
        return FLAG    
        
def validBraces(list):
    v=Validator()
    
    return v.valid(list)
