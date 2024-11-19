from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from envs.traffic_env import TrafficEnv

def create_model(env):
    model = DQN("MlpPolicy", env, verbose=1, tensorboard_log="./dqn_tensorboard/")
    return model

def train_model(model, timesteps=10000):
    model.learn(total_timesteps=timesteps)
    model.save("dqn_traffic_model")
