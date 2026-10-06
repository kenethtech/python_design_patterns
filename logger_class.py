from datetime import datetime, UTC
class Logger(object):

    def __init__(self, filename):
        self.filename = filename
        self.now = datetime.now(UTC)

    def _write_log(self, level, msg):
        with open(self.filename, "a") as log_file:
            log_file.write("[{0}] [{1}] {2}\n".format(self.now, level,msg))

    def info(self, msg):
        self._write_log("INFO", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)
