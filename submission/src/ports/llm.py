from __future__ import annotations

CALL_COUNT = 0


class NoOpLLM:
    def complete(self, *args, **kwargs):
        global CALL_COUNT
        CALL_COUNT += 1
        raise RuntimeError("LLM disabled in assessed deterministic path")


def reset_call_count() -> None:
    global CALL_COUNT
    CALL_COUNT = 0


def call_count() -> int:
    return CALL_COUNT
