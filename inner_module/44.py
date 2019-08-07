import pickle


class GameState:
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0

state = GameState()
state.level += 1
state.lives -= 1

path = 'game_state.bin'
# with open(path, 'wb') as f:
#     pickle.dump(state, f)

with open(path, 'rb') as f:
    state_after = pickle.load(f)

print(state_after.__dict__)

print('=' * 100)

serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)