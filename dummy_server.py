from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
players = {}

def create_player(player_id):
    if player_id not in players:
        players[player_id] = {"coins": 1000, "diamonds": 50, "games_played": 0, "wins": 0}

@app.route('/add_coins', methods=['POST'])
def add_coins():
    data = request.json
    player_id = data.get("player_id")
    amount = data.get("amount")
    create_player(player_id)
    players[player_id]["coins"] += amount
    return jsonify({"message": f"Added {amount} coins to {player_id}", "player": players[player_id]})

@app.route('/simulate_win', methods=['POST'])
def simulate_win():
    data = request.json
    player_id = data.get("player_id")
    create_player(player_id)
    players[player_id]["games_played"] += 1
    players[player_id]["wins"] += 1
    return jsonify({"message": f"Simulated win for {player_id}", "player": players[player_id]})

@app.route('/live_board', methods=['GET'])
def live_board():
    player_id = request.args.get("player_id")
    create_player(player_id)
    return jsonify({"message": "Live board data", "player": players[player_id], "board": "This is a mock live board"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
