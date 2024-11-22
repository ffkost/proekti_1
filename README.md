# proekti_1


#scatter_squares.py
This project is a simple Python script that visualizes the relationship between numbers and their squares using a scatter plot. It demonstrates the use of the matplotlib library to create customizable and visually appealing charts. The script calculates the squares of numbers from 1 to 1000 and plots them as points on a graph.


Project: Random Walk Visualizer
Description

This project is a Python script that generates and visualizes random walks using the matplotlib library. A random walk is a mathematical concept where each step is determined randomly in both direction and distance. This script allows users to:

    Generate a random walk with up to 50,000 points.
    Visualize the random walk with a gradient of colors, starting from blue and ending with a red point for the final position.

Features

    Interactive User Experience: The program repeatedly asks the user if they want to create a new random walk.
    Custom Visualization:
        Starting point (green) and ending point (red) are emphasized for clarity.
        A gradient color map (Blues) visually distinguishes steps.
        High-resolution plots for detailed visualization.
    No Coding Knowledge Needed: Just run the program and enjoy!

How It Works

    Random Walk Logic:
        The walk begins at the origin (0, 0).
        Each step randomly chooses a direction (+1 or -1) and a distance (0 to 4) for both x and y coordinates.
        Steps that result in no movement are discarded to avoid repetition.
    Visualization:
        The program uses a scatter plot to represent the walk.
        Axes are hidden to focus attention on the walk itself.
    Interactive Mode:
        After displaying a random walk, the program asks the user if they want to generate another walk.
        If the user inputs 'n', the program stops. Otherwise, it generates a new walk.



Project: Temperature Trends Visualization - Death Valley, CA (2021)
Description

This project visualizes daily high and low temperatures for Death Valley, California, in 2021. The data is read from a CSV file, processed, and plotted to show temperature variations over the year.
Features

    CSV Parsing:
        Reads temperature data from a CSV file.
        Handles missing or invalid data gracefully.
    Date Handling:
        Converts string dates to Python datetime objects for accurate plotting.
    Data Visualization:
        Plots high temperatures in red and low temperatures in blue.
        Fills the area between high and low temperatures with a shaded region for visual emphasis.
    Formatted Output:
        Adds a descriptive title, axis labels, and formatted x-axis date labels.
        Ensures readability with customized font sizes and transparency.

How It Works

    Data Extraction:
        Reads the CSV file (death_valley_2021_simple.csv) line by line.
        Extracts dates, high temperatures, and low temperatures from the file.
        Handles missing or invalid data using a try-except block and skips over incomplete rows.
    Plotting:
        Uses matplotlib to create a line plot of high and low temperatures over time.
        Highlights the range between high and low temperatures using a shaded region.
    Output:
        Displays the final visualization using plt.show().

Requirements

    Python 3.x
    Libraries:
        matplotlib
        csv
        datetime

How to Run

    Save the CSV file (death_valley_2021_simple.csv) in the same directory as the script.
    Install the required libraries (if not already installed):

pip install matplotlib

Run the script:

    python temperature_trends.py

    View the plot of daily high and low temperatures for 2021.

Example Output

The script generates a plot with:

    High temperatures shown as a red line.
    Low temperatures shown as a blue line.
    A shaded region between the high and low temperatures to highlight the daily range.

This README is detailed and provides a clear overview of what the project does and how to use it.
