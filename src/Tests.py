from loguru import logger
import sys

logger.warning("That's it, beautiful and simple logging!")

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>", filter="my_module", level="Info")

logger.Info("yada yada!!")