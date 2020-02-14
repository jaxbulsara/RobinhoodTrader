import logging
from logging import Logger, StreamHandler, Formatter


class LogFactory:
    def __init__(self, isVerbose=False):
        self.isVerbose = isVerbose
        self.streamFormat = (
            "%(levelname)s in %(module)s:%(lineno)d - %(message)s"
        )
        self.streamFormatter = None
        self.streamHandler = None
        self.log = None

    def getLogger(self):
        self._createStreamFormatter()
        if self.isVerbose:
            self._createVerboseStreamHandler()
        else:
            self._createNonVerboseStreamHandler()
        self._createLogger()
        return self.logger

    def _createStreamFormatter(self):
        self.streamFormatter = Formatter(fmt=self.streamFormat)

    def _createVerboseStreamHandler(self):
        self.streamHandler = StreamHandler()
        self.streamHandler.setFormatter(self.streamFormatter)
        self.streamHandler.setLevel(logging.DEBUG)

    def _createNonVerboseStreamHandler(self):
        self.streamHandler = StreamHandler()
        self.streamHandler.setFormatter(self.streamFormatter)
        self.streamHandler.setLevel(logging.INFO)

    def _createLogger(self):
        self.logger = Logger(name="robinhood")
        self.logger.addHandler(self.streamHandler)
        self.logger.setLevel(logging.DEBUG)
