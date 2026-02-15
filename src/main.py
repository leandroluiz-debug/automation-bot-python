from core.logs.logger import get_logger
from core.config.settings import APP_NAME, VERSION

logger = get_logger()

def main():
    logger.info(f"Iniciando {APP_NAME} v{VERSION}")
    logger.info("Sistema inicializado com sucesso.")

if __name__ == "__main__":
    main()
