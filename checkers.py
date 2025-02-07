box = [['__' for _ in range(8)] for _ in range(8)]
white = 12
black = 12
change = "w"
q_change = "qw"
n = 1

def boxes(i):
    if i%2 == 0:
        return False
    else:
        return True

# Default White Coin 
for i in range(0,3):
    flag = boxes(i)
    for j in range(0,8):
        if flag == True:
            box[i][j] = "w"+str(n)
            n += 1
            flag = False
        else:
            flag = True
      
n = 1      
# Default Black Coin 
for i in range(5,8):
    flag = boxes(i)
    for j in range(0,8):
        if flag == True:
            box[i][j] = "b"+str(n)
            n += 1
            flag = False
        else:
            flag = True
    
for row in box:
    print(' '.join(row))
    
# checking black coin positions:
def black_coin(row,col,temp_ch):
    temp_pre = ""
    temp_post = ""
    if row-1>=0 and col-1>=0:
        temp_pre = box[row-1][col-1]
        if temp_pre == "__":
            print(f"{temp_ch} : {row-1} {col-1}")
        else:
            if row-2 >= 0 and col-2 >= 0:
                if temp_ch[:2] == "qw":
                    if temp_pre[0] == "b" or temp_pre[:2] == "qb":
                        if box[row-2][col-2] == "__":
                            print(f"{temp_ch} : {row-2} {col-2}")
                else: 
                    if temp_pre[0] != "b" and temp_pre[:2] != "qb":
                        if box[row-2][col-2] == "__":
                            print(f"{temp_ch} : {row-2} {col-2}")
                    
    if row-1>=0 and col+1<=7:
        temp_post = box[row-1][col+1]
        if box[row-1][col+1] == "__":
            print(f"{temp_ch} : {row-1} {col+1}")
        else:
            if row-2 >= 0 and col+2 <= 7:
                if temp_ch[:2] == "qw":
                    if temp_post[0] == "b" or temp_post[:2] == "qb":
                        if box[row-2][col+2] == "__":
                            print(f"{temp_ch} : {row-2} {col+2}")
                else:
                    if temp_post[0] != "b" and temp_post[:2] != "qb":
                        if box[row-2][col+2] == "__":
                            print(f"{temp_ch} : {row-2} {col+2}")

# checking white coin positions:
def white_coin(row,col,temp_ch):
    temp_pre = "__"
    temp_post = "__"
    if row+1<=7 and col+1<=7:
        temp_post = box[row+1][col+1]
        if temp_post == "__":
            print(f"{temp_ch} : {row+1} {col+1}")
        else:
            if row+2 <= 7 and col+2 <= 7:
                if temp_ch[:2] == "qb":
                    if temp_post[0] == "w" or temp_post[:2] == "qw":
                        if box[row+2][col+2] == "__":
                            print(f"{temp_ch} : {row+2} {col+2}")
                else:
                    if temp_post[0] != "w" or temp_post[:2] != "qw":
                        if box[row+2][col+2] == "__":
                            print(f"{temp_ch} : {row+2} {col+2}")
                    
    if row+1<=7 and col-1>=0:
        temp_pre = box[row+1][col-1]
        if box[row+1][col-1] == "__":
            print(f"{temp_ch} : {row+1} {col-1}")
        else:
            if row+2<=7 and col-2 >= 0:
                if temp_ch[:2] == "qb":
                    if temp_pre[0] == "w" or temp_pre[:2] == "qw":
                        if box[row+2][col-2] == "__":
                            print(f"{temp_ch} : {row+2} {col-2}")
                else:
                    if temp_pre[0] != "w" and temp_pre[:2] != "qw":
                        if box[row+2][col-2] == "__":
                            print(f"{temp_ch} : {row+2} {col-2}")
    
# Available Spaces
def available_space(row,col,temp_ch):
    temp = temp_ch[0]
    if temp == "b":
        black_coin(row,col,temp_ch)
    else:
        white_coin(row,col,temp_ch) 
            
# changing black coin
def change_black(x,y,p,q,user_coin):
    global count_2
    box[p][q] = "__"
    if y>q and p-1>=0:
        if y == q+1:
            box[x][y]=user_coin
        elif y == q+2:
            box[p-1][q+1] = "__"
            box[x][y]=user_coin
    else:
        if y==q-1 and p-1>=0:
            box[x][y]=user_coin
        elif y==q-2:
            box[p-1][q-1] = "__"
            box[x][y]=user_coin
            
    if x == 0 and user_coin[0] == "b":
        box[x][y] = "qb"+str(count_2)
        count_2 += 1
        
# changing white coin
def change_white(x,y,p,q,user_coin):
    global count_1
    box[p][q] = "__"
    if y<q and p+1<=7:
        if y == q-1:
            box[x][y]=user_coin
        elif y == q-2:
            box[p+1][q-1] = "__"
            box[x][y]=user_coin
    else:
        if y==q+1 and p+1<=7:
            box[x][y]=user_coin
        elif y==q+2:
            box[p+1][q+1] = "__"
            box[x][y]=user_coin
            
    if x == 7 and user_coin[0] == "w":
        box[x][y] = "qw"+str(count_1)
        count_1 += 1
                
                
count_1 = 1
count_2 = 1
# Changing the Coin
while(white != 0 and black != 0):
    if change == "w":
        change = "b"
        q_change = "qb"
    else:
        change = "w"
        q_change = "qw"
        
    print("Choose The coin And Position : ")
    i=0
    j=0
    for i in range(0,8):
        flag = boxes(i)
        for j in range(0,8):
            if flag == True:
                check = box[i][j]
                q_check = box[i][j]
                
                if change == check[0]:
                    available_space(i,j,check)
                elif q_change == q_check[:2]:
                    black_coin(i,j,q_check)
                    white_coin(i,j,q_check)            
                flag = False
            else:
                flag = True
                
    user_coin = input("Enter The Coin : ")
    user_place = int(input("Enter The Position : "))
    b = user_place % 10
    user_place = int(user_place/10)
    a = user_place % 10
    
    
    # Changing the Coin
    no_check = True
    for i in range(0,8):
        flag = boxes(i)
        if no_check == True:
            for j in range(0,8):
                if flag == True:
                    if box[i][j] == user_coin:
                        if "b" == user_coin[0]:
                            change_black(a,b,i,j,user_coin)
                            no_check = False
                            break
                        elif "w" == user_coin[0]:
                            change_white(a,b,i,j,user_coin)
                            no_check = False
                            break
                        else:
                            change_black(a,b,i,j,user_coin)
                            change_white(a,b,i,j,user_coin)
                            no_check = False
                            break
                    flag = False
                else:
                    flag = True
        else:
            break
                
    for row in box:
        print(' '.join(row))
    
    white = 0
    black = 0
    
    # count white coins
    for i in range(0,8):
        flag = boxes(i)
        for j in range(0,8):
            if flag == True:
                if "w" in box[i][j] or "qw" in box[i][j]:
                    white += 1
                flag = False
            else:
                flag = True
                
    # count black coins
    for i in range(0,8):
        flag = boxes(i)
        for j in range(0,8):
            if flag == True:
                if "b" in box[i][j] or "qb" in box[i][j]:
                    black += 1
                flag = False
            else:
                flag = True
                
    print(f"white is : {white}")
    print(f"black is : {black}")
                       
if white == 0:
    print("Black Wins")
else:
    print("White Wins")
    