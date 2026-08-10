from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

Mode = Literal["deterministic_offline", "ai_disabled"]


@dataclass(frozen=True)
class RuntimeMode:
    mode: Mode = "deterministic_offline"
    llm_enabled: bool = False

    @classmethod
    def from_request(cls, mode: str | None) -> "RuntimeMode":
        m: Mode = "ai_disabled" if mode == "ai_disabled" else "deterministic_offline"
        return cls(mode=m, llm_enabled=False)

    def refuse_narrator(self) -> bool:
        return True

    def allow_llm_call(self) -> bool:
        return False
