


import os
import yaml
import numpy as np
import pandas as pd


from dotenv import load_dotenv
from datetime import datetime

from typing import Dict, List, Union, Set, Optional

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, Field
from fastapi import APIRouter

# from backend_service.routers.general.general import router as general
# from backend_service.routers.access.access import router as access

from routers.general.general import router as general
from routers.access.access import router as access
from routers.postgres_ideefix.postgres_ideefix import router as postgres_ideefix

app = FastAPI()


# Configure CORS
origins = [
    "http://localhost:8080",  # Add your frontend URL here
    "http://localhost:5173",   # Add your Vue.js frontend URL here
    "http://127.0.0.1:8080"   # Add your frontend URL here
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(general, tags=["General"])
app.include_router(access, tags=["Access"])
# app.include_router(postgres_ideefix, tags=["Postgres_Ideefix"])


app.include_router(postgres_ideefix, prefix="/api", tags=["ideefix"])







