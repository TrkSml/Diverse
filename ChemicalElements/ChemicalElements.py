"""
This was written the 26th of January 2017.
The code aims to determine the exact composition of a molecule and displays the number of the consisting atoms.
An exemple is shown at the end.
"""

import re

class Stack :
    #fix the nature of the input components
    open=['(','[','{']
    close=[')',']','}']
    stack=[]
    
    def stackk(self):
        return self.stack
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        self.stack.pop()

class chemical_elements:
    
	def uniq(self,list):
  	     unique=[]
  	     for el in list:
       		if not(el in unique) :
            	   unique.append(el)
   	     return unique

	def exist(self,el,string):
	     try:
	            a=string.index(el)
	            return [a,True]
	     except ValueError:
	            return False


	def detect_positions(self,el,string):
	    """
	    
	     We will work with the elements' positions at first. For this purpose, the function gives back an array
	     of the wanted position. A little difficulty here to combine one-worded elements and two-worded ones.
	    
	    """
	
	    result=[]
	    while(self.exist(el,string)) :
	          result.append(self.exist(el,string)[0])
	          string=string[:string.index(el)]+'*'*len(el)+string[string.index(el)+len(el):]
	    return result
    
            
            
	def parse_molecule(self,formula):

	    entities=self.uniq(re.findall('[A-Z][a-z]|[A-Z]',formula))
	    sorted=entities
	    sorted.sort(key=lambda x:len(x))
	    sorted=sorted[::-1]
	    dict={}
	    redlist=[]

	    for el in sorted :

	        positions=self.detect_positions(el,formula)
	        totalcoeff=0
	        prototype=formula

	        for pos in positions :

	          if not(pos in redlist) :

	            redlist.append(pos)
	            count=pos 
	            coeff=1
	            mult=re.findall(re.escape(el)+'\d*',prototype)

	            if mult: 

	              try:

	                   mult=re.findall('\d+$',mult[0])[0]
	                   coeff=int(mult)
	                   count+=len(str(mult[0]))
	              except IndexError: pass
                
	            s=Stack()

	            while count<(len(prototype)):

	                if prototype[count] in s.open: 
	                      s.push(prototype[count])

	                try :

	                    if prototype[count] in s.close: 
	                        s.pop()
                
	                except IndexError:
	                    mult=re.findall(re.escape(prototype[count-1]+prototype[count])+'\d+',prototype)
                    
	                    try :

	                      if mult : 
	                         mult=re.findall('\d+$',mult[0])
	                         coeff*=int(mult[0])
	                         count+=len(str(mult[0]))

	                    except IndexError: pass

	                count+=1

	            totalcoeff+=coeff 

	            prototype=prototype[:pos]+'*'*len(el)+prototype[pos+len(el):]

	        dict[el]=totalcoeff  
        
	    return dict            
            


		
#ch=chemical_elements()
#print(ch.parse_molecule('(C5H5)Fe(CO)2CH3'))







