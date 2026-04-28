import os
import pandas as pd

# Use absolute path relative to this file's location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample_food_dataset.csv")

VALID_GOALS = {"weight_loss", "weight_gain", "maintenance"}
VALID_DIETS = {"veg", "non-veg", "all"}


def get_recommendations(goal, diet="all", sort_by=None, top_n=5):
    """
    Return filtered food recommendations based on goal and optional diet preference.

    Parameters:
        goal (str): One of 'weight_loss', 'weight_gain', 'maintenance'
        diet (str): 'veg', 'non-veg', or 'all' (default)
        sort_by (str): Optional column name to sort results
        top_n (int): Max number of results to return

    Returns:
        list[dict]: List of food recommendation dictionaries
    """
    if not goal:
        raise ValueError("Goal is required.")

    goal = str(goal).strip().lower()
    if goal not in VALID_GOALS:
        raise ValueError(f"Invalid goal '{goal}'. Choose from: {', '.join(VALID_GOALS)}")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Filter by goal
    filtered = df[df["goal_type"] == goal]

    # Filter by diet preference if provided and column exists
    diet = str(diet).strip().lower() if diet else "all"
    if diet != "all" and "diet_type" in filtered.columns:
        filtered = filtered[filtered["diet_type"] == diet]

    # Optional sorting
    if sort_by and sort_by in filtered.columns:
        filtered = filtered.sort_values(by=sort_by, ascending=True)

    # Limit results
    result_df = filtered.head(top_n)

    # Convert to list of dicts and handle NaN values
    records = result_df.fillna("").to_dict(orient="records")
    return records

