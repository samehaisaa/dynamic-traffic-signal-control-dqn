import gym
from gym import spaces
import numpy as np
import random

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()

        # Action space: 2 actions, e.g., 0: red, 1: green
        self.action_space = spaces.Discrete(2)

        # Observation space: Number of vehicles at each intersection
        self.observation_space = spaces.Box(low=0, high=10, shape=(2,), dtype=np.int)

        # Initialize state
        self.state = np.array([random.randint(0, 10), random.randint(0, 10)])  # Two lanes with random vehicles

        # Reward weight
        self.reward_weight = 1.0

    def reset(self):
        # Reset state to random
        self.state = np.array([random.randint(0, 10), random.randint(0, 10)])
        return self.state

    def step(self, action):
        # Take action (0: red, 1: green)
        if action == 1:
            # Green light: reduce traffic on the current lane
            self.state[0] = max(0, self.state[0] - 1)  # Reduce one vehicle
        else:
            # Red light: increase traffic on the current lane
            self.state[0] = min(10, self.state[0] + 1)

        # Reward: Reduce traffic, penalty for too many vehicles
        reward = -self.state[0] + self.reward_weight * (10 - self.state[1])

        # Check if done
        done = bool(self.state[0] >= 10)

        return self.state, reward, done, {}

    def render(self):
        # Simple render of traffic light status
        print(f"Traffic: Lane 1 = {self.state[0]} vehicles, Lane 2 = {self.state[1]} vehicles")
