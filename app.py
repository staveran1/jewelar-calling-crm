import os
from flask import Flask, Response

app = Flask(__name__)
HERE = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    """Serve the single-page Wholesale Calling CRM dashboard."""
    with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
        return Response(f.read(), mimetype="text/html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # Railway provides PORT; fall back to 5000 for local runs.
    port = int(os.environ.get("PORT", 5000))
    print("Wholesale Calling CRM running on port", port)
    app.run(host="0.0.0.0", port=port)
