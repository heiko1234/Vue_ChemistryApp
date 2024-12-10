


import os
import yaml
import numpy as np
import pandas as pd


from dotenv import load_dotenv
from datetime import datetime

from typing import Dict, List, Union, Set, Optional

from fastapi import FastAPI, Depends, Request

from pydantic import BaseModel, Field
from fastapi import APIRouter

# from backend_service.routers.general.general import router as general
# from backend_service.routers.access.access import router as access

from routers.general.general import router as general
from routers.access.access import router as access

app = FastAPI()



app.include_router(general, tags=["General"])
app.include_router(access, tags=["Access"])










