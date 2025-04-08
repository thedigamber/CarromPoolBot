import time

# Mock database
players = {}
games = {}

def create_player(player_id):
    players[player_id] = {"coins": 1000, "diamonds": 50, "games_played": 0, "wins": 0}

def get_player_info(player_id):
    if player_id not in players:
        create_player(player_id)
    return players[player_id]

def send_coins(player_id, amount):
    if player_id not in players:
        create_player(player_id)
    players[player_id]["coins"] += amount
    time.sleep(1)  # Simulate server processing time
    return f"Sent {amount} coins to {player_id}"

def send_diamonds(player_id, amount):
    if player_id not in players:
        create_player(player_id)
    players[player_id]["diamonds"] += amount
    time.sleep(1)  # Simulate server processing time
    return f"Sent {amount} diamonds to {player_id}"

def auto_play_match(player_id):
    if player_id not in players:
        create_player(player_id)
    players[player_id]["games_played"] += 1
    players[player_id]["wins"] += 1
    time.sleep(2)  # Simulate server processing time
    return f"Auto-played match for {player_id} and won"

def start_game(player_id):
    game_id = len(games) + 1
    games[game_id] = {"state": "started", "player_id": player_id}
    return games[game_id]

def join_game(player_id):
    game_id = len(games) + 1
    games[game_id] = {"state": "joined", "player_id": player_id}
    return games[game_id]
