#include <iosteam>
using namespace std;
/**************************************************************
*   Tic Tac Toe
*   By Dane Selch   DATE: 2/7/23
*   Not for sale or distribution, 
*   Purpose: This program was made to help me practice using C++ 
**************************************************************/


    /****
    *Challange three circle version (4player version) 
    **********/
int main() {
    game Toe;
            //cout << "How many players do you have?";
            // cin >> playerCount;
    cout << "Welcome to my Tic-Tac-Toe game"; 
    play(Toe);
    cout << "thanks for playing";
    return 0;
}

/*********************
*getPlayerInput
* inputs: none
* output: in
* purpose; a generic function that can be called whenever 
*       the player needs to take an action
*********************/
char getPlayerInput(){
    char in
    cout << "input:  ";
    cin >> in;
    return in;
}

/********************
* play
*   inputs: none
*   purpose: keep the game running until players are done.
*********************/            
void play(game Toe){
            char in;
            do(){
            Toe.display();
                cout << "please slect an option (type the single letter and press enter)\n";
    cout << "q: quit     r: ready for your turn      t: see who's turn it is. ";
            in =  getPlayerInput();
            switch(in){
                case "q":  
                    Toe.endGame();
                    break;
                case "r":
                    Toe.takeTurn();
                    break;
                case "t":
                    Toe.getTurn();
                    break;
                default:
                    cout << "sorry that is not a valid option, try again.";
                }
                // after every action see if the game has been won.
                Toe.checkWin();
            }
            while(Toe.end_game == false);
        }
