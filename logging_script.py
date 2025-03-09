import logging
from datetime import datetime

# Log file configuration
LOG_FILE = "sms_backup.log"

# Configure logging
logging.basicConfig(
    # Where it will be logged.
    filename=LOG_FILE,
    # Logging max detailed information.
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_failed_sms(message_body, recipient, error):

    # Logs the date and time, recipient number, and message.
    try:
        # Creates string format to log data.
        log_entry = f"{recipient}|{message_body}|{error}"
        logging.debug(log_entry)
        print(f"Logged failed SMS: {log_entry}")
    except Exception as e:
        # Issues with formating into the log file will be caught here.
        print(f"Error while logging SMS: {e}")

# Just for testing if writing to log file works.
# This is the format inside the log file.
# 2024-11-23 20:37:24,395 - DEBUG - +1234567890|This is a test alert message.|Failed - Network error
if __name__ == "__main__":
    # Test logging a failed SMS
    test_message = "This is a test alert message."
    test_recipient = "+1234567890"
    test_error = "Failed - Network error"

    log_failed_sms(test_message, test_recipient, test_error)
