from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.iris_reader_service import IrisReaderService
import uvicorn

app = FastAPI()
iris_service = IrisReaderService()

class EnrollRequest(BaseModel):
    user_id: str

class IdentifyResponse(BaseModel):
    user_id: str | None = None
    confidence: float = 0
    message: str | None = None

@app.on_event("startup")
async def startup_event():
    if not iris_service.initialize_camera():
        raise Exception("Failed to initialize camera")

@app.on_event("shutdown")
async def shutdown_event():
    iris_service.release_camera()

@app.post("/enroll", response_model=str)
async def enroll_user(request: EnrollRequest):
    try:
        return iris_service.enroll_user(request.user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/identify", response_model=IdentifyResponse)
async def identify_user():
    try:
        user_id, confidence = iris_service.identify_user()
        if user_id:
            return IdentifyResponse(user_id=user_id, confidence=confidence)
        else:
            return IdentifyResponse(message="No match found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

