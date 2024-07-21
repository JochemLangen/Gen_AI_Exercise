import numpy as np
import matplotlib.pyplot as plt
import math
import os


class fruit_inspector:

    def __init__(self, file_path='test'):
        
        if file_path == 'test':
            file_path = os.path.join('..','data','fruit_baskets_example')
            self.test = True
        else:
            self.test = False
        
        self.fpath = file_path
        
        self.fruit_boxes = self.__read_basket_file_inner(test = self.test)
        
        self.plot_baskets()
        
    def read_basket_file(self, file_path=None):
        return self.__read_basket_file_inner(file_path)

    def __read_basket_file_inner(self, file_path=None, test=False):

        if file_path == None:
            file_path = self.fpath
            test = self.test
        
        basket_contents = {
            "A": ["Blueberry", "Raspberry", "Strawberry", "Gooseberry"],
            "B": ["Apple", "Orange"],
            "C": ["Kiwi", "Banana", "Grapefruit"],
            "D": ["Grapes", "Mango"]
        }
    
        baskets = []

        with open(file_path, 'r') as file:
            lines = file.readlines()
            
        assert not(test and len(lines) != 4), "The test file 'fruit_baskets_example' has changed! " \
                             + "Revert it to its original version and put your results in a different file at once!"
    
        current_basket_type = None
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith('@Basket_type'):
                current_basket_type = line.split('= "')[1].strip().replace('"', '').replace(';', '')
            elif line and current_basket_type:
                contents = line.replace('"', '').strip(',').split(', ')
                if len(contents) != 10:
                    raise ValueError("Incorrect number of fruit found in basket number" + \
                                     " {}: {} \nThis should be 10!".format(len(baskets)+1, \
                                                                           len(contents)))
                if all(item in basket_contents[current_basket_type] for item in contents):
                    baskets.append([current_basket_type] + contents)
                else:
                    raise ValueError(f"Invalid item in basket type {current_basket_type}: {contents}!")
                current_basket_type = None
            else:
                raise ValueError("Found incorrect format at line {}!".format(i+1) \
                                 + " This is not allowed!")
        
        baskets = np.array(baskets)
        
        if not(test):
            assert len(baskets) == 50, str("Incorrect number of baskets found: {}! This should be 50.".format(len(baskets)))

            assert all(x in baskets[:,0] for x in ['A', 'B', 'C', 'D']), "There should be at least one of every basket type!"
        
            assert all(x in baskets[:,1:] for x in ["Blueberry", "Raspberry", "Strawberry", "Gooseberry", "Apple", "Orange", "Kiwi", "Banana", "Grapefruit", "Grapes", "Mango"]), "There should be at least one of very fruit type!"
        
        return baskets
    
    def plot_baskets(self, baskets_array=None):
        
        if baskets_array == None:
            baskets_array = self.fruit_boxes
        
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
    
        basket_size = 4
        num_baskets = len(baskets_array)
    
        num_cols = math.ceil(math.sqrt(num_baskets))
        num_rows = math.ceil(num_baskets / num_cols)
    
        for i, basket in enumerate(baskets_array):
            basket_type = basket[0]
            fruits = basket[1:]
    
            row = i // num_cols
            col = i % num_cols
            x_start = col * (basket_size + 2)
            y_start = -row * (basket_size + 2)
    
            rect = plt.Rectangle((x_start, y_start), basket_size, basket_size, edgecolor='black', facecolor='none')
            ax.add_patch(rect)
    
            fruit_size = 1400/num_baskets
            for j, fruit in enumerate(fruits):
                x = x_start + (j % basket_size) + 0.5
                y = y_start + (j // basket_size) + 0.6
                ax.scatter(x, y, color=fruit_colors[fruit], s=fruit_size)
    
        unique_fruits = list(fruit_colors.keys())
        for fruit in unique_fruits:
            ax.scatter([], [], color=fruit_colors[fruit], label=fruit)
            
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
        
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        
        ax.set_title('Your fruit baskets:')
    
        plt.show()