
import tkinter as tk
from tkinter import ttk
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import plot_handler as ph


map_type = None


# Function to plot graph
def update_plot():

    #set R-value
    ph.r = float(entry.get())
    ph.x0 = float(entry_start.get())

    #Type of map
    map_type = text_var.get()
    # Generate random data for demonstration
    if map_type == "Logistic map" or map_type == "Tent map":
        x, y = ph.get_x_y(map_type)
    else:
        x = np.linspace(0, 10, 100)
        y = np.sin(x) + np.random.random(100) * 0.5  # Sine wave with noise

    # Clear the current figures
    ax1.clear()
    ax2.clear()
    
    # Plot on the first subplot
    ax1.plot(x, y, label="Return map")
    ax1.plot(x, x, label="y=x")
    ax1.set_title(map_type)
    ax1.set_xlabel("x(j)")
    ax1.set_ylabel("x(j+1)")
    ax1.legend(loc='upper right')

    nbr_steps = int(entry_nbr_steps.get())
    if map_type == "Logistic map":
        x, y = ph.logistic_map(nbr_steps)
    else:
        y = np.sin(x)
    ax2.plot(x, y, label=map_type)  # Example plot for second subplot
    ax2.set_title("After some timesteps")
    ax2.set_xlabel("j")
    ax2.set_ylabel("x(j)")

    
    # Redraw the canvas
    canvas.draw()

# Function to handle window close event
# Function to handle window close event
def on_closing():
    # Quit tkinter main loop and destroy the window
    root.quit()
    root.destroy()

# Create the main tkinter window
root = tk.Tk()
root.title("Tkinter with Matplotlib")

# Create a frame for the plot and button
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

#fig, ax = plt.subplots(figsize=(5, 4))
# Create a matplotlib figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))  # 1 row, 2 columns

# Create a Tkinter variable to hold the selected text
text_var = tk.StringVar(value="Logistic map")

# Create a canvas to embed the plot
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

font_size = 20
# Define a larger font
large_font = font.Font(size=font_size)

# Create a style object
style = ttk.Style()

# Configure the styles for some widgets
style.configure('.',
                font=large_font)  # Apply the font style
#style.configure('TRadioButton',
#                font=large_font)


# Create a button to update the plot
button = ttk.Button(frame, text="Show Plot", command=update_plot)
button.pack(side=tk.BOTTOM)

# Create and pack the radio buttons
# Create a radio button with arguments on multiple lines
radio_button_a = ttk.Radiobutton(
    root,
    text="Logistic map",
    value="Logistic map",
    variable=text_var
)
#radio_button_a.pack(anchor=tk.W)
radio_button_a.pack(anchor=tk.W, padx=10, pady=10, side=tk.LEFT)

radio_button_b = ttk.Radiobutton(
    root, text="Tent map",
    value="Tent map",
    variable=text_var
)
#radio_button_b.pack(anchor=tk.W)
radio_button_b.pack(anchor=tk.W, padx=10, pady=10, side=tk.LEFT)

# Create a label
label = tk.Label(root, text="R:", font=large_font)
#label.pack(padx=10, pady=10)
label.pack(side=tk.LEFT, padx=10, pady=10)

# Create a StringVar with default value
default_value = tk.StringVar(value="2")

entry = tk.Entry(root, width=5, textvariable=default_value, font=large_font)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label
label = tk.Label(root, text="Initial x:", font=large_font)
label.pack(side=tk.LEFT, padx=10, pady=10)

# Create a StringVar with default value
default_value = tk.StringVar(value="0.1")

entry_start = tk.Entry(
    root,
    width=6,
    textvariable=default_value,
    font=large_font
)
entry_start.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label
label = tk.Label(root, text="Number of steps:", font=large_font)
label.pack(side=tk.LEFT, padx=10, pady=10)

# Create a StringVar with default value
default_value = tk.StringVar(value="20")

entry_nbr_steps = tk.Entry(
    root,
    width=6,
    textvariable=default_value,
    font=large_font
)
entry_nbr_steps.pack(side=tk.LEFT, padx=10, pady=10)

# Initialize the plot
update_plot()

# Bind the window close button to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the tkinter main loop
root.mainloop()