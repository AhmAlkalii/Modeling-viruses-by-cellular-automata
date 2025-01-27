import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# Constants for states
SUSCEPTIBLE = 0  # Green
INFECTED = 1  # Red
RECOVERED = 2  # Purple
DEAD = 3  # Black

# Custom colormap
cmap = ListedColormap(['green', 'red', 'purple', 'black'])

# Load the COVID data
covid = pd.read_csv('USA Data.csv')

# Extract infection, recovery, and death rates
average_infection_rate = covid['Infected per 1M'].mean() / 1000000
average_recovery_rate = covid['Recovered per 1M'].mean() / 1000000
average_death_rate = covid['Death per 1M'].mean() / 1000000

# Initialize the grid with susceptible and initially infected cells
def initialize_grid(size, initial_infection_rate):
    grid = np.random.choice([SUSCEPTIBLE, INFECTED],
                            size=size * size,
                            p=[1 - initial_infection_rate, initial_infection_rate])
    return grid.reshape((size, size))

# Update the grid based on infection, recovery, and death probabilities
def update_grid(grid, infection_prob, recovery_prob, death_prob):
    new_grid = grid.copy()
    size = grid.shape[0]
    for i in range(size):
        for j in range(size):
            if grid[i, j] == INFECTED:
                if np.random.rand() < death_prob:
                    new_grid[i, j] = DEAD
                elif np.random.rand() < recovery_prob:
                    new_grid[i, j] = RECOVERED
                else:
                    for x in range(max(0, i - 1), min(size, i + 2)):
                        for y in range(max(0, j - 1), min(size, j + 2)):
                            if grid[x, y] == SUSCEPTIBLE:
                                if np.random.rand() < infection_prob:
                                    new_grid[x, y] = INFECTED
    return new_grid


# Plot the epidemiological curve
def plot_epidemiological_curve(susceptible_counts, infected_counts, recovered_counts, dead_counts, steps):
    plt.figure()
    plt.plot(range(steps + 1), susceptible_counts, label='Susceptible', color='green')
    plt.plot(range(steps + 1), infected_counts, label='Infected', color='red')
    plt.plot(range(steps + 1), recovered_counts, label='Recovered', color='purple')
    plt.plot(range(steps + 1), dead_counts, label='Dead', color='black')
    plt.xlabel('Steps')
    plt.ylabel('Count')
    plt.title('Epidemiological Curve')
    plt.legend()
    plt.show()

# Plot heatmap of the grid state
def plot_heatmap(grid, step):
    plt.figure()
    ax = plt.gca()
    plt.imshow(grid, cmap=cmap, vmin=0, vmax=3)
    plt.title(f'Heatmap at Step {step}')
    cbar = plt.colorbar(ticks=[0, 1, 2, 3], format='%d', label='State')
    cbar.ax.set_yticklabels(['Susceptible', 'Infected', 'Recovered', 'Dead'])

    # Add counts to xlabel
    total_cells = grid.size
    infected_cells = np.sum(grid == INFECTED)
    recovered_cells = np.sum(grid == RECOVERED)
    dead_cells = np.sum(grid == DEAD)
    ax.set_xlabel(
        f'Total Cells: {total_cells}  Infected Cells: {infected_cells}  Recovered Cells: {recovered_cells}  Dead Cells: {dead_cells}'
    )

    plt.tight_layout()
    plt.show()

# Plot bar chart of cell states
def plot_bar_chart(grid, step):
    counts = [np.sum(grid == state) for state in [SUSCEPTIBLE, INFECTED, RECOVERED, DEAD]]
    labels = ['Susceptible', 'Infected', 'Recovered', 'Dead']
    plt.figure()
    plt.bar(labels, counts, color=['green', 'red', 'purple', 'black'])
    plt.title(f'Bar Chart of Cell States at Step {step}')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.show()

# Plot pie chart of cell states
def plot_pie_chart(grid, step):
    counts = [np.sum(grid == state) for state in [SUSCEPTIBLE, INFECTED, RECOVERED, DEAD]]
    labels = ['Susceptible', 'Infected', 'Recovered', 'Dead']
    plt.figure()
    plt.pie(counts, labels=labels, colors=['green', 'red', 'purple', 'black'], autopct='%1.1f%%')
    plt.title(f'Pie Chart of Cell States at Step {step}')
    plt.show()

# Main function to run the simulation
def run_simulation(grid_size, initial_infection_rate, infection_prob, recovery_prob, death_prob, steps):
    grid = initialize_grid(grid_size, initial_infection_rate)

    # Initialize lists to store the counts of each state
    susceptible_counts = [np.sum(grid == SUSCEPTIBLE)]
    infected_counts = [np.sum(grid == INFECTED)]
    recovered_counts = [np.sum(grid == RECOVERED)]
    dead_counts = [np.sum(grid == DEAD)]

    plot_heatmap(grid, 0)  # Initial heatmap

    for step in range(1, steps + 1):
        grid = update_grid(grid, infection_prob, recovery_prob, death_prob)
        plot_heatmap(grid, step)  # Update heatmap for each step

        # Update counts for the epidemiological curve
        susceptible_counts.append(np.sum(grid == SUSCEPTIBLE))
        infected_counts.append(np.sum(grid == INFECTED))
        recovered_counts.append(np.sum(grid == RECOVERED))
        dead_counts.append(np.sum(grid == DEAD))

    # Plot the epidemiological curve
    plot_epidemiological_curve(susceptible_counts, infected_counts, recovered_counts, dead_counts, steps)

    # Plot the final bar chart and pie chart after the simulation
    plot_bar_chart(grid, steps)
    plot_pie_chart(grid, steps)

# if __name__ == "__main__":
#     run_simulation(grid_size=50, initial_infection_rate=average_infection_rate,
#                    infection_prob=0.2, recovery_prob=average_recovery_rate,
#                    death_prob=average_death_rate, steps=19)
