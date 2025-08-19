from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from schemas.user_input import InputData 
from model.predict import predict_output

app = FastAPI(
    docs_url=None,
    redoc_url=None
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/api/predict")
def process_input(data: InputData):

    user_input = {
        "sector": data.sector,
        "bedRoom": data.bedRoom,
        "bathroom": data.bathroom,
        "balcony": data.balcony,
        "agePossession": data.agePossession,
        "built_up_area": data.built_up_area,
        "servant_room": data.servant_room,
        "furnishing_type": data.furnishing_type,
        "luxury_category": data.luxury_category,
        "floor_category": data.floor_category
    }

    try:
        prediction = predict_output(user_input)

        if prediction >= 1:
            # 1 crore or more
            price = f"{prediction:.2f} Crore"
        else:
            # Less than 1 crore, show in Lacs
            lacs = prediction * 100
            price = f"{lacs:.0f} Lac"

        return JSONResponse(status_code = 200, content={'price':price})
    except Exception as e:
        return JSONResponse(status_code = 500, content = str(e))