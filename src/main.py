from core.config.settings import load_settings
from core.logs.logger import setup_logger


def main():
    settings = load_settings()

    logger = setup_logger(
        name="automation-bot",
        level=settings.log_level,
        log_to_file=settings.log_to_file,
        log_file=settings.log_file,
    )

    logger.info("Python Automation Bot - Demo Version")
    logger.info("Project initialized successfully.")
    logger.info(f"Log level: {settings.log_level}")
    logger.info(f"Logging to file: {settings.log_to_file}")
    logger.info(f"Log file path: {settings.log_file}")


if __name__ == "__main__":
    main()
