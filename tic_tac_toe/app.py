import time
import keyboard
from pynput.keyboard import Key
from game import TicTacToe
import json

from Gui import Gui

# Function to read game initialization data from game-init.json
def read_game_init():
    with open('game-init.json', 'r') as file:
        game_init_data = json.load(file)
    return game_init_data


def start_game():
    gui = Gui(grid_size)
    gui.render(game.current_player + " turn")

    while True:
        time.sleep(0.1)

        match keyboard.read_key():
            case "left":
                if gui.selected_row > 0:
                    gui.selected_row -= 1
            case "right":
                if gui.selected_row < grid_size - 1:
                    gui.selected_row += 1
            case "up":
                if gui.selected_column > 0:
                    gui.selected_column -= 1
            case "down":
                if gui.selected_column < grid_size - 1:
                    gui.selected_column += 1
            case "enter":
                process_move(gui)
                continue
            case 12:
                exit(0)
            case _:
                continue

        gui.render(game.current_player + " turn")


def process_move(gui):
    player_symbol = game.player_symbols[game.current_player]
    result, winner, winning_cells = game.make_move(gui.selected_row, gui.selected_column)

    match(result):
        case "occupied":
            gui.render(game.current_player + " turn")
            print('cell is occupied')
        case "success":
            gui.board[gui.selected_column][gui.selected_row] = player_symbol
            gui.render(game.current_player + " turn")
        case "win":
            for i in winning_cells:
                gui.board[i[1]][i[0]] = "w"

            gui.render("player: " + winner + " won")
            exit(0)
        case "draw":
            gui.render(game.current_player + " turn")
            gui.render("draw")
            exit(0)


# Read game initialization data
game_init_data = read_game_init()
num_players = game_init_data['num_players']
player_names = game_init_data['player_names']
grid_size = game_init_data['grid_size']
player_symbols = game_init_data.get('player_symbols', None)  # Get player symbols from game-init.json, if available
game = TicTacToe(num_players, player_names, grid_size, player_symbols)  # Initialize the game with player symbols

start_game()
