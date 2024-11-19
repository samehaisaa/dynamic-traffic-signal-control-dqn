def test_model():
    # Load the trained model
    model = DQN.load("./dqn_tensorboard/DQN_3")  # Or wherever your model is saved

    # Initialize the environment
    env = TrafficEnv()

    # Test the model for 10 episodes
    rewards = []
    for episode in range(10):
        obs = env.reset()
        total_reward = 0
        done = False
        while not done:
            # Use the model to predict the next action
            action, _states = model.predict(obs)
            obs, reward, done, info = env.step(action)
            total_reward += reward
            
            # Render the environment to visualize it
            env.render()

        rewards.append(total_reward)
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

    # Calculate and print the average reward over all episodes
    avg_reward = sum(rewards) / len(rewards)
    print(f"Average Reward over 10 episodes: {avg_reward}")
