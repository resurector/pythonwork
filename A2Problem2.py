#Rasheed Hameed
# “I have not given or received any unauthorized assistance on this assignment.” 
# 10-06-2018
# A2-P2: STEM AND LEAF


def FileReader(filename):
    'input filename and output list'
    infile=open(filename, 'r')          #open file
    content = infile.read()             #read the file in a list
    Record = content.split()            #seperate it
    infile.close()                      #Close it
    return Record                       #return the value back


   
def StemAndLeaf():
    'plots a stem and leaf plot after taking in a list'
    
    #Greet's user
    print('\n')
    print('Hello user please proceed by entering your input for file')
    
    try:    
            
        
        #While loop loops until the user exits
        while True:
          
            listx=[]        #Reseting to protect from illegal entry
            Entry = int(input('Please input 1, 2, 3 or 4 to exit: '))
            print('\n')
            print('STEM AND LEAF PLOT')
            print('\n')
            
            #Entry 1 choose file 1
            if (Entry==1):
                listx = FileReader('StemAndLeaf1.txt')
                Entry=0             #Reset value
            
            #Entry 2 choose file 2    
            elif (Entry==2):
               listx = FileReader('StemAndLeaf2.txt')
               Entry=0              #Reset value
            
            #Entry 3 choose file 3
            elif (Entry==3):
                listx = FileReader('StemAndLeaf3.txt')
                Entry=0             #Reset Value
            
            #Entry 4  to exit   
            elif (Entry==4):
                break
             
            stem = []               #Reset and starter
            leaf = []               #Reset and Starter
            temp = {}               #Resest and starter dictionary
            
            #Converting List to integers to help with sorting
            for i in range(len(listx)):
                listx[i]=int(listx[i])
            listx.sort()
            
            #Converting back to strings to mutate digits
            for i in range(len(listx)):
                listx[i]=str(listx[i])
            #Adding below a temporary item to the list to help get to the end
            #of the list
            listx.append('x')               
            #print(listx)
            
            
            
            for i in range(len(listx)):
                #Case when there is only 2 digits
                if len(listx[i])==2:
                    if listx[i][0:1]!=listx[i+1][0:1]:          #When the next value doesn't match the value then pick that stem 
                        stem.append(listx[i][0:1])              
                    leaf.append(listx[i][-1])
                    if stem.count(listx[i][0])==1:              #When u have at least a stem so grab and reset
                        temp[stem[0]]=leaf
                        stem=[]
                        leaf=[]
                
                #Case when there is only 4 digits
                elif len(listx[i])==3:
                    if listx[i][0:2]!=listx[i+1][0:2]:          #When the next value doesn't match the value then pick that stem 
                        stem.append(listx[i][0:2])
                    leaf.append(listx[i][-1])
                    if stem.count(listx[i][0:2])==1:
                        temp[stem[0]]=leaf
                        stem=[]
                        leaf=[]
                        
                #Case when there is only 3 digits        
                elif len(listx[i])==4:
                    if listx[i][0:3]!=listx[i+1][0:3]:
                        stem.append(listx[i][0:3])
                    leaf.append(listx[i][-1])
                    if stem.count(listx[i][0:3])==1:
                        temp[stem[0]]=leaf
                        stem=[]
                        leaf=[]
            
            stem.append(listx[-1][0:3])                         #grab the last items of the list due to adding the extra item at the end
            leaf.append(listx[-1][1:3])                         #grab the last item of list  
            for k,v in temp.items():
                     print('   {:3} | {:4}'.format(k,'  '.join(v)))  
    
    except ValueError:
        # executed only if a ValueError exception is raised
        print('Invalid input. Starting from beginning again')
        StemAndLeaf()

  

StemAndLeaf()

