# imports
import os
import csv
import sys
from rdkit import Chem
import lazyqsar as lq

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
MODELPATH = os.path.join(root, "..", "..", "checkpoints")


# my model
def my_model(smiles_list):

    
    mdl1 = lq.LazyBinaryQSAR.load_model(os.path.join(MODELPATH, "osm_all_bin1"))
    mdl2 = lq.LazyBinaryQSAR.load_model(os.path.join(MODELPATH, "osm_all_bin25"))

    y_pred1 = mdl1.predict_proba(smiles_list)[:,1]
    y_pred2 = mdl2.predict_proba(smiles_list)[:,1]

    return y_pred1, y_pred2


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output1, output2 = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["IC50_1uM".lower(), "IC50_2point5uM".lower()])  # header with column names
    for o1, o2 in zip(output1, output2):
        writer.writerow([o1, o2])