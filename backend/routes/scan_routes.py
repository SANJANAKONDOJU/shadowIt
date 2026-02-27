# from flask import Blueprint, request, jsonify
# from services.shodan_service import search_assets
# from services.risk_engine import enrich_assets_with_risk

# scan_bp = Blueprint("scan", __name__)

# @scan_bp.route("/api/scan", methods=["POST"])
# def scan():
#     data = request.json
#     target = data.get("target")

#     assets = search_assets(target)
#     enriched = enrich_assets_with_risk(assets)

#     high = sum(1 for a in enriched if a["risk"] == "High")
#     medium = sum(1 for a in enriched if a["risk"] == "Medium")
#     low = sum(1 for a in enriched if a["risk"] == "Low")

#     return jsonify({
#         "total_assets": len(enriched),
#         "high_risk": high,
#         "medium_risk": medium,
#         "low_risk": low,
#         "assets": enriched
#     })
from flask import Blueprint, request, jsonify
from services.shodan_service import search_assets
from services.risk_engine import enrich_assets_with_risk
from services.logger import log_event

scan_bp = Blueprint("scan", __name__)

@scan_bp.route("/api/scan", methods=["POST"])
def scan():
    try:
        data = request.json

        # Validate request body
        if not data or "target" not in data:
            return jsonify({"error": "Target is required"}), 400

        target = data.get("target")

        if not target or target.strip() == "":
            return jsonify({"error": "Invalid target"}), 400

        # Log scan event
        log_event(f"Scan requested for target: {target}")

        # Get assets from Shodan (or mock fallback)
        assets = search_assets(target)

        # Enrich assets with risk classification
        enriched = enrich_assets_with_risk(assets)

        # Calculate risk counts
        high = sum(1 for a in enriched if a["risk"] == "High")
        medium = sum(1 for a in enriched if a["risk"] == "Medium")
        low = sum(1 for a in enriched if a["risk"] == "Low")

        response = {
            "target": target,
            "total_assets": len(enriched),
            "high_risk": high,
            "medium_risk": medium,
            "low_risk": low,
            "assets": enriched
        }

        return jsonify(response), 200

    except Exception as e:
        log_event(f"Scan error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500