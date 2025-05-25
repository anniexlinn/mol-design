# Mol-Design: AI-Driven Pharmaceutical Molecule Generation  
**Machine Learning + Evolutionary Optimization for Drug Discovery**  

## **Project Description**  
**Mol-Design automates the discovery of novel drug candidates** by combining AI and evolutionary algorithms. It generates chemically viable molecules with predicted high activity against biological targets, significantly accelerating early-stage drug discovery.  

**Innovations**:  
- Hybrid ML-evolutionary approach  
- SELFIES-based robust molecular representation  
- Tournament selection for efficient optimization


## Overview  
An end-to-end pipeline for designing novel pharmaceutical molecules using:  
- **Molecular generation** (SMILES/SELFIES)  
- **Machine learning oracles** (RandomForest, XGBoost, SVR) for activity prediction  
- **Evolutionary algorithms** with mutation and selection  
- **Automated optimization** of activity scores  

**Key Features**:  
✔️ RDKit-based descriptor calculation  
✔️ Customizable mutation operators  
✔️ Early stopping via convergence detection  
✔️ Output of diverse, high-activity candidates  

---

## 🔧 Installation  

### Prerequisites  
- Python 3.8+  
- RDKit (requires conda)  

### Steps  
```bash
git clone https://github.com/yourusername/mol-design.git
cd mol-design

# Set up environment (conda recommended)
conda create -n moldesign python=3.8 -y
conda activate moldesign
conda install -c conda-forge rdkit -y

# Install remaining dependencies
pip install -r requirements.txt

