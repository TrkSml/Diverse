from math import sqrt

def verif(input):
      try :
        return int(str(input))==input
      except ValueError :
         return False
         
class Sudoku(object):

    data=[]
    def __init__(self,data):
        self.data=data

    def cell(self,list):
        return int(sqrt(len(self.data[0])))
        
    def verif_data(self,list):
        FLAG1=(abs(int(sqrt(len(list[0])))-sqrt(len(list[0])))==0.0)
        FLAG2=[len(c) for c in list].count(len(list[0])) == len(list)
        FLAG3=[[1<=c<=len(list[0]) and verif(c) for c in list[j]].count(True)==len(list[0]) for j in range(len(list))].count(True)==len(list)   
        return FLAG1 and FLAG2 and FLAG3
    
    def verif_rows(self,list):
        if self.verif_data(list):
            table_true=[len(set(list[c]))==len(list[c]) for c in range(len(list))]
            return table_true.count(True)==len(list)
        else :
            return False
        
    def verif_col(self,list):
        if self.verif_data(list):
            table_true=[len([list[c][j] for c in range(len(list[j]))])==len(set([list[c][j] for c in range(len(list))])) for j in range(len(list[0]))]
            return table_true.count(True)==len(list)
        else :
            return False
        
    def valid(self,list):
        return  self.verif_rows(list) and self.verif_col(list)
      
    def extract(self,seq):
        support=[]
        for c in seq:
            support.extend(c)
        return support
        
    def org_data(self,list):
          nbr=self.cell(list)
          col=0
          total=[]
          while(col<len(list)):
              row=0
              while(row<len(list[0])):
                  total.append(list[col][row:row+nbr])
                  row+=nbr
              col+=1
          return total
              
    def construct(self,l):
        nbr=self.cell(l)
        work=self.org_data(l)
        flow=0
        rows=[]
        FLAG=True
        while(flow<len(work)):
            count=0
            part=[]
            while(count<nbr):
                part.append(work[flow])
                count+=1
                flow+=1
            rows.append(part)
        flow=0
        partition=[]
        while(flow<len(rows)):
            count=0
            part=[]
            while(count<nbr):
                part.append(rows[flow])
                count+=1
                flow+=1
            partition.append(part)
          
        for el in partition :
          tool=[]
          for element in el:
               tool.append(element)
          study=[len(set(self.extract(list(c))))==len(self.extract(list(c))) for c in zip(*[c for c in tool])]
          if not(study.count(True)==len(study)) :
              FLAG=False
              break
              
        return FLAG       
        #find a way to use zip 
                      
    def is_valid(self):
        if self.verif_rows(self.data) and self.verif_col(self.data) :
            return self.construct(self.data)
        else :
            return False 


lis=[
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]

]

Su=Sudoku(lis)

print(Su.is_valid())   

        
        
        
