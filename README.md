# 🎮 Game Difficulty Classifier (ML System)

A multiclass machine learning system that automatically classifies game levels
into **Easy**, **Medium**, or **Hard** based on gameplay parameters.  
The project focuses on **data synthesis, explainable ML, and safe error analysis**
for game balancing.

---

## 🚀 Motivation

Manual game difficulty balancing is subjective, time-consuming, and hard to scale.
This project explores how machine learning can assist game designers by
**automating difficulty classification** using measurable level attributes.

The emphasis is not just on prediction accuracy, but on:
- Correct label design
- Explainability
- Safe vs dangerous failure analysis

---

## 🧠 Problem Definition

**Input:** Gameplay parameters of a level  
**Output:** Difficulty class → `Easy`, `Medium`, or `Hard`

This is modeled as a **multiclass classification problem**.

---

## 📊 Features Used

| Feature | Description |
|------|------------|
| `enemy_density` | Number of enemies per unit area |
| `health_pickups` | Available health items in the level |
| `accuracy_required` | Player accuracy (%) needed to succeed |
| `time_limit` | Time allowed to complete the level (seconds) |
| `map_complexity` | Structural complexity of the map (1–10) |

---

## 🧪 Project Phases

### Phase 1: Data Synthesis & Label Engineering
- Designed rule-based difficulty logic to generate synthetic gameplay data
- Introduced controlled label noise to simulate real-world inconsistencies
- Output: Structured dataset with engineered difficulty labels

### Phase 2: Exploratory Data Analysis (EDA)
- Validated difficulty boundaries using boxplots and pair plots
- Identified overlap between Medium and Hard levels
- Verified feature usefulness before model training

### Phase 3: Model Training
- Trained a **Random Forest classifier** for multiclass prediction
- Used stratified train-test split and balanced class weights
- Evaluated using **confusion matrix, precision, recall, and macro F1-score**

### Phase 4: Model Packaging & Inference
- Persisted trained model and label encoder using `joblib`
- Built a reusable inference pipeline for new game levels
- Performed **safe vs dangerous error analysis** to assess gameplay risk

---

## 🌲 Model Details

- **Algorithm:** Random Forest Classifier  
- **Why Random Forest?**
  - Handles nonlinear feature interactions
  - Robust to noisy labels
  - Provides built-in feature importance for explainability

---

## 📈 Key Results & Insights

- Achieved strong multiclass performance with high macro F1-score
- Most misclassifications occurred between **Medium ↔ Hard** (acceptable)
- Rarely misclassified **Hard → Easy**, preventing game-breaking outcomes
- **Enemy density** and **time limit** were the strongest difficulty drivers

---

## ⚠️ Error Analysis (Why This Matters)

Not all errors are equal in games:

- ❌ **Hard → Easy**: Dangerous (breaks game balance)
- ✅ **Hard → Medium**: Acceptable (minor tuning issue)

This project explicitly analyzes such failure modes instead of relying on accuracy alone.

---

## 🧪 Example Inference

```python
sample_level = {
    "enemy_density": 80,
    "health_pickups": 2,
    "accuracy_required": 78,
    "time_limit": 110,
    "map_complexity": 8
}

Predicted Difficulty: Hard

##🛠 Tech Stack

Python 3.11

NumPy, Pandas

Matplotlib, Seaborn

Scikit-learn

Jupyter Notebook

game-difficulty-classifier/
│
├── data/
│   └── raw/
├── notebooks/
│   ├── 02_eda.ipynb
│   └── 03_model_training.ipynb
├── src/
│   ├── data_generator.py
│   └── predict.py
├── models/
│   ├── random_forest.pkl
│   └── label_encoder.pkl
├── requirements.txt
└── README.md

##Future Improvements

Hyperparameter tuning with cross-validation

Adaptive difficulty adjustment (dynamic gameplay)

REST API using FastAPI for real-time inference

Integration with a game engine pipeline

