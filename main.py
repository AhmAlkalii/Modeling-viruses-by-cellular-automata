from choromap import create_choromap
from plot import create_plots
from sim import run_simulation, average_infection_rate, average_recovery_rate

def main():
    create_choromap()
    create_plots()

    # Example simulation parameters
    grid_size = 80
    initial_infection_rate = average_infection_rate
    infection_prob = 0.2
    recovery_prob = average_recovery_rate
    steps = 10

    # Run simulation
    run_simulation(grid_size, initial_infection_rate, infection_prob, recovery_prob, steps)

if __name__ == "__main__":
    main()
