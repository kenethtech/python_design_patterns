import logger
from logger_class import Logger

def main():
    logger_object = Logger("var/log/class_log.log")
    logger_object.info("This is the logger class!!")
    logger_object.error("This is the error object")


if __name__ == "__main__":
    main()
