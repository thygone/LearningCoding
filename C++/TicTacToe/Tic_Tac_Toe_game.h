#include <iostream>
#include <string>
#include "Player_TTToe.h"
using namespace std;

        /*
        winning patterns
        same size:
            3 in a line
                a. horizontal,
                b. vertical,
                c. diagnal
        differnt sizes
            1. Small, Med, Large in a line,
                a. horizontal,
                b. vertical,
                c. diagnal
            2. same size in a line,
                a. horizontal,
                b. vertical,
                c. diagnal
            3. small, med, large all in one spot 
        */


class game{
    private:
        //variables    
        bool end_game = false; // signal to end the game
        int turn_counter = 0;
        int player_count = 0;
        bool CATS = false; // used for case of a tie
    public:
        bool tplayers[]; // keeps track of who's turn it is
        Player players[]; // array of players.
        int board[];// an array to hold each place on the board
        
        
            
        
        
        //constructor
        game(){
            board[9] = {
                0, 0, 0,
                0, 0, 0,
                0, 0, 0
                };
                // each player represented as a T/F on if they have won the game or not
            players[2] = { 
                false, false
                };
            tplayers[4] = {
                true,false,false,false
            };
                
        }
        game(int X){
           //3-4 player version???
            player_count = X
            board[9] = {
                // each spot has 3 circles, small, medium, and big that can go there. total of 27 positions on the 3x3 board 
                {0,0,0}, {0,0,0}, {0,0,0},
                {0,0,0}, {0,0,0}, {0,0,0},
                {0,0,0}, {0,0,0}, {0,0,0}}; 
            if (x==2){
                players[2] = {
                    false,false
                };
            }
            else if(x == 3){
                players[3] = {
                    false,false,
                    false
                };
            }
            else if(x==4){
                players[4]{
                    false,false,
                    false,false
                };
            }
            else {
                cout << "error invalid number, try to play another time";
                endGame()
            }
            }
        
        // METHODS
        //masCabe2018(VCM)
        /*********************
        * getPlayerInput
        * inputs: none
        * output: none
        * purpose: This function will help keep track of  
        *       who's turn it is
        *********************/
        void passTurn(){
            // up to 4 players 
            switch(turnCounter % player_count){
                case 0:
                    tplayers[0].turn = false;
                    tplayers[1].turn = true;
                    tplayers[2].turn = false;
                    tplayers[3].turn = false;
                    break;
                case 1:
                    tplayers[0].turn = true;
                    tplayers[1].turn = false;
                    tplayers[2].turn = false;
                    tplayers[3].turn = false;
                    break;
                case 2:
                    tplayers[0].turn = false;
                    tplayers[1].turn = false;
                    tplayers[2].turn = true;
                    tplayers[3].turn = false;
                    break;
                case 3: 
                    tplayers[0].turn = false;
                    tplayers[1].turn = false;
                    tplayers[2].turn = false;
                    tplayers[3].turn = true;
                    break;
                default:
                    tplayers[0].turn = true;
                    tplayers[1].turn = false;
                    tplayers[2].turn = false;
                    tplayers[3].turn = false;
            }
            // incrament to next turn in play
            self.turn_counter +=1
        }

    
        /*********************
        * checkSpot
        *   input: position wanted [point], and player wanting it [P]
        *   purpose: to check if a move is valid for the player.
        **********************/
        void checkSpot( int point, int P ){ 
            
            if (board[point] != 0){
                cout << "that spot is already taken by Player " << (point+1) <<" \n";
                            }
            else{
                takeSpot(board[point], P);
            }
        }
        /*********************
        * getPoint
        * inputs: row, column
        * output: int
        * purpose: converts the coordinant into an 
        * index for the board
        *********************/
        int getPoint(char R, int C){
            int x;
            if (R =='A'){
                x = 0;
            }else if ( R == 'B'){
                x = 3;
            }else if(R == 'C'){
                x = 6;
            }
            return x + C - 1;
        }

        /*********************
        * takeTurn
        * inputs: player
        * output: none
        * purpose: get the position the player wants
        *********************/
        char takeTurn(int player){
            char row;
            int column;
            cout << "please choose a row (A,B,C)";
            cin >> row;
            cout << "please choose a column (1,2,3)";
            cin >> column;
            return checkSpot(getPoint(row,column),player);
        }

        /*********************
        * checkVertical
        * inputs: position
        * output: boolin
        * purpose: if all the positions in the column are the same end game
        *********************/
        void checkVertical(int point,){
            int player;
            if (board[point] != 0){
                player = board[point]-1; // the # at the index indicates the index for the player (offset by 1)
                if (board[point] == board[point+3] == board[point+6]){
                    players[player] = true;
                }
            }
        }
        
        /*********************
        * checkHorizontal
        * inputs: position
        * output: none
        * purpose: if all the positions in the row are the same, will set player to true
        *********************/
        void checkHorizontal(int point){
            int player;
            if (board[point] != 0){
                player = board[point]-1; // the # at the index indicates the index for the player (offset by 1)
                if (board[point] == board[point+1] == board[point+]){
                    players[player] = true;
                }
            }
        }
        /*********************
        * checkDiagnal
        * inputs: none
        * output: boolin
        * purpose: if all the positions in the diagnal are the same end game
        *********************/
        checkDiagnal(){
            int player;
            if (board[0] != 0){
                player = board[0]-1; // the # at the index indicates the index for the player (offset by 1)
                if (board[0] == board[4] == board[8]){
                        players[player] = true;
            }else if (board[6]){
                player = board[6]-1; // the # at the index indicates the index for the player (offset by 1)
                if(board[6] == board[4] == board[2])
                       players[player] = true;
                }
            }}
        /*********************
        * checkWin
        * inputs: none
        * output: none
        * purpose: This is called after every turn to check if the game ends.
        *********************/
        void checkWin(){
            //check first row and column
            checkVertical(0);
            checkHorizontal(0);
            // check 2nd row and column
            checkVertical(1); 
            checkHorizontal(3);
            //check last row and column
            checkVertical(2);
            checkHorizontal(6);
            //check diagnals
            checkDiagnal();
            for (int i = 0; i < player_count.size(); i++){
                if (players[i] == true)
                cout << "player " << (i + 1) << "WINS!!\n";
                endGame()
            }
        }


        /*********************
        * endGame
        * inputs: none
        * output: none
        * purpose: sets game_end to true and thus ends the program
        *********************/
        void endGame(){
            end_game = true;
        }

        /*********************
        *display
        * inputs: none
        * output: none
        * purpose: shows the board to the players
        *********************/
        void display(int board[9]){
         
            for (int i = 0; i < 9; i++){
                if (i % 3 == 0){
                    cout << "\n    " << row;
                }
                cout << i;
                if (board[i] == 0){
                    cout << "|___|";
                }else if (board[i] == 1){
                    cout << "|_O_|";
                }else if (board[i] == 2){
                    cout << "|_X_|";
                }   
            }      
        }
}