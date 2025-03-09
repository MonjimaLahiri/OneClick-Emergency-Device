import logging
from sms_send import send_sms  # Import send_sms from the first script
from datetime import datetime

LOG_FILE = "sms_backup.log"

def readFile():
    failed_sms = []

    try:
        with open(LOG_FILE, "r") as log_file:
            lines = log_file.readlines()
            for line in lines:
                if "Failed" in line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        recipient = parts[0].strip()
                        message_body = parts[1].strip()
                        error = parts[2].strip()
                        failed_sms.append((recipient, message_body, error))

        return failed_sms

    except Exception as e:
        print(f"Error reading log file: {e}")
        return []

def deleteLogMessage(recipient, message_body, error):
    try:
        with open(LOG_FILE, "r") as log_file:
            lines = log_file.readlines()
        
        with open(LOG_FILE, "w") as log_file:
            for line in lines:
                if not (recipient in line and message_body in line and error in line):
                    log_file.write(line)
    
    except Exception as e:
        print(f"Error updating log file: {e}")

def resend_failed_sms():
    failed_sms = readFile()

    for recipient, message_body, error in failed_sms:
        print(f"Resending message to {recipient}: {message_body} (Error: {error})")

        if send_sms(recipient, message_body):
            print(f"Successfully resent message to {recipient}. Removing from log.")
            deleteLogMessage(recipient, message_body, error)


def main():
    failed_entries = readFile()
    print("These are the failed entries in the log file:")
    for entry in failed_entries:
        print(f"Recipient: {entry[0]}, Message: {entry[1]}, Error: {entry[2]}")

# Execute main function to see failed entries (optional)
if __name__ == "__main__":
    main()