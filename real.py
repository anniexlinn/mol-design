import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import trange
from rdkit import Chem, rdBase
from rdkit.Chem.rdchem import Mol
# import tdc
# from tdc import Evaluator
# from tdc.generation import MolGen
# from rdkit import RDLogger
# RDLogger.DisableLog('rdApp.*')

from rdkit.Chem import rdFingerprintGenerator
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

from xgboost import XGBClassifier
from rdkit import DataStructs
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

import random
from typing import List
import os
import yaml
import wget
import joblib

data = pd.read_csv('initial.csv')
data
smiles_list = data['smiles'].tolist() # extracts smiles column from data

def generate_fingerprints(smiles_list, fp_type, fp_size):
  """
    Generate molecular fingerprints given SMILES
  """
  if fp_type == 'morgan':
      fp_gen = rdFingerprintGenerator.GetMorganGenerator(radius=3, fpSize=fp_size)
  elif fp_type == 'rdkit':
      fp_gen = rdFingerprintGenerator.GetRDKitFPGenerator(fpSize=fp_size)
  elif fp_type == 'atom_pair':
      fp_gen = rdFingerprintGenerator.GetAtomPairGenerator(fpSize=fp_size)
  elif fp_type == 'topological_torsion':
      fp_gen = rdFingerprintGenerator.GetTopologicalTorsionGenerator(fpSize=fp_size)
  
  fps = [] # store fingerprints
  smiles_og = [] # store orignial SMILES strings
  for smile in smiles_list:
    smiles_og.append(smile)
    mol = Chem.MolFromSmiles(smile)
    if mol is not None:
      fp = fp_gen.GetFingerprint(mol)
      # convert fingerprint to numpy array
      arr = np.zeros((0,), dtype=int) 
      DataStructs.ConvertToNumpyArray(fp, arr)
      fps.append(arr) # append fingerprint to list
    else:
      fps.append(np.zeros(fp_size, dtype=int)) # if molecule invalid, append 0 to numpy list

  return np.array(fps), smiles_og
  print(np.array)


  
