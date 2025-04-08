import random
import backend

def start_game(player_id):
    return backend.start_game(player_id)

def join_game(player_id):
    return backend.join_game(player_id)

def simulate_strike(player_id, direction, power):
    result = random.choices(["miss", "hit"], weights=[0.7, 0.3])[0]
    return result
