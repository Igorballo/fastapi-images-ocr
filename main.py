from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract
import pdf2image


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def extract_text_from_pdf(file: UploadFile):
    images = pdf2image.convert_from_bytes(file.file.read())
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        print(text)
        full_text += text
    return full_text

    
@app.post("/extract-pdf-text")
async def extract_pdf_text(file: UploadFile = File(...)):
    pdf_text = extract_text_from_pdf(file)
    return {"message": pdf_text}