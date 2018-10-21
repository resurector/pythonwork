#Rasheed Hameed
# “I have not given or received any unauthorized assistance on this assignment.” 
# 9-30-2018
# A2-P1   
        
def CountNameEnds():
    'Function takes in txt files of 1,000 boys and girls names and prints out counts of endings of those letters'
    
    #Read in text files into content1, and content2 and close those txt files after reading
    infile1 = open('namesBoys.txt', 'r')
    content1 = infile1.read()
    infile1.close()
    infile2 = open('namesGirls.txt','r')
    content2 = infile2.read()
    infile2.close()
    
    #Split the names in a list
    namesBoys = content1.split()
    namesGirls = content2.split()
    
    #Creating empty dictionaries for boys and girls
    
    counters1 = {}
    counters2 = {}

    #Grabbing a name and counting the letters that are present in those names for boys  
    for boy in namesBoys:
        if boy[-1] in counters1:
            counters1[boy[-1]]+=1
        else:
            counters1[boy[-1]] = 1
    #Grabbing a name and counting the letters that are present in those names for boys  
    for girl in namesGirls:
        if girl[-1] in counters2:
            counters2[girl[-1]] +=1
        else:
            counters2[girl[-1]] = 1
   
    #Creating a temporary list of lower case alphabets for later use
    temp = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        temp.append(char)
    
    #Creating a boys name ending letter dicionary with counts leter 
    #being keys and counts being value in alphabetical order     
    boys = {}
    for i in range(26):
        if temp[i] in counters1:
            boys.update({temp[i]:counters1[temp[i]]})
        else:
            boys.update({temp[i]:0})
           
   #Creating a girls name ending letter dicionary with counts leter 
   #being keys and counts being value in alphabetical order
    girls = {}
    for i in range(26):
        if temp[i] in counters2:
            girls.update({temp[i]:counters2[temp[i]]})
        else:
            girls.update({temp[i]:0})
      

    #Setting up the ending in formatting that would line up below
    print('{:25}{:29}{}'.format('Ending','Boys','Girls'))
    #Setting up counts in nice formatting
    for i in range(26):
        print('{:9}{:20}{:30}'.format(temp[i], boys[temp[i]], girls[temp[i]]))

CountNameEnds()

''' 
Notice that out of those 1000 boys and girls names Boys names most of boys 
names tend to end in letter n and for girls letter it is letter a. Additionally, 
boys names are more spread out on the letter spectrum while girls names have 
letters a, e, n, y endings to be more popular

'''
