# test1
# Python File Upload Website

A small local web app that lets you upload files from your browser and saves them to an `uploads/` folder.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open `http://127.0.0.1:8000` in your browser.

## Notes

- Uploaded files are stored in `uploads/`.
- File names are sanitized and prefixed with a UUID to avoid collisions.
- Max upload size is 16 MB.
