from __future__ import annotations
import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
from src.paths import METRICS_DIR


@dataclass
class MetricsEvent:
    name: str
    request_id: str
    workflow: str
    started_ms: float
    ended_ms: float = 0.0
    side_effect_count: int = 0
    conflict_count: int = 0
    authz_decision: str = ""
    readiness_state: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


class MetricsCollector:
    def start(self, name: str, request_id: str, workflow: str) -> MetricsEvent:
        return MetricsEvent(
            name=name, request_id=request_id, workflow=workflow, started_ms=time.time() * 1000
        )

    def emit(self, event: MetricsEvent) -> Path:
        event.ended_ms = time.time() * 1000
        path = METRICS_DIR / f"{event.request_id}_{event.workflow}.json"
        path.write_text(json.dumps(asdict(event), indent=2), encoding="utf-8")
        return path
