from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Full Stack AI Lab - CI/CD Working!"

# Health check route (optional but useful for deployment)
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


# Run only in local development
if __name__ == "__main__":
    app.run(debug=True)