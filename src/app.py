from fastapi import FastAPI, UploadFile, File
import shutil
from inference import predict_image

app = FastAPI()

@app.post("/classify")
async def classify(file: UploadFile = File(...)):

    file_location = "temp.jpg"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    predictions = predict_image(file_location)

    top_class = predictions[0][0]
    top_conf = predictions[0][1]

    return {
        "disease": top_class.replace("___", " ").replace("_", " "),
        "confidence": round(top_conf, 2),
        "all_predictions": {
            p[0].replace("___", " ").replace("_", " "): float(p[1])
            for p in predictions[:5]
        },
        "note": "For best results upload a clear close-up image of a single leaf with minimal background."
    }
@app.get("/")
def home():
    return {"status": "Plant Disease API Running"}
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
