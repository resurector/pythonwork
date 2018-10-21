#Rasheed Hameed
#I have not given or received any unauthorized assistance on this assignment 
#Problem A1-P4
    



def Game():
    'Word game input any size word'    
    tempstart = []                                                                      #Empty list Constructor
    
    counter = 0                                                                         #Move counter
    
    #Instructions of the game below
    
    print('Instructions of the game:')      
    print('You start off by entering your name, beginning word,  and goal word')
    print('\n')
    print('You can add remove a letter by choosing the index')
    print('You can add at letter and at index or replace')
    
    #Inputs for name and choice of play
    name = input('Enter your name please: ')
    start = input('Enter your starting word: ')
    end = input('Enter your ending word: ')
    print('\n')

    print('Lets start')
    print('To insert type insert')
    print('To remove type remove')
    print('To replace type replace')
    print('To exit type exit')
    
    #inputchoice is the choice variable for the choices below
    inputchoice = input('Choose insert, remove, replace or exit: ')

    #split the string into a list to help choose
    for char in start:
            tempstart.append(char)
    
    #while loop when the starting word matches the finishing word
    while (start!=end):       
            
            #Case when the choice of play is to insert      
            if inputchoice=='insert':
                inputchoice = ''                                                  #zero out the choice variable to let user choose again
                counter+=1                                                        #increasing move counter
                letterchoice = input('Letter choice: ')                           #choose the letter
                inputindex = int(input('index position: '))                       #choose index  
                tempstart.insert(inputindex, letterchoice)                        #insert the choices  
                start=''.join(tempstart)                                          #join the split letters back to a string
                print(start)                                                      #show what we have 
                print('The Goal is: '+end)                                        #show what to reach to
              
                inputchoice = input('Choose insert, remove, replace or exit: ')   #give the choice of input again to 
            
            #Case when the choice of play is to remove a letter 
            elif inputchoice=='remove':
                inputchoice = ''                                                 #zero out the choice variable to let user choose again
                counter+=1                                                       #increasing move counter
                inputindex = int(input('index position: '))                      #index input
                if inputindex > len(start)-1:                                    #in case if you put an index that is out of bounds                       
                    print('index out of range') 
                    inputindex = int(input('index position: '))                  #re-enter the index
                tempstart.pop(inputindex)                                        #remove that index from the temporary list
                start=''.join(tempstart)                                         #show where we are at
                print(start)
                print('The Goal is: '+end)
                inputchoice = input('Choose insert, remove, replace or exit: ')

            #Case when the choice of play is to replace a letter     
            elif inputchoice== 'replace':
                inputchoice = ''                                                #zero out the choice variable to let user choose again
                counter+=1                                                      #increasing move counter
                inputindex = int(input('index position: '))
                letterchoice = input('Letter choice: ')
                tempstart[inputindex]=letterchoice                              #replace the index with the letter choice
                start=''.join(tempstart)
                print(start)
                print('The Goal is: '+end)
                inputchoice = input('Choose insert, remove, replace or exit: ')
            
            #Case when you want to exit the game
            elif inputchoice == 'exit':
                inputchoice = ''
                break
            
            #InCase when you accidently enter letter instead of number
            elif type(inputindex!=int):
                inputchoice = input('Choose insert, remove, replace or exit: ')
                
            #InCase when you accidently enter number instead of a letter
            elif type(letterchoice!=str):
                inputchoice = input('Choose insert, remove, replace or exit: ')
               
    #Exiting when the condition is met when start word equals the end word
    counter = str(counter)
    print(name + ' ' + 'Congratulations! you have finished the game.')
    print('The game was finished in: ' + ' ' + counter + ' ' + 'moves')
   
    
 
'''   
This game does a lot more than the problem has asked for.  We can input any size beginning word and any size ending word

Game()
Instructions of the game:
You start off by entering your name, beginning word,  and goal word


You can add remove a letter by choosing the index
You can add at letter and at index or replace

Enter your name please: Rasheed Hameed

Enter your starting word: super

Enter your ending word: night


Lets start
To insert type insert
To remove type remove
To replace type replace
To exit type exit

Choose insert, remove, replace or exit: insert

Letter choice: n

index position: 0
nsuper
The Goal is: night

Choose insert, remove, replace or exit: remove

index position: 6
index out of range

index position: 5
nsupe
The Goal is: night

Choose insert, remove, replace or exit: replace

index position: 1

Letter choice: i
niupe
The Goal is: night

Choose insert, remove, replace or exit: replace

index position: 2

Letter choice: g
nigpe
The Goal is: night

Choose insert, remove, replace or exit: remove

index position: 4
nigp
The Goal is: night

Choose insert, remove, replace or exit: insert

Letter choice: h

index position: 3
nighp
The Goal is: night

Choose insert, remove, replace or exit: replace

index position: 4

Letter choice: t
night
The Goal is: night

Choose insert, remove, replace or exit: insert
Rasheed Hameed Congratulations! you have finished the game.
The game was finished in:  7 moves
'''    
  
   
    


            
                

        
            
         
        
   
        
            
