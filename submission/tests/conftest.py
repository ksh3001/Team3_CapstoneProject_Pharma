import sys
from pathlib import Path

SUBMISSION = Path(__file__).resolve().parents[1]
if str(SUBMISSION) not in sys.path:
    sys.path.insert(0, str(SUBMISSION))
