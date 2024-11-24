# proekti_1


3D Parametric Formula Plotter

This project is a Python script that generates 3D plots for user-defined mathematical formulas. It enables users to input up to 5 formulas using the variables x and z and visualizes their relationships in 3D space.
Features

    Dynamic Formula Evaluation:
        Users can input mathematical expressions using Python functions like sin, cos, and exp.
        Formulas can combine x and z variables to create complex parametric relationships.

    3D Visualization:
        Generates interactive 3D scatter plots for each formula.
        Plots data points (x, y, z) and connects them with lines for a clear visual representation.

    Multiple Formula Input:
        Supports up to 5 formulas in one execution.
        Each formula is displayed in a separate 3D plot.

    Error Handling:
        Provides user-friendly error messages if the input formula is invalid or cannot be evaluated.

How It Works
1. Input Mathematical Formulas

    Users can input up to 5 formulas, separated by commas.
    Example of valid formulas:
        sin(x) + cos(z)
        exp(-0.01*x) * sin(z)
        x**4 + x**2

2. Generate x and z Values

    x values range from 0.1 to 100 (step 0.1) for a fine-grained resolution.
    z values range from 0.02 to 20 (step 0.02).

3. Evaluate Formulas

    For each formula, the script evaluates the y values using the input expressions.
    Dynamic evaluation is performed using Python’s eval() function.

4. Plot in 3D

    The evaluated x, y, and z values are visualized using Matplotlib's 3D plotting capabilities.
    Each plot includes:
        Purple scatter points representing the data.
        A black connection line to show continuity.
        Labels for axes and a title for the formula.

Dependencies
Python Libraries

    Matplotlib: For creating 3D visualizations.
    mpl_toolkits.mplot3d: A toolkit for 3D plotting in Matplotlib.
    math: For mathematical operations like sin, cos, and exp.

Install required dependencies using:

pip install matplotlib

Usage
Step 1: Clone the Repository

git clone https://github.com/<your-username>/3d-formula-plotter.git
cd 3d-formula-plotter

Step 2: Run the Script

python 3d_plotter.py

Step 3: Input Formulas

    When prompted, input up to 5 formulas, separated by commas.
    Example:

    Enter formulas: sin(x) + cos(z), exp(-0.01*x) * sin(z)

Step 4: View the Plots

    The script generates a 3D scatter plot for each formula.
    Rotate and zoom the plot for better visualization.

Example Outputs
Input:

sin(x) + cos(z), x**2 - z**2, exp(-0.01*x) * sin(z)

Generated Plots:

    Plot 1: 3D visualization of sin(x) + cos(z).
    Plot 2: 3D visualization of x**2 - z**2.
    Plot 3: 3D visualization of exp(-0.01*x) * sin(z).

Error Handling

    If the input formula contains invalid syntax or unsupported operations, the script displays a clear error message:

Error: Try again [error details]

Examples of unsupported formulas:

    Using variables other than x and z.
    Using undefined functions or invalid expressions.

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
