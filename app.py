import os
from flask import Flask, render_template

# Create Flask app with explicit template and static folders
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend", "templates")
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend", "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Register blueprints
from backend.routes.api import recommend_bp
app.register_blueprint(recommend_bp)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

