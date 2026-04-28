from flask import Blueprint, request, jsonify
from backend.services.recommendation_service import get_recommendations

recommend_bp = Blueprint("recommend", __name__, url_prefix="/api")


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    """
    POST /api/recommend
    Body JSON:
    {
        "goal": "weight_loss",
        "diet": "all",          // optional: veg | non-veg | all
        "sort_by": "calories",  // optional column name
        "top_n": 5              // optional int
    }
    """
    data = request.get_json(silent=True) or {}

    goal = data.get("goal")
    diet = data.get("diet", "all")
    sort_by = data.get("sort_by")
    top_n = data.get("top_n", 5)

    # Validate top_n
    try:
        top_n = int(top_n)
        if top_n < 1:
            top_n = 5
    except (ValueError, TypeError):
        top_n = 5

    try:
        results = get_recommendations(goal=goal, diet=diet, sort_by=sort_by, top_n=top_n)
    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400
    except FileNotFoundError as fe:
        return jsonify({"success": False, "error": str(fe)}), 500
    except Exception as e:
        return jsonify({"success": False, "error": "An unexpected error occurred.", "details": str(e)}), 500

    return jsonify({
        "success": True,
        "count": len(results),
        "goal": goal,
        "diet": diet,
        "recommendations": results
    }), 200

