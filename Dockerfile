FROM python:alpine3.21
RUN pip install uvicorn fastapi
COPY app.py app.py
EXPOSE 8080
ENTRYPOINT ["python","app.py"]
