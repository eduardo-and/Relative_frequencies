import relative_frequency

relF = relative_frequency

#
#Functions
#
#1. absolute_frequency(list)
#   
#    Calculate the absolute frequecy and return a DataFrame       
#          
#    Input: list
#    Return: dataFrame
#
#2. accumulated_frequency(list)
#   
#    Calculate the accumulated frequecy and return a DataFrame      
#          
#    Input: list
#    Return: dataFrame
#
#3. relative_frequency(list)
#   
#    Calculate the relative frequecy and return a DataFrame     
#          
#    Input: list
#    Return: dataFrame
#
#4. relative_accumulated_frequency(list)
#   
#    Calculate the accumulated relative frequecy and return a DataFrame     
#          
#    Input: list
#    Return: dataFrame
#
#5. all_frequencys(list)
#   
#    Calculate all frequecys(absolute,accumulated,relative and relative accumulated) and return a DataFrame      
#          
#    Input: list
#    Return: dataFrame



# Note: 
#   It is not necessary to use function (1)out.treat_input before using the other functions, they already perform the treatment in input.

#EXEMPLES:

data1= [2114,7119,7119,1876,4278,3183,1932,1355,4278,1030,2000,1077,5835,1512,1697,2478,3981,1643,1643,1500,4608,1000,1030]
data2= [35,51,44,42,37,38,36,39,44,43,40,40,32,39,41,38,42,35,40,46,37,35,41,39,42,39]
data3= [507,389,305,305,336,310,387,442,373,428,387,454,323,441,388,426,411,382,305,450,309,416,359,388,307,337,469,351,422,413,337]
data4= [1595,1595,1820,1580,1804,1635,1820,2020,1820,1250,2083,1522,1306,1572,1778,2296,1445,1716,1618,1824]


print(f'\n\nAbsolute Frequency of data1:\n')
print(relF.absolute_frequency(data1))

print(f'\n\nAccumulated Frequency of data2:\n')
print(relF.accumulated_frequency(data2))

print(f'\n\nRelative Frequency of data3:\n')
print(relF.relative_frequency(data3))

print(f'\n\nRelative Accumulated Frequency of data4:\n')
print(relF.relative_accumulated_frequency(data4))

print(f'\n\nAll Frequencys of data1 and data3:\n')
print("Data1:\n")
print(relF.all_frequencys(data1))
print("\nData3:\n")
print(relF.all_frequencys(data3))

