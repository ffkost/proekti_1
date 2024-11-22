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

import matplotlib.pyplot as plt

x_values = range(1, 1001)  #
y_values = [x**2 for x in x_values]  #

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=10) #
#ax.scatter(x_values, y_values, color='red', s=10)  # style
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10) # style 2
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes. # isto
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style='plain') #style

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight') # za save