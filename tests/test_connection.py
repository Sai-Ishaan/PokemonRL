### Test connection to Pokemon Showdown server

import asyncio
from poke_env.player import RandomPlayer

# Coroutine 
async def main():
    #Creating 2 random players
    p1 = RandomPlayer(battle_format="gen8randombattle")
    p2 = RandomPlayer(battle_format="gen8randombattle")
    
    #5 matches between p1 and p2
    await p1.battle_against(p2, n_battles=5) 
    print(f"Player 1 won {p1.n_won_battles} battles")
    print(f"Player 2 won {p2.n_won_battles} battles")
    
if __name__ == "__main__":
    asyncio.run(main())    