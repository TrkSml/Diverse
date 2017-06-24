def search(list,number):
	end=len(list)-1
	begin=0

	while(end>=begin):
		if list[begin]+list[end] >number:
			end-=1
		elif list[begin]+list[end] <number:
			begin+=1
		else :
			return [list[begin],list[end]]
	return -1

# def advance(list,pos1,pos2):
# 	if pos1>pos2:
# 		return advance(list,pos2,pos1)
# 	if 1+pos1==pos2:
# 		pos1+=2
# 	else :
# 		pos+=1
# 	return pos1,pos2



##### different combinations of a given number of integers 
##### whose sums are equal to a certain output

def select_items(input,list_indexes):
	return [input[i] for i in list_indexes]

from collections import deque

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

list=range(100)
import time

#on a sorted list
#print search_equal_elements(list,52,7)





