# import matplotlib.pyplot as plt
# #plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(2, 4)
# plt.show()
#------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# #plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# plt.show()

# import matplotlib.pyplot as plt
#
# x_values = [1, 2, 3, 4, 5] #
# y_values = [1, 4, 9, 16, 25] #
#
# #plt.style.use('seaborn-v0_8') #
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100) #
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
# plt.show()

# import matplotlib.pyplot as plt
#
# x_values = range(1, 1001)  #
# y_values = [x**2 for x in x_values]  #
#
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# #ax.scatter(x_values, y_values, s=10) #
# #ax.scatter(x_values, y_values, color='red', s=10)  # style
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10) # style 2
# #ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#
# # Set chart title and label axes. # isto
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Set size of tick labels.
# ax.tick_params(labelsize=14)
#
# # Set the range for each axis.
# ax.axis([0, 1100, 0, 1_100_000])
# #ax.ticklabel_format(style='plain') #style
#
# plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight') # za save

# import matplotlib.pyplot as plt
# from math import sin, cos, exp
#
# def evaluate_formula(formula, x_values):
#     try:
#         y_values = [eval(formula) for x in x_values]
#         return y_values
#     except Exception as e:
#         print(f"Error evaluating formula: {e}")
#         return None
#
#
#
# print("You can use 'sin', 'cos', and 'exp' along with standard operators (+, -, *, /, **) in your formula.")
# print("Example formulas: 'sin(x) + 0.5 * sin(5*x)', 'exp(-0.01*x) * sin(x)', 'cos(x**2 / 100)'")
# user_formula = input("Enter a formula with 'x' as the variable: ")
#
# x_values = [x / 10 for x in range(1, 1001)]
#
# y_values = evaluate_formula(user_formula, x_values)
#
# if y_values:
#     plt.style.use('seaborn-v0_8')
#     fig, ax = plt.subplots()
#     ax.plot(x_values, y_values, color='black', linewidth=1, label="Connection Line")
#     ax.scatter(x_values, y_values, color='purple', s=10, label="Data Points")
#     ax.set_title(f"Plot of {user_formula}", fontsize=24)
#     ax.set_xlabel("Value", fontsize=14)
#     ax.set_ylabel("Result of Formula", fontsize=14)
#     ax.tick_params(labelsize=14)
#     ax.axis([0, max(x_values), min(y_values) - 10, max(y_values) + 10])
#     ax.legend()
#     plt.show()
#     plt.savefig('function_plot.png', bbox_inches='tight')
# else:
#     print("Failed to plot the formula. Please check your input and try again.")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin, cos, exp


def evaluate_formula(formula, x_values, z_values):
    try:
        y_values = [eval(formula) for x, z in zip(x_values, z_values)] #!
        return y_values
    except Exception as e:
        print(f"Error Try again {e}")
        return None

# Input formulas from the user
print("You can use sin,cos, exp() \n")
print("Use 'x' and 'z' as variables in the formula (e.g., sin(x) + cos(z), sin(x) + sin(z), exp(-0.01*x) * sin(z),x**4+x**2")
print("Enter up to 5 formulas separated by commas.")
user_input = input("Enter formulas: ")

# Split input into individual formulas
formulas = [f.strip() for f in user_input.split(",")]

# Limit to a maximum of 5 formulas
if len(formulas) > 5:
    print("Error: You entered more than 5 formulas. Please enter up to 5 formulas.")
else:
    # Generate x and z values (parametric grid)
    x_values = [x / 10 for x in range(1, 1001)]  # Finer range for smoother waves
    z_values = [z / 50 for z in range(1, 1001)]  # Another parameter (z)

    # Create a 3D plot for each formula
    for i, formula in enumerate(formulas):
        y_values = evaluate_formula(formula, x_values, z_values)

        if y_values:
            # Create a 3D plot
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Scatter purple dots in 3D space and connect them
            ax.scatter(x_values, y_values, z_values, color='purple', s=10, label="Data Points")
            ax.plot(x_values, y_values, z_values, color='black', linewidth=1, label="Connection Line")

            # Set labels and title
            ax.set_title(f"3D Plot of {formula}", fontsize=20)
            ax.set_xlabel("X-axis", fontsize=12)
            ax.set_ylabel("Y-axis", fontsize=12)
            ax.set_zlabel("Z-axis", fontsize=12)

            # Add a legend for clarity
            ax.legend()

    # Show all plots at once
    plt.show()


