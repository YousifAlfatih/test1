from pathlib import Path
from uuid import uuid4

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.post("/upload")
def upload_file() -> tuple[str, int] | str:
    file = request.files.get("file")

    if file is None or file.filename == "":
        return render_template("index.html", error="Please choose a file before uploading."), 400

    original_name = secure_filename(file.filename)
    unique_name = f"{uuid4().hex}_{original_name}"
    destination = UPLOAD_DIR / unique_name
    file.save(destination)

    return render_template(
        "index.html",
        success=f"Uploaded '{original_name}' successfully.",
        stored_path=str(destination.relative_to(BASE_DIR)),
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
