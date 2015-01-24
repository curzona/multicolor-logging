import logging
from multicolor import ColorFormatter, Fore

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
logger.addHandler(handler)

formatter = ColorFormatter('{startcolor}%(asctime)s %(levelname)s:{endcolor} %(message)s')
formatter.addColor(Fore.GREEN, levelno=logging.INFO)
formatter.addColor(Fore.YELLOW, levelno=logging.ERROR)
formatter.addColor(Fore.CYAN, levelno=logging.DEBUG)
handler.setFormatter(formatter)

logger.info("This is some info")
logger.debug("This is some debug")
logger.error("This is serious!")

