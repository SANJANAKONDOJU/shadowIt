from flask import Flask
from flask_cors import CORS
from routes.scan_routes import scan_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(scan_bp)
app.register_blueprint(dashboard_bp)

@app.route("/api/health")
def health():
    return {"status": "Backend Running"}
 
@app.errorhandler(Exception)
def handle_exception(e):
    return {"error": "Internal Server Error"}, 500
 
if __name__ == "__main__":
    app.run(debug=True)