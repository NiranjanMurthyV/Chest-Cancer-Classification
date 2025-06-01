import sys
import os
sys.path.append(os.path.join(os.getcwd(), "src"))

from cnnClassifier import logger

logger.info("Logger working without export command!")