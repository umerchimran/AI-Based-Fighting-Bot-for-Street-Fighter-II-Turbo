from command import Command
import numpy as np
from buttons import Buttons
import csv
import os
import joblib
model = joblib.load("trained_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
# Only create the file once
if not os.path.exists("gameplay_data.csv"):
    with open("gameplay_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "X", "Y", "Command", "Left", "Right", "Up", "Down", "A", "B", "Y_btn", "L", "R"])

class Bot:

    def __init__(self):
        #< - v + < - v - v + > - > + Y
        self.fire_code=["<","!<","v+<","!v+!<","v","!v","v+>","!v+!>",">+Y","!>+!Y"]
        self.exe_code = 0
        self.start_fire=True
        self.remaining_code=[]
        self.my_command = Command()
        self.buttn= Buttons()

    # def fight(self,current_game_state,player):
    #     #python Videos\gamebot-competition-master\PythonAPI\controller.py 1
    #     if player=="1":
    #         #print("1")
    #         #v - < + v - < + B spinning

    #         if( self.exe_code!=0  ):
    #            self.run_command([],current_game_state.player1)
    #         diff=current_game_state.player2.x_coord - current_game_state.player1.x_coord
    #         if (  diff > 60 ) :
    #             toss=np.random.randint(3)
    #             if (toss==0):
    #                 #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player1)
    #                 self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
    #             elif ( toss==1 ):
    #                 self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player1)
    #             else: #fire
    #                 self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
    #         elif (  diff < -60 ) :
    #             toss=np.random.randint(3)
    #             if (toss==0):#spinning
    #                 #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player1)
    #                 self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
    #             elif ( toss==1):#
    #                 self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player1)
    #             else: #fire
    #                 self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
    #         else:
    #             toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
    #             if ( toss>=1 ):
    #                 if (diff>0):
    #                     self.run_command(["<","<","!<"],current_game_state.player1)
    #                 else:
    #                     self.run_command([">",">","!>"],current_game_state.player1)
    #             else:
    #                 self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player1)
    #         self.my_command.player_buttons=self.buttn

    #     elif player=="2":

    #         if( self.exe_code!=0  ):
    #            self.run_command([],current_game_state.player2)
    #         diff=current_game_state.player1.x_coord - current_game_state.player2.x_coord
    #         if (  diff > 60 ) :
    #             toss=np.random.randint(3)
    #             if (toss==0):
    #                 #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player2)
    #                 self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
    #             elif ( toss==1 ):
    #                 self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player2)
    #             else:
    #                 self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
    #         elif ( diff < -60 ) :
    #             toss=np.random.randint(3)
    #             if (toss==0):
    #                 #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player2)
    #                 self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
    #             elif ( toss==1):
    #                 self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player2)
    #             else:
    #                 self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
    #         else:
    #             toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
    #             if ( toss>=1 ):
    #                 if (diff<0):
    #                     self.run_command(["<","<","!<"],current_game_state.player2)
    #                 else:
    #                     self.run_command([">",">","!>"],current_game_state.player2)
    #             else:
    #                 self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player2)
    #         self.my_command.player2_buttons=self.buttn
    #     return self.my_command

    def fight(self, current_game_state, player):
        # Initialize the button object
        self.buttn = Buttons()

        if player == "1":
            # Player 1 logic
            if self.exe_code != 0:
                self.run_command([], current_game_state.player1)

            # Extract features for player 1
            player1 = current_game_state.player1
            features = np.array([[player1.x_coord, player1.y_coord,
                                int(player1.player_buttons.left), int(player1.player_buttons.right),
                                int(player1.player_buttons.up), int(player1.player_buttons.down),
                                int(player1.player_buttons.A), int(player1.player_buttons.B),
                                int(player1.player_buttons.Y), int(player1.player_buttons.L),
                                int(player1.player_buttons.R)]])

            # Predict the command using the model
            predicted_label = model.predict(features)
            command_str = label_encoder.inverse_transform(predicted_label)[0]

            # Translate the command string into button presses
            for action in command_str.split('+'):
                action = action.strip()
                if hasattr(self.buttn, action):  # Now checking without lowercase
                    setattr(self.buttn, action, True)

            self.my_command.player_buttons = self.buttn

        elif player == "2":
            # Player 2 logic
            if self.exe_code != 0:
                self.run_command([], current_game_state.player2)

            # Extract features for player 2
            player2 = current_game_state.player2
            features = np.array([[player2.x_coord, player2.y_coord,
                                int(player2.player_buttons.left), int(player2.player_buttons.right),
                                int(player2.player_buttons.up), int(player2.player_buttons.down),
                                int(player2.player_buttons.A), int(player2.player_buttons.B),
                                int(player2.player_buttons.Y), int(player2.player_buttons.L),
                                int(player2.player_buttons.R)]])

            # Predict the command using the model
            predicted_label = model.predict(features)
            command_str = label_encoder.inverse_transform(predicted_label)[0]

            # Translate the command string into button presses
            for action in command_str.split('+'):
                action = action.strip()
                if hasattr(self.buttn, action):  # Now checking without lowercase
                    setattr(self.buttn, action, True)

            self.my_command.player2_buttons = self.buttn

        return self.my_command




    def run_command( self , com , player   ):

        if self.exe_code-1==len(self.fire_code):
            self.exe_code=0
            self.start_fire=False
            print ("compelete")
            #exit()
            # print ( "left:",player.player_buttons.left )
            # print ( "right:",player.player_buttons.right )
            # print ( "up:",player.player_buttons.up )
            # print ( "down:",player.player_buttons.down )
            # print ( "Y:",player.player_buttons.Y )

        elif len(self.remaining_code)==0 :

            self.fire_code=com
            #self.my_command=Command()
            self.exe_code+=1

            self.remaining_code=self.fire_code[0:]

        else:
            self.exe_code+=1
            if self.remaining_code[0]=="v+<":
                self.buttn.down=True
                self.buttn.left=True
                print("v+<")
            elif self.remaining_code[0]=="!v+!<":
                self.buttn.down=False
                self.buttn.left=False
                print("!v+!<")
            elif self.remaining_code[0]=="v+>":
                self.buttn.down=True
                self.buttn.right=True
                print("v+>")
            elif self.remaining_code[0]=="!v+!>":
                self.buttn.down=False
                self.buttn.right=False
                print("!v+!>")

            elif self.remaining_code[0]==">+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.right=True
                print(">+Y")
            elif self.remaining_code[0]=="!>+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.right=False
                print("!>+!Y")

            elif self.remaining_code[0]=="<+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.left=True
                print("<+Y")
            elif self.remaining_code[0]=="!<+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.left=False
                print("!<+!Y")

            elif self.remaining_code[0]== ">+^+L" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print(">+^+L")
            elif self.remaining_code[0]== "!>+!^+!L" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.L= False #not (player.player_buttons.L)
                print("!>+!^+!L")

            elif self.remaining_code[0]== ">+^+Y" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print(">+^+Y")
            elif self.remaining_code[0]== "!>+!^+!Y" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.Y= False #not (player.player_buttons.L)
                print("!>+!^+!Y")


            elif self.remaining_code[0]== ">+^+R" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print(">+^+R")
            elif self.remaining_code[0]== "!>+!^+!R" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.R= False #ot (player.player_buttons.R)
                print("!>+!^+!R")

            elif self.remaining_code[0]== ">+^+A" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print(">+^+A")
            elif self.remaining_code[0]== "!>+!^+!A" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.A= False #not (player.player_buttons.A)
                print("!>+!^+!A")

            elif self.remaining_code[0]== ">+^+B" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print(">+^+B")
            elif self.remaining_code[0]== "!>+!^+!B" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.B= False #not (player.player_buttons.A)
                print("!>+!^+!B")

            elif self.remaining_code[0]== "<+^+L" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print("<+^+L")
            elif self.remaining_code[0]== "!<+!^+!L" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.L= False  #not (player.player_buttons.Y)
                print("!<+!^+!L")

            elif self.remaining_code[0]== "<+^+Y" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print("<+^+Y")
            elif self.remaining_code[0]== "!<+!^+!Y" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.Y= False  #not (player.player_buttons.Y)
                print("!<+!^+!Y")

            elif self.remaining_code[0]== "<+^+R" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print("<+^+R")
            elif self.remaining_code[0]== "!<+!^+!R" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!<+!^+!R")

            elif self.remaining_code[0]== "<+^+A" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print("<+^+A")
            elif self.remaining_code[0]== "!<+!^+!A" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.A= False  #not (player.player_buttons.Y)
                print("!<+!^+!A")

            elif self.remaining_code[0]== "<+^+B" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print("<+^+B")
            elif self.remaining_code[0]== "!<+!^+!B" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.B= False  #not (player.player_buttons.Y)
                print("!<+!^+!B")

            elif self.remaining_code[0]== "v+R" :
                self.buttn.down=True
                self.buttn.R= not (player.player_buttons.R)
                print("v+R")
            elif self.remaining_code[0]== "!v+!R" :
                self.buttn.down=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!v+!R")

            else:
                if self.remaining_code[0] =="v" :
                    self.buttn.down=True
                    print ( "down" )
                elif self.remaining_code[0] =="!v":
                    self.buttn.down=False
                    print ( "Not down" )
                elif self.remaining_code[0] =="<" :
                    print ( "left" )
                    self.buttn.left=True
                elif self.remaining_code[0] =="!<" :
                    print ( "Not left" )
                    self.buttn.left=False
                elif self.remaining_code[0] ==">" :
                    print ( "right" )
                    self.buttn.right=True
                elif self.remaining_code[0] =="!>" :
                    print ( "Not right" )
                    self.buttn.right=False

                elif self.remaining_code[0] =="^" :
                    print ( "up" )
                    self.buttn.up=True
                elif self.remaining_code[0] =="!^" :
                    print ( "Not up" )
                    self.buttn.up=False
            self.remaining_code=self.remaining_code[1:]
            with open("gameplay_data.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    player.player_id if hasattr(player, "player_id") else "Unknown",
                    player.x_coord,
                    player.y_coord,
                    self.remaining_code[0] if self.remaining_code else "None",
                    int(self.buttn.left),
                    int(self.buttn.right),
                    int(self.buttn.up),
                    int(self.buttn.down),
                    int(self.buttn.A),
                    int(self.buttn.B),
                    int(self.buttn.Y),
                    int(self.buttn.L),
                    int(self.buttn.R),
                ])

        return
