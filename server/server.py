import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from utils import PromptRequest, CompletionRequest, predict, autocomplete


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the code assistant server!"}


@app.post("/prompt")
async def get_prediction(request: PromptRequest):
    try:
        return StreamingResponse(
            predict(request.prompt, request.files), media_type="text/plain"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"[/prompt] - error processing request: {str(e)}"
        )


@app.post("/autocomplete")
async def get_autocomplete(request: CompletionRequest):
    try:
        return StreamingResponse(
            autocomplete(request.context_before, request.context_after),
            media_type="text/plain",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"[/autocomplete] - error processing request: {str(e)}",
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
