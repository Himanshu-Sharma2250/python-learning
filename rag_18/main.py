from .server import app
import uvicorn
from dotenv import load_dotenv

load_dotenv()

def main():
    uvicorn.run(app, port=4000, host='localhost')

main()

# to run the server : (in root) -> python -m rag_18.main

# faced problem in this because : os is importing some attribute which is not present in windows and to solve this we use this 
# to run the worker : (in root) -> rq worker --worker-class rq.worker.SimpleWorker
# but again i faced some error, which is telling me that 18_rag is wrong, so I have to change it to rag_18  