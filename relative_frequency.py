
import pandas as pd

# Calculate the absolute frequecy and return a DataFrame
# The function receive a list
def absolute_frequency(dataset):
    frq = [] 
    temp = []
    temp2 = []
    colName= ["Value","Ab.Frequency"]
    for count in range(0,len(dataset)):
        if(type(dataset) == list):
            if dataset[count] in temp2:
                continue
        else:
            return "Error! wrong input type! insert a list." 
            
        temp = [dataset[count],dataset.count(dataset[count])]  
        temp2.append(dataset[count])    
        frq.append(temp)    

    frq = pd.DataFrame(data=frq,columns=colName)
    return frq
 
    
# Calculate the accumulated frequecy and return a DataFrame
# The function receive a list 
def accumulated_frequency(dataset):
    tmp = absolute_frequency(dataset)
    value= tmp['Value']
    frq= tmp['Ab.Frequency']
    
    frqAc= []
    colName= ["Value","Ac.Frequency"]
    
    fsum= frq[0]
    frqAc.append([value[0],fsum])
    
    for count in range(1,len(value)):
        fsum+= frq[count]
        frqAc.append([value[count],fsum])
    
    frqAc= pd.DataFrame(data = frqAc,columns= colName)

    return frqAc

# Calculate the relative frequecy and return a DataFrame
# The function receive a list 
def relative_frequency(dataset):
    tmp = absolute_frequency(dataset)
    value= tmp['Value']
    frq= tmp['Ab.Frequency']
    
    frqAc= []
    colName= ["Value","Rel.Frequency"]
    
      
    for count in range(0,len(value)):
        frqr = frq[count]/len(dataset)*100
        frqr= round(frqr, 3)
        frqAc.append([value[count],frqr])
    
    frqAc= pd.DataFrame(data = frqAc,columns= colName)

    return frqAc

# Calculate the accumulated relative frequecy and return a DataFrame
# The function receive a list 
def relative_accumulated_frequency(dataset):
    tmp = relative_frequency(dataset)
    value= tmp['Value']
    frq= tmp['Rel.Frequency']
    
    frqAc= []
    colName= ["Value","Ac. Relative Frequency"]
    
    fsum= round(frq[0],2)
    frqAc.append([value[0],fsum])
    
    for count in range(1,len(value)):
        
        fsum+= frq[count]
        
        if(count+1 == len(value)):
            if(fsum>100.00):
                fsum=100.00
          
        frqAc.append([value[count],round(fsum,2)])
        
    frqAc= pd.DataFrame(data = frqAc,columns= colName)

    return frqAc

# Calculate all frequecys(absolute,accumulated,relative and relative accumulated) and return a DataFrame
# The function receive a list 
def all_frequencys(dataset):
   abF= absolute_frequency(dataset)
   acF= accumulated_frequency(dataset)
   rlF= relative_frequency(dataset)
   arF= relative_accumulated_frequency(dataset)
   
   abF.insert(loc=2,value= acF["Ac.Frequency"],column= "Ac.Frequency") 
   abF.insert(loc=3,value= rlF["Rel.Frequency"],column= "Rel.Frequency") 
   abF.insert(loc=4,value= arF["Ac. Relative Frequency"],column= "Ac. Relative Frequency") 
   
   return abF 



