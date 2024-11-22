import matplotlib.pyplot as plt  # Import the matplotlib library for plotting.
from random import choice  # Import choice to randomly select steps for the walk.


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points  # The number of points in the walk.

        # All walks start at the origin (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep adding points until the walk has the desired number of points.
        while len(self.x_values) < self.num_points:
            # Randomly choose the direction (positive or negative) and distance for x and y.
            x_direction = choice([1, -1])  # Choose either 1 (right) or -1 (left).
            x_distance = choice([0, 1, 2, 3, 4])  # Choose a distance from 0 to 4.
            x_step = x_direction * x_distance  # Calculate the step in the x direction.

            y_direction = choice([1, -1])  # Choose either 1 (up) or -1 (down).
            y_distance = choice([0, 1, 2, 3, 4])  # Choose a distance from 0 to 4.
            y_step = y_direction * y_distance  # Calculate the step in the y direction.

            # Ignore steps that don't move at all (both x_step and y_step are 0).
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next position by adding the step to the last position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Append the new position to the walk.
            self.x_values.append(x)
            self.y_values.append(y)


# Main loop to repeatedly create and display random walks.
while True:
    # Create a new random walk with 50,000 points.
    rw = RandomWalk(50_000)
    rw.fill_walk()  # Generate the points for the walk.

    # Create a plot to visualize the random walk.
    plt.style.use('classic')  # Use a classic style for the plot.
    fig, ax = plt.subplots(figsize=(15, 9))  # Create a figure and axis with a large size.

    # Use a colormap to color points based on their position in the walk.
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Highlight the starting point in green and the ending point in red.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Start point.
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # End point.

    # Remove the axis for a cleaner look.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')  # Ensure equal scaling on both axes.

    # Display the plot.
    plt.show()

    # Ask the user if they want to create another random walk.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':  # Exit the loop if the user inputs 'n'.
        break
