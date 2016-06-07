import argparse
from tetris.game import Game

from tetris.players import AI


def start(weights=None):
    player = AI(weights)
    game = Game(player)
    game.new_game()
    game.start_ticking()
    game.run_game()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('initial_weights', metavar='w', type=int, nargs='*',
                        help='integers for the initial weights')
    args = parser.parse_args()
    start(weights=args.initial_weights)
