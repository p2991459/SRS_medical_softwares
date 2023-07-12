import os
from datetime import datetime, timedelta
import pytz
debug_level = os.getenv("DEBUG_LEVEL")
if debug_level is None:
    debug_level = "INFO"
print(f"LOG Level: {debug_level}")

class Logger:
    def __init__(self, class_name):
        self._class_name = class_name

    def _get_current_time(self):
        current_time = datetime.utcnow()
        ist = pytz.timezone('Asia/Kolkata')
        current_time_ist = current_time.replace(tzinfo=pytz.utc).astimezone(ist)
        formatted_time = current_time_ist.strftime("%d:%m:%Y %H:%M:%S")
        return formatted_time
    def _print_message(self, message: str, is_error=False):
        if is_error:
            print(f"ERROR - [{self._class_name[0:30]}]: {message}")
        else:
            logMessage = f"\n[{self._get_current_time()}] - {debug_level.upper()} - [{self._class_name[0:20]}]: {message}\n"
            file = open("logs.txt","a+")
            file.write(logMessage)
            file.flush()
            print(logMessage)

    def info(self, message: str):
        self._print_message(message, False)

    def debug(self, message: str):
        if debug_level.upper() == "DEBUG":
            self._print_message(message, False)

    def error(self, message: str):
        self._print_message(message, True)
