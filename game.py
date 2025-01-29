def main():
    main_list = start()
    direction=input("Enter up, down, left, right!")
    if direction == "up":
        upfunc(main_list)
    elif direction=="down":
        downfunc(main_list)
    elif direction == "left":
        leftfunc(main_list)
    elif direction == "right":
        rightfunc(main_list)

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
    for i in startlist :
        print(i)
    return startlist

def upfunc(main_list):
    for i in range(4):
        for j in range(1 ,4):
            if main_list[j][i] != 0:
                for k in range(j-1, -1 , -1):
                    if main_list [k][i] == 0 or main_list [K+1][i]:
                        main_list[k][i]+= main_list[k+1][i]
                        main_list[k+1][i]= 0 
    for i in main_list:
        print(i)
        
def downfunc(main_list):
    for i in range(4):
         for j in range(2 ,-1 ,-1):
            if main_list [j][i]:
                for k in range(j+1 ,4):
                    if main_list [k][i] == 0 or main_list[k][i] ==main_list [k-1][i]:
                         main_list[k][i] += main_list [k-1][i]
                         main_list[k-1][i] =0
    for i in main_list:
        print(i)


def rightfunc(main_list):
    for j in range(4):
        for i in range (2, -1, -1):
            for k in range(i+1, 4):
                if main_list[j][k]== 0 or main_list[j][k-1]== main_list[j][k]:
                    main_list[j][k] +=main_list [j][k-1]
                    main_list[j][k-1]= 0
for i in main_list:
    print(i)
                
def leftfunc(main_list):
    for j in range(4):
        for i in range(1 , 4):
        #main_list[j][i]
            for k in range(i-1 ,-1, -1):
                if main_list[j][k] ==0 or main_list[j][k+1] == main_list [j][k]:
                    main_list[j][k] += main_list[j][k+1]
                    main_list[j][k+1] =0 
    for i in main_list:
        print(i)



main()
