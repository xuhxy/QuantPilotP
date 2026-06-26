from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.add(
    LOG_DIR / "quantpilot.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

__all__ = ["logger"]