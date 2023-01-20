import numpy
import random

from config import LEARNING_RATE
from formulas import sig, inv_sig, inv_err

curr_node_id = 0

class Layer:
    def __init__(self, num_nodes, input_vals, layer_num):
        self.num_nodes = num_nodes
        self.input_vals = input_vals
        self.layer_num = layer_num
        self.weight = [[random.random() for col in range(len(input_vals))] for row in range(num_nodes)]
        self.weight_delta = [[0 for col in range(len(input_vals))] for row in range(num_nodes)]
        self.layer_net = [0 for col in range(num_nodes)]
        self.layer_out = [0 for col in range(num_nodes)]
        self.bias = (random.random() * 2) - 1

    def eval(self):
        #evaluation part
        #Get input, compute the output of layer nodes.
        raise Exception('Implement this part.')
            

    def backprop(self, other):
        #use backpropagation method to update weights
                
        raise Exception('Implement this part.')

class cfile(file):
    def __init__(self, name, mode = 'r'):
        self = file.__init__(self, name, mode)

    def w(self, string):
        self.writelines(str(string) + '\n')
        return None
