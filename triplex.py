import matplotlib.pyplot as plt

# Create the main figure and the first axes (primary y-axis)
fig, ax1 = plt.subplots()

# Plot data on the primary y-axis
ax1.plot([1, 2, 3], [4, 5, 6], color='b', label="Data 1")
ax1.set_ylabel('Primary Y-axis', color='b')

# Create the second y-axis (shared x-axis)
ax2 = ax1.twinx()
ax2.plot([1, 2, 3], [6, 4, 2], color='g', label="Data 2")
ax2.set_ylabel('Secondary Y-axis', color='g')

# Create the third y-axis (shared x-axis)
# Move the third y-axis a bit further to avoid overlap
ax3 = ax1.twinx()

# Move the third y-axis to the right by setting the position of the spine
ax3.spines['right'].set_position(('outward', 60))  # Shift third y-axis outward

# Plot data on the third y-axis
ax3.plot([1, 2, 3], [1, 2, 3], color='r', label="Data 3")
ax3.set_ylabel('Tertiary Y-axis', color='r')

# Optional: Set axis labels and titles
ax1.set_xlabel('X-axis')

plt.title('Multiple twinx Example')
plt.tight_layout()

plt.show()
