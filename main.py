import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# Define the states
SUSCEPTIBLE = 0  # Green
INFECTED = 1  # Red
RECOVERED = 2  # Purple

# Custom colormap: green for susceptible, red for infected, purple for recovered
cmap = ListedColormap(['green', 'red', 'purple'])


# Initialize the grid with susceptible and initially infected cells
def initialize_grid(size, initial_infection_rate):
    grid = np.random.choice([SUSCEPTIBLE, INFECTED],
                            size=size * size,
                            p=[1 - initial_infection_rate, initial_infection_rate])
    return grid.reshape((size, size))


# Update the grid based on infection and recovery probabilities
def update_grid(grid, infection_prob, recovery_prob):
    new_grid = grid.copy()
    size = grid.shape[0]
    for i in range(size):
        for j in range(size):
            if grid[i, j] == INFECTED:
                # Attempt to recover infected cells
                if np.random.rand() < recovery_prob:
                    new_grid[i, j] = RECOVERED
                else:
                    # Attempt to infect neighboring susceptible cells
                    for x in range(max(0, i - 1), min(size, i + 2)):
                        for y in range(max(0, j - 1), min(size, j + 2)):
                            if grid[x, y] == SUSCEPTIBLE:
                                if np.random.rand() < infection_prob:
                                    new_grid[x, y] = INFECTED
    return new_grid


# Display the grid with color representation and counts
def display_grid(grid, step):
    plt.imshow(grid, cmap=cmap, vmin=0, vmax=2)
    plt.title(f'Step: {step}')
    plt.colorbar(ticks=[0, 1, 2], format='%d', label='State')

    # Count the number of infected cells
    total_cells = grid.size
    infected_cells = np.sum(grid == INFECTED)
    recovered_cells = np.sum(grid == RECOVERED)
    plt.xlabel(f'Total Cells: {total_cells}  Infected Cells: {infected_cells}  Recovered Cells: {recovered_cells}')

    plt.show()


# Animate the simulation over a series of steps
def animate_simulation(grid, steps, infection_prob, recovery_prob):
    fig, ax = plt.subplots()
    im = ax.imshow(grid, cmap=cmap, vmin=0, vmax=2)

    def update(frame):
        nonlocal grid
        grid = update_grid(grid, infection_prob, recovery_prob)
        im.set_array(grid)
        ax.set_title(f'Step: {frame}')

        # Count and display the number of infected cells
        total_cells = grid.size
        infected_cells = np.sum(grid == INFECTED)
        recovered_cells = np.sum(grid == RECOVERED)
        ax.set_xlabel(f'Total Cells: {total_cells}  Infected Cells: {infected_cells}  Recovered Cells: {recovered_cells}')

        return [im]

    anim = animation.FuncAnimation(fig, update, frames=steps, repeat=False)
    plt.show(block=True)  # Ensure the plot window remains open


# Main function to run the simulation
def run_simulation(grid_size, initial_infection_rate, infection_prob, recovery_prob, steps):
    grid = initialize_grid(grid_size, initial_infection_rate)
    display_grid(grid, 0)  # Display the initial grid
    for step in range(1, steps + 1):
        grid = update_grid(grid, infection_prob, recovery_prob)
        display_grid(grid, step)  # Display the grid at each step


# Example usage
if __name__ == "__main__":
    grid_size = 50
    initial_infection_rate = 0.1
    infection_prob = 0.2
    recovery_prob = 0.05
    steps = 5
    run_simulation(grid_size, initial_infection_rate, infection_prob, recovery_prob, steps)
