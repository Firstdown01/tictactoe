board=[i for i in range(0,10)]
print(board[1])
f,p=1,1
def check(n):
    return (board[n]=='X' or board[n]=='O')
def chewin():
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
       return 1   
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        return 1    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        return 1    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        return 1  
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        return 1    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        return 1   
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        return 1   
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        return 1    
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
       return 0    
       
def display():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ") 
while f==1:
    display()
    if(p%2!=0):
        n=int(input(("enter number")))
        if(not check(n)):
            board[n]='X'
            print("marked")
            
            # 
        else:
            print("pick another")
            p=p-1
        
            
    if(p%2==0):
        n=int(input(("enter number")))
        if(not check(n)):
            board[n]='O'
            print("marked")
            # if(chewin()):
            #     print("player 2 wins")
        else:
            print("pick another")
            p=p-1
    if(chewin()):
        print("player %c wins",p%2)
        f=0
    p=p+1  
    if(p==10):
        f=0
print(board) 
    

