from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Ensure we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import get_metrics, check_alerts, load_config

app = FastAPI(title="System Health Monitor API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    try:
        metrics = get_metrics()
        if not metrics:
            raise HTTPException(status_code=500, detail="Failed to collect metrics")
        
        config = load_config()
        alerts = check_alerts(metrics, config)
        
        return {
            "status": "HEALTHY" if not alerts else "WARNING",
            "metrics": metrics,
            "alerts": alerts
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
