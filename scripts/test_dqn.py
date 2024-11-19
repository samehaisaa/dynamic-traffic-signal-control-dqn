from stable_baselines3 import DQN
from envs.traffic_env import TrafficEnv
from stable_baselines3.common.vec_env import DummyVecEnv

def main():
    # Initialize the environment and load the trained model
    env = DummyVecEnv([lambda: TrafficEnv()])
    model = DQN.load("dqn_traffic_model")

    # Run the agent in the environment
    obs = env.reset()
    total_reward = 0

    for _ in range(100):  # Run for 100 timesteps
        action, _states = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    print(f"Total Reward: {total_reward}")

if __name__ == "__main__":
    main()
