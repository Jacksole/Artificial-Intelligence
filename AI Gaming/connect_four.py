from easyAI.games import ConnectFour
from easyAI import Human_Player, AI_Player, Negamax

ai = Negamax(7) # AI thinks 7 moves in advance
game = ConnectFour( [ AI_Player(ai), Human_Player() ])
game.play()