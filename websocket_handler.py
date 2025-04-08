import asyncio

async def sync_game_state(game_state):
    while True:
        await asyncio.sleep(1)  # Simulate real-time sync delay
        print(f"Syncing game state: {game_state}")
