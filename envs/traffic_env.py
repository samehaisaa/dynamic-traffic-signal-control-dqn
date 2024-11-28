import gym
from gym import spaces
import numpy as np
import random
import pygame
from pygame.locals import *

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()

        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=10, shape=(2,), dtype=int)
        self.state = np.array([random.randint(0, 10), random.randint(0, 10)])

        self.reward_weight = 1.0

        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Traffic Signal Control")
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        self.render_every_n_steps = 5  # Only render every few steps to avoid freezing

    def reset(self):
        self.state = np.array([random.randint(0, 5), random.randint(0, 5)])
        return self.state

    def step(self, action):
        if action == 1:
            self.state[0] = max(0, self.state[0] - 1)  # Green light: reduce traffic
        else:
            self.state[0] = min(5, self.state[0] + 1)  # Red light: increase traffic

        reward = -self.state[0] + self.reward_weight * (10 - self.state[1])
        done = bool(self.state[0] >= 5)

        if self.render_every_n_steps > 0 and self.state[0] % self.render_every_n_steps == 0:
            self.render()  # Render the screen every few steps

        return self.state, reward, done, {}

    def render(self, mode='human'):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        self.screen.fill((255, 255, 255))  # White background

        text = self.font.render(f"Lane 1: {self.state[0]} vehicles, Lane 2: {self.state[1]} vehicles", True, (0, 0, 0))
        self.screen.blit(text, (50, 50))

        if self.state[0] > 2:
            pygame.draw.rect(self.screen, (255, 0, 0), (150, 150, 50, 100))  # Red light
        else:
            pygame.draw.rect(self.screen, (0, 255, 0), (150, 120, 50, 100))  # Green light

        if self.state[1] > 2:
            pygame.draw.rect(self.screen, (255, 0, 0), (400, 150, 50, 100))  # Red light
        else:
            pygame.draw.rect(self.screen, (0, 255, 0), (400, 150, 50, 100))  # Green light

        pygame.display.update()
        self.clock.tick(10)  # Control the frame rate

    def close(self):
        pygame.quit()
