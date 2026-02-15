
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(name: str, level: str, log_to_file: bool, log_file: Path) -> logging.Logger:
    """
    Cria um logger padrão:
    - Sempre loga no console
    - Opcionalmente loga em arquivo com rotação (evita log infinito)
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Evita duplicar handlers se você rodar várias vezes
    if logger.handlers:
        return logger

    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # File handler (opcional)
    if log_to_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = RotatingFileHandler(
            filename=str(log_file),
            maxBytes=1_000_000,   # ~1MB
            backupCount=3,        # mantém até 3 arquivos antigos
            encoding="utf-8",
        )
        fh.setLevel(level)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    logger.propagate = False
    return logger
