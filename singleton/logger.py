


class Logger(object):
    """A file-based message logger with the following properties
    
    Attributes:
        file_name: a string representation the full path the log file to which
    this logger will write its message
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def _write_log(self, level, msg):

        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")
    
    def critical(self, level, msg):
        self._write_log("CRITICAL", msg)
    
    def error(self, level, msg):
        self._write_log("ERROR", msg)

    def warn(self, level, msg):
        self._write_log("WARN", msg)

    def info(self, level, msg):
        self._write_log("INFO", msg)

    def debug(self, level, msg):
        self._write_log("DEBUG", msg)

