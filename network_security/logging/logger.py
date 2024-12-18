import logging
import os
from datetime import datetime

# Create a log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path for logs folder in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)  # Create logs folder if it doesn't already exist

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging to write logs to the file with a specific format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)