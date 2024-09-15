from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
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
