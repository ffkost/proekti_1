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


