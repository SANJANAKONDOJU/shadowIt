# from flask import Blueprint, request, jsonify
# from services.analytics_engine import generate_dashboard_data
# from services.shodan_service import search_assets
# from services.risk_engine import enrich_assets_with_risk

# dashboard_bp = Blueprint("dashboard", __name__)

# # @dashboard_bp.route("/api/dashboard", methods=["POST"])
# # def dashboard():
# #     data = request.json
# #     target = data.get("target")

# #     assets = search_assets(target)
# #     enriched = enrich_assets_with_risk(assets)

# #     dashboard_data = generate_dashboard_data(enriched)

# #     return jsonify(dashboard_data)
# @dashboard_bp.route("/api/dashboard", methods=["POST"])
# def dashboard():
#     data = request.json

#     if not data or "target" not in data:
#         return jsonify({"error": "Target is required"}), 400

#     target = data.get("target")

#     if not target:
#         return jsonify({"error": "Invalid target"}), 400

#     assets = search_assets(target)
#     enriched = enrich_assets_with_risk(assets)

#     dashboard_data = generate_dashboard_data(enriched)

#     return jsonify(dashboard_data)
from flask import Blueprint, request, jsonify
from services.shodan_service import search_assets
from services.risk_engine import enrich_assets_with_risk
from services.analytics_engine import generate_dashboard_data
from services.logger import log_event

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/api/dashboard", methods=["POST"])
def dashboard():
    try:
        data = request.json

        # Validate request body
        if not data or "target" not in data:
            return jsonify({"error": "Target is required"}), 400

        target = data.get("target")

        if not target or target.strip() == "":
            return jsonify({"error": "Invalid target"}), 400

        # Log dashboard request
        log_event(f"Dashboard analytics requested for target: {target}")

        # Fetch assets (real Shodan or fallback)
        assets = search_assets(target)

        # Add risk classification
        enriched = enrich_assets_with_risk(assets)

        # Generate analytics
        dashboard_data = generate_dashboard_data(enriched)

        # Attach target for clarity
        dashboard_data["target"] = target

        return jsonify(dashboard_data), 200

    except Exception as e:
        log_event(f"Dashboard error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500