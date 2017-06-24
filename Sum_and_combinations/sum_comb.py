
##### different combinations of a given number of integers within a sorted list
##### whose sums are equal to a certain output
##### Example :
#####
##### >>list=range(10)
##### >>search_equal_elements(list,10,4)
##### " list : [0,1,2,3,4,5,6,7,8,9]
##### " output demanded : 10 "
##### " number of elemenets to form a combination : 4 "
#####
##### result :
##### [[0, 0, 5, 5], [1, 0, 4, 5], [1, 1, 4, 4], [2, 1, 3, 4], [2, 2, 3, 3]]
#####
##### @author: Tarek Samaali
#####

from collections import deque

def select_items(input,list_indexes):
	return [input[i] for i in list_indexes]

def advance_begin(dq):
	dq[-1]+=1
	dq.rotate(1)
	return dq

def regress_end(dq):
	dq[-1]-=1
	dq.rotate(-1)
	return dq

def search_equal_elements(list,output,number):

	end=len(list)-1
	
	begin_set=[]
	end_set=[]
	if number%2:

		### To use repetitive numbers
		begin_set=[0]*((number+1)/2)
		end_set=[end for _ in range(number/2)]

		### To use unique numbers
		# begin_set=range((number+1)/2)
		# end_set=[end-i for i in range(number/2)]

	else :

		### To use repetitive numbers
		begin_set=[0]*(number/2)
		end_set=[end for _ in range(number/2)]

		### To use unique numbers
		# begin_set=range(number/2)
		# end_set=[end-i for i in range(number/2)]


	if number>=len(list):
		return -1

	dqbegin=deque(begin_set)
	dqend=deque(end_set)

	result=[]

	while(max(dqbegin)<min(dqend)):
	
		if sum(select_items(list,dqbegin)+select_items(list,dqend))>output:
			dqend=regress_end(dqend)

		if sum(select_items(list,dqbegin)+select_items(list,dqend))<output:
			dqbegin=advance_begin(dqbegin)

		if sum(select_items(list,dqbegin)+select_items(list,dqend))==output:
			result+=[select_items(list,dqbegin)+select_items(list,dqend)]
			dqend=regress_end(dqend)

	return result

######################################################################################
######################################################################################
######################################################################################

