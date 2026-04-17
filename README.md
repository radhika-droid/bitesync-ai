# BiteSync AI 🥗

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: WIP](https://img.shields.io/badge/status-WIP-orange.svg)](https://github.com/radhika-droid/bitesync-ai)

BiteSync AI is a smart food recommendation and nutrition assistant that helps users make better food choices based on their health goals.

The platform helps users:

- Decide what to eat based on goals (weight loss, gain, maintenance)
- Get personalized food recommendations
- Track calories and nutrition
- Plan meals
- Improve diet and lifestyle

**Long-term vision:** Complete AI-powered food assistant with LLM-powered recommendations, recipe generation, grocery lists, and personalized insights.

## 🚀 Quick Start

```bash
cd e:/bitesync-ai
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in browser.

## ✨ Features

### Current

- Food recommendation system
- Goal & diet preference selection
- Basic calorie/nutrition tracking
- Meal planning UI
- Responsive frontend

### Planned

- AI/LLM recommendations
- Personalized meal plans
- Recipe suggestions
- Grocery lists
- Progress dashboard
- User authentication

## 🛠 Tech Stack

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Python, Flask  
**ML:** Pandas, NumPy, Scikit-learn

## 📁 Project Structure

```
bitesync-ai/
├── app.py                 # Flask app entrypoint
├── requirements.txt
├── README.md
├── TODO.md
│
├── backend/               # Backend services
│   ├── model/
│   │   └── predict.py
│   └── utils/
│       └── calorie_db.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/styles.css
│       └── js/script.js
│
├── data/                  # Datasets (add sample_food_dataset.csv)
├── docs/
│   └── project-overview.md
└── .env.example
```

Note: The structure may evolve as new features are added.

## 📦 Installation (Detailed)

### 1. Clone/Fork

```bash
git clone https://github.com/radhika-droid/bitesync-ai.git
cd bitesync-ai
```

### 2. Virtual Env (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python app.py
```

## 📊 Example Dataset (data/sample_food_dataset.csv)

```csv
food_name,calories,protein,carbs,fat,goal_type
Oats,150,5,27,3,weight_loss
Banana Shake,300,8,45,6,weight_gain
Salad,120,3,10,5,maintenance
Chicken Breast,220,35,0,5,weight_loss
Peanut Butter Sandwich,350,12,30,18,weight_gain
```

## 🎯 User Flow

1. Select goal (weight loss/gain/maintenance)
2. Choose diet prefs
3. Get AI-powered recommendations
4. Track calories & plan meals

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

**Branch:** `feature/short-desc`  
**Commit:** `feat: add feature`

## 📄 License

[MIT License](LICENSE) © 2024 BiteSync AI

## 👥 Maintainer

[radhika-droid](https://github.com/radhika-droid)
