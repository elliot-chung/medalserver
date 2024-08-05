from process import medals_per_100_athletes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:5173",
    "https://olympicmedals2024.vercel.app",
]

app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def medals():
    data = medals_per_100_athletes()
    return data

@app.get("/healthcheck")
def health_check():
     return {"status": "ok"}


