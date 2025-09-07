from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry
import time
import uvicorn

app = FastAPI()
registry = CollectorRegistry()
counter = Counter("siva_requests_total","Total number of requests", ["method","endpoint","statuscode"],registry=registry)

@app.middleware("http")
async def prometheus_metrics_middleware(request: Request, call_next):
   method = request.method
   endpoint = request.url.path
   response = await call_next(request)
   statuscode=str(response.status_code)
   counter.labels(method=method,endpoint=endpoint,statuscode=statuscode).inc()
   return response

@app.get("/")
def test():
    message = "default message from canary"
    return message
@app.get("/user/{username}")
def username(username: str):
    message = "Post default canary username "+username
    return message
@app.get("/item/{itemid}")
def itemid(itemid: int):
    message = "canary Item id "+ itemid
    return message

@app.get("/metrics")
def metrics():
    return Response(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8080)
