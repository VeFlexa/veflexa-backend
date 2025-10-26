from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import prices, optimize

app = FastAPI(
    title="VeFlexa API",
    description="Backend for electric fleet smart charging optimizer",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego restringimos a veflexa.com
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prices.router, prefix="/api/v1/prices", tags=["Prices"])
app.include_router(optimize.router, prefix="/api/v1/optimize", tags=["Optimization"])

@app.get("/")
def root():
    return {"message": "Welcome to VeFlexa API"}
