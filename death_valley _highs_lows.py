from pathlib import Path  # Import Path for handling file paths.
import csv  # Import csv module for working with CSV files.
from datetime import datetime  # Import datetime for working with date formats.
import matplotlib.pyplot as plt  # Import matplotlib for plotting data.

# Define the path to the CSV file.
path = Path('death_valley_2021_simple.csv')
lines = path.read_text().splitlines()  # Read the CSV file line by line.
print(lines)  # Print the content of the CSV file for debugging.

# Create a CSV reader object to parse the lines.
reader = csv.reader(lines)
print(reader)  # Print the reader object for debugging.
header_row = next(reader)  # Read the header row (first line of the CSV).

# Extract dates, high, and low temperatures from the CSV file.
dates, highs, lows = [], [], []  # Initialize empty lists for data.
for row in reader:  # zapocnuvame od vtor red posto gore header row veke zita prv red
    current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Convert the date string to a datetime object.
    try:
        high = int(row[3])  # Parse the high temperature as an integer.
        low = int(row[4])  # Parse the low temperature as an integer.
    except ValueError:  # Handle cases where data is missing or invalid.
        print(f"Missing data for {current_date}")  # Print a message for missing data.
    else:
        dates.append(current_date)  # Add valid dates to the list.
        highs.append(high)  # Add high temperatures to the list.
        lows.append(low)  # Add low temperatures to the list.
print(highs)  # Print the high temperatures for debugging.

# Display the index and header for each column in the header row.
for index, column_header in enumerate(header_row):  # enumerate dava index i sto ima na taa pozicija
    print(index, column_header)  # Print the index and column header.

# Plot the high and low temperatures.
#plt.style.use('seaborn') #treba seaborn so drugo ime za style e
fig, ax = plt.subplots()  # Create a figure and axes for the plot.

# Plot high temperatures in red and low temperatures in blue with some transparency.
#ax.plot(highs, color='red')
ax.plot(dates, highs, color='red', alpha=0.5)  # Plot high temperatures with reduced opacity.
ax.plot(dates, lows, color='blue', alpha=0.5)  # Plot low temperatures with reduced opacity.
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # Fill the area between highs and lows.

# Format the plot for better readability.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"  # Title for the plot.
ax.set_title(title, fontsize=20)  # Set the title font size.
ax.set_xlabel('', fontsize=16)  # Label the x-axis.
fig.autofmt_xdate()  # Format the x-axis for date labels.
ax.set_ylabel("Temperature (F)", fontsize=16)  # Label the y-axis.
ax.tick_params(labelsize=16)  # Set the font size for tick labels.

plt.show()  # Display the plot.

#print(header_row) #1 / the same as above for this code and dont remove my comments or change code
