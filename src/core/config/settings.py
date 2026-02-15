from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    # Pasta base do projeto (ajusta a partir de src/)
    base_dir: Path

    # Logs
    log_level: str = "INFO"
    log_to_file: bool = True
    log_dir_name: str = "logs"
    log_file_name: str = "app.log"

    @property
    def log_dir(self) -> Path:
        return self.base_dir / self.log_dir_name

    @property
    def log_file(self) -> Path:
        return self.log_dir / self.log_file_name


def load_settings() -> Settings:
    """
    Carrega configurações a partir de variáveis de ambiente, com defaults.
    """
    # base_dir = pasta "src" (suba um nível a partir de core/config)
    base_dir = Path(__file__).resolve().parents[2]

    log_level = os.getenv("APP_LOG_LEVEL", "INFO").upper()
    log_to_file = os.getenv("APP_LOG_TO_FILE", "1") in ("1", "true", "True", "yes", "YES")

    return Settings(
        base_dir=base_dir,
        log_level=log_level,
        log_to_file=log_to_file,
    )

