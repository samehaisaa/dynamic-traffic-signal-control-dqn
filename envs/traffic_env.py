import gym
from gym import spaces
import numpy as np
import random
import pygame
from pygame.locals import *

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()

        # Action space: 2 actions, 0: red, 1: green
        self.action_space = spaces.Discrete(2)

        # Observation space: Number of vehicles at each intersection (e.g., 2 intersections)
        self.observation_space = spaces.Box(low=0, high=10, shape=(2,), dtype=np.int)

        # Initialize state (random number of vehicles in each lane)
        self.state = np.array([random.randint(0, 10), random.randint(0, 10)])

        # Reward weight
        self.reward_weight = 1.0

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Traffic Signal Control")
        self.font = pygame.font.SysFont("Arial", 24)

    def reset(self):
        # Reset state to random
        self.state = np.array([random.randint(0, 10), random.randint(0, 10)])
        return self.state

    def step(self, action):
        # Take action (0: red, 1: green)
        if action == 1:
            self.state[0] = max(0, self.state[0] - 1)  # Green light: reduce traffic
        else:
            self.state[0] = min(10, self.state[0] + 1)  # Red light: increase traffic

        # Reward: Reduce traffic, penalty for congestion
        reward = -self.state[0] + self.reward_weight * (10 - self.state[1])

        # Done if the traffic gets too congested
        done = bool(self.state[0] >= 10)

        return self.state, reward, done, {}

    def render(self, mode='human'):
        # Handle events (e.g., window close)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        # Clear the screen
        self.screen.fill((255, 255, 255))  # White background

        # Display traffic information (e.g., vehicle counts)
        text = self.font.render(f"Lane 1: {self.state[0]} vehicles, Lane 2: {self.state[1]} vehicles", True, (0, 0, 0))
        self.screen.blit(text, (50, 50))

        # Draw simple representation of traffic lights
        if self.state[0] > 5:  # Red light for lane 1
            pygame.draw.rect(self.screen, (255, 0, 0), (150, 150, 50, 100))
        else:  # Green light for lane 1
            pygame.draw.rect(self.screen, (0, 255, 0), (150, 150, 50, 100))

        if self.state[1] > 5:  # Red light for lane 2
            pygame.draw.rect(self.screen, (255, 0, 0), (400, 150, 50, 100))
        else:  # Green light for lane 2
            pygame.draw.rect(self.screen, (0, 255, 0), (400, 150, 50, 100))

        # Update the display
        pygame.display.update()

        # Pause to control the speed of the visualization
        pygame.time.delay(500)

    def close(self):
        pygame.quit()
