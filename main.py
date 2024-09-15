from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*", "http://localhost:*"],
  allow_credentials=True,
  allow_methods=["*", "http://localhost:*"],
  allow_headers=["*", "http://localhost:*"],
)

currentData = 10000


@app.get("/")
async def read_root():
  return "It's working"


@app.post("/distance-sensor")
async def post_data(request: Request):
  global currentData
  body = await request.body()
  currentData = int(body)
  return f"ok {int(body)}"


@app.get("/distance-sensor")
async def get_current_data():
  return currentData
