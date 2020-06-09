# Relative_frequencies

**Author:** Eduardo de Andrade;

**Languages/Tools/Frameworks:** Python
 
**Date:** 09/05/2020

**Description:**
A set of functions that return relative frequencies(absolute frequecy,relative frequency,accumulated frequecy, accumulated relative frequency) from a dataset.

### **Run:**
  - #### 1. Move the file relative_frequency.py for inside of your python project and import the library in the file you want to use the library:<br>
              
              import relative_frequency as relF

              
  - #### 2.Use as desired functions. The library contains 5 functions:
    -  ###  **absolute_frequency(list)**
          **Calculate the absolute frequecy and return a DataFrame**
            
          **Input:** list  &nbsp;
          **Return:** dataFrame

        
    - ### **accumulated_frequency(list)**
         **Calculate the accumulated frequecy and return a DataFrame**
        
        **Input:** list
        **Return:** dataFrame

         
    - ###  **relative_frequency(list)**     
        **Calculate the relative frequecy and return a DataFrame**
        
        **Input:** list  &nbsp;
        **Return:** dataFrame

     - ###  **relative_accumulated_frequency(list)**    
          **Calculate the accumulated relative frequecy and return a DataFrame**
        
        **Input:** list  &nbsp;
        **Return:** dataFrame
              
      - ###  **all_frequencys(list)**    
        **Calculate all frequecys(absolute,accumulated,relative and relative accumulated) and return a DataFrame**
        
        **Input:** list  &nbsp;
        **Return:** dataFrame
     

### **Exemples:**
        
  &nbsp;&nbsp; **Import and define arrays:**
               
             import relative_frequency as relF

              data1=[2114,7119,7119,1876,4278,3183,1932,1355,4278,1030,2000,1077,5835,1512,1697,2478,3981,1643,1643,1500,4608,1000,1030]
              data2= [35,51,44,42,37,38,36,39,44,43,40,40,32,39,41,38,42,35,40,46,37,35,41,39,42,39]
              data3= [507,389,305,305,336,310,387,442,373,428,387,454,323,441,388,426,411,382,305,450,309,416,359,388,307,337,469,351,422,413,337]
              data4= [1595,1595,1820,1580,1804,1635,1820,2020,1820,1250,2083,1522,1306,1572,1778,2296,1445,1716,1618,1824]
              
              
 &nbsp;&nbsp;  **absolute_frequency(list):**
                  
               print(f'\n\nAbsolute Frequency of data1:\n')
               print(relF.absolute_frequency(data1))
      
&nbsp;&nbsp;Output:
   
            Absolute Frequency of data1:

                  Value  Ab.Frequency
              0    2114             1
              1    7119             2
              2    1876             1
              3    4278             2
              4    3183             1
              5    1932             1
              6    1355             1
              7    1030             2
              8    2000             1
              9    1077             1
              10   5835             1
              11   1512             1
              12   1697             1
              13   2478             1
              14   3981             1
              15   1643             2
              16   1500             1
              17   4608             1
              18   1000             1
  
&nbsp;&nbsp;  **accumulated_frequency(list):**
  
            print(f'\n\nAccumulated Frequency of data2:\n')
            print(relF.accumulated_frequency(data2))
    
   &nbsp;&nbsp;Output:
   
        Accumulated Frequency of data2:

              Value  Ac.Frequency
          0      35             3
          1      51             4
          2      44             6
          3      42             9
          4      37            11
          5      38            13
          6      36            14
          7      39            18
          8      43            19
          9      40            22
          10     32            23
          11     41            25
          12     46            26
   
   &nbsp;&nbsp;**relative_frequency(list):**
   
          print(f'\n\nRelative Frequency of data3:\n')
          print(relF.relative_frequency(data3)))
      
  &nbsp;&nbsp;Output:
              
          Relative Frequency of data3:

              Value  Rel.Frequency
          0     507          3.226
          1     389          3.226
          2     305          9.677
          3     336          3.226
          4     310          3.226
          5     387          6.452
          6     442          3.226
          7     373          3.226
          8     428          3.226
          9     454          3.226
          10    323          3.226
          11    441          3.226
          12    388          6.452
          13    426          3.226
          14    411          3.226
          15    382          3.226
          16    450          3.226
          17    309          3.226
          18    416          3.226
          19    359          3.226
          20    307          3.226
          21    337          6.452
          22    469          3.226
          23    351          3.226
          24    422          3.226
          25    413          3.226

  &nbsp;&nbsp; **relative_accumulated_frequency(list):**
            
              print(f'\n\nRelative Accumulated Frequency of data4:\n')
              print(relF.relative_accumulated_frequency(data4))
              
   &nbsp;&nbsp;output:     
                
              Relative Accumulated Frequency of data4:

                  Value  Ac. Relative Frequency
              0    1595                    10.0
              1    1820                    25.0
              2    1580                    30.0
              3    1804                    35.0
              4    1635                    40.0
              5    2020                    45.0
              6    1250                    50.0
              7    2083                    55.0
              8    1522                    60.0
              9    1306                    65.0
              10   1572                    70.0
              11   1778                    75.0
              12   2296                    80.0
              13   1445                    85.0
              14   1716                    90.0
              15   1618                    95.0
              16   1824                   100.0
                         
  &nbsp;&nbsp; **all_frequencys(list):**
            
              print(f'\n\nAll Frequencys of data1 and data3:\n')
              print("Data1:\n")
              print(relF.all_frequencys(data1))
              print("\nData3:\n")
              print(relF.all_frequencys(data3))

   &nbsp;&nbsp;output:     
                
              All Frequencys of data1 and data3:

              Data1:

                  Value  Ab.Frequency  Ac.Frequency  Rel.Frequency  Ac. Relative Frequency
              0    2114             1             1          4.348                    4.35
              1    7119             2             3          8.696                   13.05
              2    1876             1             4          4.348                   17.39
              3    4278             2             6          8.696                   26.09
              4    3183             1             7          4.348                   30.44
              5    1932             1             8          4.348                   34.79
              6    1355             1             9          4.348                   39.13
              7    1030             2            11          8.696                   47.83
              8    2000             1            12          4.348                   52.18
              9    1077             1            13          4.348                   56.53
              10   5835             1            14          4.348                   60.87
              11   1512             1            15          4.348                   65.22
              12   1697             1            16          4.348                   69.57
              13   2478             1            17          4.348                   73.92
              14   3981             1            18          4.348                   78.27
              15   1643             2            20          8.696                   86.96
              16   1500             1            21          4.348                   91.31
              17   4608             1            22          4.348                   95.66
              18   1000             1            23          4.348                  100.00

              Data3:

                  Value  Ab.Frequency  Ac.Frequency  Rel.Frequency  Ac. Relative Frequency
              0     507             1             1          3.226                    3.23
              1     389             1             2          3.226                    6.46
              2     305             3             5          9.677                   16.13
              3     336             1             6          3.226                   19.36
              4     310             1             7          3.226                   22.58
              5     387             2             9          6.452                   29.04
              6     442             1            10          3.226                   32.26
              7     373             1            11          3.226                   35.49
              8     428             1            12          3.226                   38.71
              9     454             1            13          3.226                   41.94
              10    323             1            14          3.226                   45.17
              11    441             1            15          3.226                   48.39
              12    388             2            17          6.452                   54.84
              13    426             1            18          3.226                   58.07
              14    411             1            19          3.226                   61.30
              15    382             1            20          3.226                   64.52
              16    450             1            21          3.226                   67.75
              17    309             1            22          3.226                   70.97
              18    416             1            23          3.226                   74.20
              19    359             1            24          3.226                   77.43
              20    307             1            25          3.226                   80.65
              21    337             2            27          6.452                   87.10
              22    469             1            28          3.226                   90.33
              23    351             1            29          3.226                   93.56
              24    422             1            30          3.226                   96.78
              25    413             1            31          3.226                  100.00

**To run the examples on your machine, move the description.py file into your project and run.**
