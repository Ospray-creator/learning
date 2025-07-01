from fastapi import FastAPI

app = FastAPI(title="MCP LM Server")

@app.get("/")
def health_check():
    return {"status": "running"}

# Placeholder endpoints for integration

