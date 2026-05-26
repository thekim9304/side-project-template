from __future__ import annotations

import os
from pathlib import Path


PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT", Path(__file__).resolve().parents[2]))
DATA_DIR = Path(os.getenv("DATA_DIR", PROJECT_ROOT / "data"))
ARTIFACT_DIR = Path(os.getenv("ARTIFACT_DIR", PROJECT_ROOT / "artifacts"))


def get_runtime_summary() -> dict[str, str]:
    return {
        "project_root": str(PROJECT_ROOT),
        "data_dir": str(DATA_DIR),
        "artifact_dir": str(ARTIFACT_DIR),
    }
