import numpy as np
import pandas as pd
import random
import os

# -----------------------------
# Difficulty Label Logic
# -----------------------------
def generate_difficulty(row):
    score = 0

    if row["enemy_density"] > 70:
        score += 2
    elif row["enemy_density"] > 40:
        score += 1

    if row["health_pickups"] < 3:
        score += 2
    elif row["health_pickups"] < 6:
        score += 1

    if row["accuracy_required"] > 75:
        score += 2
    elif row["accuracy_required"] > 50:
        score += 1

    if row["time_limit"] < 120:
        score += 2
    elif row["time_limit"] < 240:
        score += 1

    if row["map_complexity"] > 7:
        score += 2
    elif row["map_complexity"] > 4:
        score += 1

    if score <= 3:
        return "Easy"
    elif score <= 6:
        return "Medium"
    else:
        return "Hard"


# -----------------------------
# Dataset Generator
# -----------------------------
def generate_dataset(n_samples=1000):
    data = []

    for _ in range(n_samples):
        row = {
            "enemy_density": np.random.randint(10, 100),
            "health_pickups": np.random.randint(1, 10),
            "accuracy_required": np.random.randint(30, 95),
            "time_limit": np.random.randint(60, 400),
            "map_complexity": np.random.randint(1, 10),
        }

        row["difficulty"] = generate_difficulty(row)

        # Label noise
        if random.random() < 0.1:
            row["difficulty"] = random.choice(["Easy", "Medium", "Hard"])

        data.append(row)

    return pd.DataFrame(data)


# -----------------------------
# Main Entry Point
# -----------------------------
if __name__ == "__main__":
    df = generate_dataset(1000)

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/game_difficulty_data.csv", index=False)

    print("Dataset generated and saved to data/raw/")
