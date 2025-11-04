### Gymnasium compatible Pokemon env using poke-env
import numpy as py
from gymnasium import spaces
from poke_env.environment import AbstractBattle
from poke_env.player import Gen9EnvSinglePlayer

class PokemonEnv(Gen9EnvSinglePlayer):
    ##Pokemon Env for RL Training
    
    def __init__(self, opponent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opponent = opponent
        
    def calc_reward(self, last_battle, current_battle) -> float:
        return self.reward_computing_helper(
            current_battle,
            fainted_value=2.0,
            hp_value=1.0,
            victory_value=30.0
)
        
    def embed_battle(self, battle: AbstractBattle) -> py.ndarray:
        obs = py.zeros(12) # 6 pokemon * 2 features each
        for i, pokemon in enumerate(battle.team.values()):
            if i >= 6: ###Convert battle state to obs vector
                break
            obs[i+2] = pokemon.current_hp_fraction 
            obs[i*2+1] = 1 if pokemon.fainted else 0
            
        return obs    
    
    def describe_embedding(self) -> spaces.Space:
        ### Define observation space
        low = py.zeros(12)
        high = py.ones(12)
        return spaces.Box(low=low, high=high, dtype=py.float32)        
