import json
import logging
import os
import traceback


class Logger:

    def __init__(self, module=__name__, level=logging.INFO):
        if os.getenv("ENVIRONMENT") == "local":
            self.level = logging.DEBUG
        else:
            self.level = level

        self.module = module
        self.logger = logging.getLogger(module)
        self.logger.setLevel(self.level)

        ch = logging.StreamHandler()
        ch.setLevel(self.level)
        ch.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s:%(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S %Z",
            )
        )

        self.logger.addHandler(ch)

    def debug(self, message, additional_info=None):
        msg = self.__format_message(message, additional_info)
        self.logger.debug(msg)

    def info(self, message, additional_info=None):
        msg = self.__format_message(message, additional_info)
        self.logger.info(msg)

    def warning(self, message, additional_info=None):
        msg = self.__format_message(message, additional_info)
        self.logger.warning(msg)

    def error(self, message, additional_info=None):
        msg = self.__format_message(message, additional_info, add_traceback=True)
        self.logger.error(msg)

    def critical(self, message, additional_info=None):
        msg = self.__format_message(message, additional_info, add_traceback=True)
        self.logger.critical(msg)

    def __format_message(self, msg, additional_info, add_traceback=False):
        formatted_message = msg
        if add_traceback:
            formatted_message = (
                f"{formatted_message} - ## TRACEBACK ## - {traceback.format_exc()}"
            )
        if additional_info is not None:
            formatted_message = f"{formatted_message} - ## ADDITIONAL INFO ## - {json.dumps(additional_info)}"

        return formatted_message
