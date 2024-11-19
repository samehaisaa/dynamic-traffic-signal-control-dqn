import matplotlib.pyplot as plt
import numpy as np

def plot_traffic(state):
    # Plotting a simple graph for traffic flow
    plt.clf()
    plt.bar([1, 2], state, color=['red', 'blue'])
    plt.xlabel('Lanes')
    plt.ylabel('Number of vehicles')
    plt.title('Traffic Flow')
    plt.pause(0.1)

def main():
    state = np.array([5, 3])  # Initial state for demonstration

    for _ in range(100):
        plot_traffic(state)
        state[0] = max(0, state[0] - 1)  # Update traffic state for demo
        plt.pause(0.1)

if __name__ == "__main__":
    main()
