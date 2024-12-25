


import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()
local_run = os.getenv("LOCAL_RUN")


# http://127.0.0.1:8000 


if __name__ == "__main__":

    if local_run:
        uvicorn.run(
            "backend_service.main:app",
            port=8000,
            host="localhost",
            reload=True
        )
    else:
        uvicorn.run(
            "backend_service.main:app",
            port=8050,
            host="localhost",
            reload=True
        )

