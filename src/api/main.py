from fastapi import FastAPI

from src.common.paths import get_runtime_summary


app = FastAPI(
    title="AI Side Project Template API",
    version="0.1.0",
    description="Bootstrap API for experiments, demos, and lightweight services.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/meta/runtime")
def runtime_meta() -> dict[str, str]:
    return get_runtime_summary()
