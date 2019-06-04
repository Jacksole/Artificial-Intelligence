from easyAI import AI_Player, Human_Player, TwoPlayersGame, id_solve
from easyAI.AI import TT


class LastCoin_game(TwoPlayersGame):
    def __init__(self, players):
        self.players = players
        self.nplayer = 1
        self.num_coins = 15
        self.max_coins = 4

    def possible_moves(self):
        return [str(a) for a in range(1, self.max_coins + 1)]

    def make_move(self, move):
        self.num_coins -= int(move)

    def win_game(self):
        return self.num_coins <= 0

    def is_over(self):
        return self.win()

    def score(self):
        return 100 if self.win_game() else 0

    def show(self):
        print(self.num_coins, 'coins left in the pile')


if __name__ == "__main__":
    tt: object = TT()
    LastCoin_game.ttentry = lambda self: self.num_coins
    r, d, m = id_solve(LastCoin_game,
                       range(2, 20), win_score=100, tt=tt)
    print(r, d, m)
    game = LastCoin_game([AI_Player(tt), Human_Player()])
    game.play()
