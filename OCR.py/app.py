from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_image():
    text = ""
    if request.method == "POST":
        if "image" not in request.files:
            return "No file uploaded"
        file = request.files["image"]
        if file.filename == "":
            return "No selected file"
        
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Open image & extract text
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img)

    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
