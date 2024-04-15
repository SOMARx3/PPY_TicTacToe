from game import TicTacToe
import json

from tic_tac_toe.Gui import Gui

# Function to read game initialization data from game-init.json
def read_game_init():
    with open('game-init.json', 'r') as file:
        game_init_data = json.load(file)
    return game_init_data


# def start_game():
#     gui = Gui(grid_size)
#     gui.render(game.current_player + " turn")
#
#     gui.board[gui.selected_row][gui.selected_column] = game.player_symbols[game.current_player]
#     result, winner, winning_cells = game.make_move(gui.selected_row, gui.selected_column)
#
#     gui.render(game.current_player + " turn")
#
#     print(result)
#     print(winner)
#     print(winning_cells)

# Read game initialization data
game_init_data = read_game_init()
num_players = game_init_data['num_players']
player_names = game_init_data['player_names']
grid_size = game_init_data['grid_size']
player_symbols = game_init_data.get('player_symbols', None)  # Get player symbols from game-init.json, if available
game = TicTacToe(num_players, player_names, grid_size, player_symbols)  # Initialize the game with player symbols

# start_game()
