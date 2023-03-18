from fastapi import FastAPI, File, UploadFile, Request
from api.endpoints import processing_images
from api.endpoints import processing_text
from utils.save_image_temporal import save_in_disk
from io import BytesIO
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.post("/processing_images")
async def call_processing_images(image: UploadFile = File(...)):
    image_bytes  = await image.read()
    image_path = save_in_disk(image_bytes)
    result = await processing_images.processing_images(image_path)
    return {"message": result}

@app.post("/processing_text")
def call_processing_text(tex: str, request: Request):
    result = processing_text.processing_text(tex, request)
    return {"urls": result}

app.mount("/static", StaticFiles(directory="utils/abc"), name="static")

##@app.get("/")
##async def root():
##  return {"message": "Funcional"}