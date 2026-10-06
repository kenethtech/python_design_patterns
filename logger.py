from datetime import datetime, UTC

def now():
    return datetime.now(UTC)

PATH = "var/log/app.log"

def write_log(filename, date, level, msg):
    with open(filename, "a") as log_file:
        log_file.write("{0}: [{1}] {2}\n".format(date, level, msg))

def error(msg):
    write_log(PATH, now(), "ERROR", msg)

def info(msg):
    write_log(PATH, now(), "INFO", msg)

def critical(msg):
    write_log(PATH, now(), "CRITICAL", msg)


def warn(msg):
    write_log(PATH, now(), "WARN", msg)

def debug(msg):
    write_log(PATH, now(), "DEBUG", msg)