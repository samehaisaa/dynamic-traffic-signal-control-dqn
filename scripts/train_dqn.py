from models.dqn_model import create_model, train_model
from envs.traffic_env import TrafficEnv
from stable_baselines3.common.vec_env import DummyVecEnv

def main():
    env = DummyVecEnv([lambda: TrafficEnv()])
    
    model = create_model(env)

    print("Training the DQN model...")
    train_model(model, timesteps=2000)

if __name__ == "__main__":
    main()
