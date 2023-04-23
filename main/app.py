from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .repository import user_repository
from traceback import print_stack
from .routers import router
from fastapi import FastAPI


class ExceptionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
        except Exception as e:
            print_stack()
            return JSONResponse(str(e), status_code=400)
        return response


app = FastAPI(docs_url='/')


@app.on_event("startup")
def create_user():
    user_repository.create_test_user()


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(str(exc), status_code=401)


app.add_middleware(ExceptionMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router)
