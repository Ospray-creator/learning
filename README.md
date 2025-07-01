# MCP LM Server

A minimal server skeleton for integrating MCP LM Studio with Paperless-ngx.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server using `uvicorn`:
   ```bash
   uvicorn src.main:app --reload
   ```

The server currently exposes a single health check endpoint at `/` and contains
placeholder clients for MCP LM Studio and Paperless-ngx.
