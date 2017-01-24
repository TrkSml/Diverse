"""  
This is an expression simplifier basically written with Python2.7.
This is a solution I proposed to the CODEWARS Community.
Written by Tarek Samaali the 20th of January 2017.

"""


import re 
import itertools

class simplifier :

    def __init__(self,string):
        self.string=string
    
    def operators(self):
    """ 
	The operands (+/-) are extracted and somehow transformed to be ready to use later on
    """
        op=filter(lambda x:x!='',re.split('[a-z0-9]',self.string))

        if re.match('^[0-9a-z]',self.string):
            op=op[::-1]
            op.append('+')
            op=op[::-1]
        return [el + '1' for el in op]
        
    def terms(self):
    """ 
	Here we're extracting the items with which we'll be building the needed tokens
	
    """

        list=[ ''.join(sorted(el)) for el in re.split('[+-]',self.string)]

        if self.operators()[0]=='-1' or self.string[0]=='+':
            list=list[1:]
        return list
        
    def tokens(self):
    """
	The items are associated with their signs

    """
        list=self.terms()
        op=self.operators()
        all=[]

        for i in range(len(list)) :
            all.append([list[i],op[i]])

        return all
        
    def extract(self):

    """

	We're constructing three-based tokens: first column for the variables, second column for the sign and third one for the multiplied integers

    """

        tok=self.tokens()

        for el in tok :
            if re.match('^[0-9]',el[0]):

                count=0
                to_add=''

                while(el[0][count].isdigit()):
                    to_add+=el[0][count]
                    count+=1
                el[0]=el[0][count:]
                el.append(int(to_add[::-1]))

            elif re.match('^[a-z]',el[0]):
                el.append(1)

        return tok
    
    def add(self,first,second):

        return [first[0],'+1' if (int(first[1])*int(first[2])+int(second[1])*int(second[2])>=0) else '-1', abs(int(first[1])*int(first[2])+int(second[1])*int(second[2]))] 
        
    def simpl(self) :

    """
	This part aims to divide achieve simplifications. We thus have the total sums if the coefficients corresponding to the proper variables
	taking into account the resulting sign

    """	

        tokens=self.extract()
        final_stack = []
        stack_compare = [el[0] for el in final_stack]
        
        for i in range(len(tokens)) :

            if tokens[i][0] in stack_compare :
                pass

            else :    
                for j in range(i+1,len(tokens)):

                    if tokens[i][0]==tokens[j][0]:
                        tokens[i]=self.add(tokens[i],tokens[j])                    
                final_stack.append(tokens[i])
                stack_compare.append(tokens[i][0])
        

        return final_stack  
            
    def clean(self):

	"""
	The items with null coefficients are removed from the tokens list.

	"""

        simpl=self.simpl()
        try :
          for j in range(len(simpl)):

              if simpl[j][2]==0 :
                  simpl.pop(j)

        except IndexError :
              pass
        return simpl
              
    def sort(self):

	"""
	
	This part seems to be the hardest, I don't really think it was implemented with the best manners. 
	However, some advanced tests gave satisfactory results.
	All monomials appears in order of increasing number of variables. 
	If two monomials have the same number of variables, they appears in lexicographic order.
	There is no leading + sign, meaning that the first coefficient is positive.

	"""

        cleaned=self.clean()

        cleaned.sort(key=lambda x:len(x[0]))

        sort_by_length=[]  
        same_length=[]  
        ok=True

        for i in range(len(cleaned)-1) :

            if ok==False :
                same_length=[]
                ok=True

            if len(cleaned[i][0])==len(cleaned[i+1][0]):
                same_length.append(cleaned[i])

            elif len(cleaned[i][0])!=len(cleaned[i+1][0]) :
                ok=False
                same_length.append(cleaned[i])
                sort_by_length.append(same_length)

        if len(sort_by_length)==0:
            cleaned.sort(key=lambda x: x[0])
            return cleaned
            
        if len(cleaned[-1][0])==len(same_length[0][0]) :
            same_length.append(cleaned[-1])
            sort_by_length.append(same_length)

        else :
            sort_by_length.append([cleaned[-1]])
        

        if  len(sort_by_length)>0 :
            for el in sort_by_length :
                el.sort(key=lambda x:x[0])
        elif len(sort_by_length)==0:
            sort_by_length=cleaned

        final_list=[]
        
        for el in sort_by_length:
            final_list.extend(el)
        
        return final_list
        
        
    def construct(self):

	"""
	The last part consists in concatenating the resulting tokens. 
	This would give is the desired simplification. :)

	"""
        sort=self.sort()

        sort=[[el[0],el[1][0],el[2]] for el in sort]

        result=''
        for el in sort :
            if el[2]==1:
                result+=el[1]+el[0]
            else :
                result+=el[1]+str(el[2])+el[0]
        if result[0]=='+' :
            return result[1:]

        return result
                

    
        
        
