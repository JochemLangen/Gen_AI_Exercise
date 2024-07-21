import numpy as np
import matplotlib.pyplot as plt
import math


class fruit_inspector:

    def __init__(self, file_path):
        
        self.fpath = file_path
        
        self.fruit_boxes = self.read_basket_file()
        
        self.plot_baskets()
        
    

    def read_basket_file(self, file_path=None):
        
        # If no filepath is provided, use object's filepath
        if file_path == None:
            file_path = self.fpath
        
        # Define the allowed contents for each basket type
        basket_contents = {
            "A": ["Blueberry", "Raspberry", "Strawberry", "Gooseberry"],
            "B": ["Apple", "Orange"],
            "C": ["Kiwi", "Banana", "Grapefruit"],
            "D": ["Grapes", "Mango"]
        }
    
        baskets = []
    
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
        
    
        current_basket_type = None
        for line in lines:
            line = line.strip()
            if line.startswith('@Basket_type'):
                current_basket_type = line.split('=')[1].strip().replace('"', '').replace(';', '')
            elif line and current_basket_type:
                contents = line.replace('"', '').strip(',').split(', ')
                if len(contents) != 10:
                    raise ValueError("Incorrect number of fruit found in basket number" + \
                                     " {}: {} \nThis should be 10!".format(len(baskets)-1, \
                                                                           len(contents)))
                if all(item in basket_contents[current_basket_type] for item in contents):
                    baskets.append([current_basket_type] + contents)
                else:
                    raise ValueError(f"Invalid item in basket type {current_basket_type}: {contents}")
                current_basket_type = None
            else:
                raise ValueError("Line found with incorrect format! This is not allowed!")
                
        if len(baskets) != 50:
            raise ValueError("Incorrect number of baskets found! This should be 50.")
        
        return np.array(baskets)
    
    def plot_baskets(self, baskets_array=None):
        
        # If no baskets are provided, use object's baskets
        if baskets_array == None:
            baskets_array = self.fruit_boxes
        
        # Define colors for each type of fruit
        fruit_colors = {
            "Blueberry": (0.0, 0.0, 0.5),      # Dark blue
            "Raspberry": (0.89, 0.04, 0.36),   # Red-pink
            "Strawberry": (0.99, 0.18, 0.28),  # Red
            "Gooseberry": (0.68, 1.0, 0.18),   # Light green
            "Apple": (0.2, 0.8, 0.0),          # Green
            "Orange": (1.0, 0.65, 0.0),        # Orange
            "Kiwi": (0.6, 0.4, 0.2),           # Brown
            "Banana": (1.0, 1.0, 0.2),         # Yellow
            "Grapefruit": (1.0, 0.45, 0.45),   # Light red
            "Grapes": (0.5, 0.0, 0.5),         # Purple
            "Mango": (1.0, 0.6, 0.2)          # Orange-yellow
        }
    
        fig, ax = plt.subplots()
    
        # Define the size of each basket's rectangle (4x4)
        basket_size = 4
        num_baskets = len(baskets_array)
    
        # Calculate number of rows and columns
        num_cols = math.ceil(math.sqrt(num_baskets))
        num_rows = math.ceil(num_baskets / num_cols)
    
        for i, basket in enumerate(baskets_array):
            basket_type = basket[0]
            fruits = basket[1:]
    
            # Calculate the position of the rectangle
            row = i // num_cols
            col = i % num_cols
            x_start = col * (basket_size + 2)  # Added extra space between baskets
            y_start = -row * (basket_size + 2)  # Added extra space between baskets, negative for top-down
    
            # Draw the basket as a black rectangle
            rect = plt.Rectangle((x_start, y_start), basket_size, basket_size, edgecolor='black', facecolor='none')
            ax.add_patch(rect)
    
            # Evenly space the fruits inside the basket in a 4x4 grid
            for j, fruit in enumerate(fruits):
                x = x_start + (j % basket_size) + 0.5
                y = y_start + (j // basket_size) + 0.6
                ax.scatter(x, y, color=fruit_colors[fruit])
    
        # Create a legend with all fruit types
        unique_fruits = list(fruit_colors.keys())
        for fruit in unique_fruits:
            ax.scatter([], [], color=fruit_colors[fruit], label=fruit)
            
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
        
        # Remove x and y labels and ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        
        ax.set_title('Your fruit baskets:')
    
        plt.show()