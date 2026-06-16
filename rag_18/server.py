from fastapi import FastAPI, Query
from .queue.worker import process_query
from .client.rq_client import queue

app = FastAPI()

@app.get("/")
def root():
    return { "status": "Server is Up and Running" }

@app.post("/chat")
def chat( query: str = Query(..., description="The chat query of user") ):
    job = queue.enqueue(process_query, query)

    return { "status": "queued", "job_id": job.id }

@app.get("/job-status")
def get_result( job_id: str = Query(..., description="Job Id") ):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value() # type: ignore

    return { "result": result }