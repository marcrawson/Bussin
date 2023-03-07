import csv
import numpy as np
from clean_data import *

def get_training_inputs():
    with open("training_inputs.csv", "r", encoding='utf-8-sig') as csv_file:
        next(csv_file) #skip first line
        csv_reader = csv.reader(csv_file)
        inputs = []

        for line in csv_reader:
            line_data = []
            line_data.append(getIdx0(line[0]))
            line_data.append(getIdx1(line[1]))
            line_data.append(getIdx2(line[2]))
            line_data.append(getIdx3(line[3]))
            line_data.append(getIdx4(line[4]))
            line_data.append(getIdx5(line[5]))
            line_data.append(getIdx6(line[6]))
            inputs.append(line_data)
             
        training_inputs = np.array(inputs)
        return training_inputs

def get_training_outputs():
    with open("training_outputs.csv", "r", encoding='utf-8-sig') as csv_file:
        next(csv_file) #skip first line
        csv_reader = csv.reader(csv_file)
        outputs = []

        for line in csv_reader:
            outputs.append(int(line[0]))
             
        training_outputs = np.array([outputs]).T
        return training_outputs