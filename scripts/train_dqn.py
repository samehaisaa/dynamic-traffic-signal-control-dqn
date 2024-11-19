from models.dqn_model import create_model, train_model
from envs.traffic_env import TrafficEnv
from stable_baselines3.common.vec_env import DummyVecEnv

def main():
    # Initialize the environment and wrap it in DummyVecEnv
    env = DummyVecEnv([lambda: TrafficEnv()])
    
    # Create the DQN model
    model = create_model(env)

    # Train the model
    print("Training the DQN model...")
    train_model(model, timesteps=20000)

if __name__ == "__main__":
    main()
