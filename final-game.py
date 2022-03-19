board =  [ "1", "2", "3","4","5","6","7","8","9","10","11","12","13","14","15","16" ]
player = 1
endGame = False

def PrintBoard():
    print("---------------------------------")
    print("|   " + board[0] +  "   |   " + board[1] + 
            "   |   " + board[2] +  "   |   " + board[3] + "   |" )
    print ( "|   " + board[4] + "   |   " + board[5]
            + "   |   " + board[6] + "   |   " + board[7] + "   |" )
    print("|   " + board[8] +  "   |   " + board[9] + 
            "  |   " + board[10] +  "  |   " + board[11] + "  |" )
    print( "|   " + board[12] + "  |   " + board[13]
            + "  |   " + board[14] + "  |   " + board[15] + "  |" ) 
    print("---------------------------------")    


def Action( action1, action2):
    global player
    global endGame
    if board[action1 - 1] != "x" and  board[action2 - 1] != "x" :
        if abs((action2 - action1)) == 4 or abs((action2 - action1)) == 1 :
            if action1 == 4 and action2 == 5 or action1 == 8 and action2 == 9  or action1 == 12 and action2 == 13  or action2 == 4 and action1 == 5 or action2 == 8 and action1 == 9 or action2 == 12 and action1 == 13 :
                print ("			player " + str(player) + " you can't play here " )
                PrintBoard()
                return

            if action1 > 9:
                board[action1 - 1] = "x "
            else :
                board[action1 - 1] = "x"
            if action2 > 9: 
                board[action2 - 1] = "x "
            else :
                board[action2 - 1] = "x"

            turns = 0
            draw = True
            for  i in range(16) :
                
                if board[i].strip() != "x" :
                    draw = False
                    if (i) != 3 and (i) != 7 and (i) != 11 :
                        if (i + 1) < 16 and board[i + 1].strip() != "x" :
                            turns += 1
                            break

                        
                    if (i) != 4 and (i) != 8 and (i) != 12 :
                        if (i - 1) >= 0 and board[i - 1].strip() != "x" :
                            turns+=1
                            break
                    
                    if (i - 4) >= 0 and board[i - 4].strip() != "x" :
                        turns+=1
                        break

                    if (i + 4) < 16 and board[i + 4].strip() != "x":
                        turns+=1
                        break

            if draw == True:
                print("                                 No one WIN the game")
                endGame = True
                return
                
            if turns != 0:
                PrintBoard()
                if player == 1:  player = 2
                else: player = 1
                
            else: 
                PrintBoard()
                print ( "player: " + str(player) + " win the game !!" )
                endGame = True
        else:
            print("you can't play here!")
    else:
        print("you can't play here")
    
PrintBoard()
while (1) :

    if endGame: 
       newGame  = input("To make new game click :'n' - to quit click 'q' ")
       if newGame == "n":
            board= [ "1", "2", "3","4","5","6","7","8","9","10","11","12","13","14","15","16" ]
            endGame = False
            PrintBoard()

       if newGame == "q": break
       else: continue
        
          

    print ( "player : " + str(player) + " Choose two numbers" )
    
    action1 = int(input("The first number is : "))
    action2 = int(input("The second number is : "))
    
    if action1 > 16 or action2 > 16 :
        print("                           ERROR:   choose from 1 to 16")
        PrintBoard()
        continue

    Action(action1,action2)
