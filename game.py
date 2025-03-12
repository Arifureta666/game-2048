def main():
    main_list = start()
    temp=zero(main_list)
    while temp :
        for i in main_list:
            print(i)
        
        direction=input("Enter up, down, left, right!")
        if direction == "up":
            upfunc(main_list)
        elif direction=="down":
            downfunc(main_list)
        elif direction == "left":
            leftfunc(main_list)
        elif direction == "right":
            rightfunc(main_list)
        temp =zero(main_list)
        if temp:
            plus_two(main_list)
    for i in main_list:
        print("GAME OVER")
def start(): 
    import random 
    startlist = [[0 for i in range (4)]for j in range(4)]
    e1i1=random.randint(0,3)    
    e1i2=random.randint(0,3)  
    e2i1=random.randint(0,3)  
    e2i2=random.randint(0,3)
    
    while e1i1==e2i1 and e1i2==e2i2 :
        e2i1=random.randint(0,3)  
        e2i2=random.randint(0,3)  
        
    startlist [e1i1][e1i2]=2
    startlist [e2i1][e2i2]=2
    
    print("the gamehas been started")
    return startlist

def upfunc(main_list):
    ban_list=[]
    for i in range(4):
        for j in range(1 ,4):
            if main_list[j][i] != 0:
                for k in range(j-1, -1 , -1):
                    if main_list [k][i] == 0:
                        main_list[k][i]+= main_list[k+1][i]
                        main_list[k+1][i]= 0 
                    elif main_list[k][i]==main_list[k+1][i] and [k,i] not in ban_list and [k+1,i] not in ban_list:
                        main_list[k][i]+= main_list[k+1][i]
                        main_list[k+1][i]= 0 
                        ban_list.append([k,i])
                        
        
def downfunc(main_list):
    ban_list=list()
    for i in range(4):
         for j in range(2 ,-1 ,-1):
            if main_list [j][i]:
                for k in range(j+1 ,4):
                    if main_list [k][i] == 0:
                         main_list[k][i] += main_list [k-1][i]
                         main_list[k-1][i] =0
                    elif main_list[k][i]==main_list[k-1][i] and [k,i] not in ban_list and [k-1,i] not in ban_list:
                        main_list[k][i] += main_list [k-1][i]
                        main_list[k-1][i] =0
                        ban_list.append([k,i])
                        

def rightfunc(main_list):
    ban_list = list()
    for j in range(4):
        for i in range (2, -1, -1):
            for k in range(i+1, 4):
                if main_list[j][k]== 0:
                    main_list[j][k] +=main_list [j][k-1]
                    main_list[j][k-1]= 0
                elif main_list[j][k]==main_list[j][k-1] and [j,k] not in ban_list and [j,k-1] not in ban_list:
                    main_list[j][k] +=main_list [j][k-1]
                    main_list[j][k-1]= 0
                    ban_list.append([j,k])
                    

                
def leftfunc(main_list):
    ban_list=list()
    for j in range(4):
        for i in range(1 , 4):
        #main_list[j][i]
            for k in range(i-1 ,-1, -1):
                if main_list[j][k] ==0:
                    main_list[j][k] += main_list[j][k+1]
                    main_list[j][k+1] =0 
                elif main_list[j][k]== main_list [j][k+1] and [j,k] not in ban_list and [j,k+1] not in ban_list:
                    main_list[j][k] += main_list[j][k+1]
                    main_list[j][k+1] =0 
                    ban_list.append([j,k])
                    
def zero(main_list):
    for i in range(4): 
        for j in range(4):
            if main_list[i][j] ==0:
                return True
    return False
 
def plus_two(main_list):
    count= 0 
    for i in range (len(main_list)):
        for j in range (len(main_list[i])):
            if main_list[i][j]==0:
                count+=1 
    import random
    temp = random.randint(1 , count)
    count = 0
    for i in range (len(main_list)):
        for j in range (len(main_list[i])):
            if main_list[i][j]==0: 
                count+=1 
                if count == temp:
                    main_list[i][j]=2
                
                
            
main()
