from flask import Flask
import os, requests
app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "1")
ENV = os.environ.get("APP_ENV", "DEV")
BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:8080")
@app.route("/")
def home():
    try:
        r = requests.get(f"{BACKEND_URL}/api/data", timeout=3)
        backend = r.json()
    except Exception as e:
        backend = {"status": "unreachable", "error": str(e)}
    return f"""<html><title>Container Demo - {ENV}</title>
<body style='font-family:sans-serif'>
<h1>AWS Container Demo - via CodePipeline</h1>
<h2>Frontend - {ENV} - Version {VERSION}</h2>
<p>Frontend -> Backend call via service discovery / Istio mesh</p>
<pre>{backend}</pre>
</body></html>"""
@app.route("/health")
def health():
    return {"status": "healthy"}, 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
