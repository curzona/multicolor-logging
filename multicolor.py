import logging
import colorama
from colorama import Fore, Back, Style

class MultiFormatter(logging.Formatter):
    def __init__(self, default):
        self.rules = []
        self.addFormatter(default)

    def addFormatter(self, formatter, **kargs):
        if type(formatter) == str:
            formatter = logging.Formatter(formatter)
        self.rules.insert(0, (kargs, formatter))

    def format(self, record):
        if self.rules:
            for pred, formatter in self.rules:
                match = True
                for k, v in pred.items():
                    if getattr(record, k) != v:
                        match = False
                        break

                if match:
                    which = formatter
                    break
        return which.format(record)

class ColorFormatter(MultiFormatter):
    def __init__(self, fmt):
        self.fmt = fmt
        default = fmt.replace("{startcolor}","").replace("{endcolor}","")
        super(ColorFormatter, self).__init__(default)
        colorama.init()

    def addColor(self, color, **kargs):
        fmt = self.fmt.format(startcolor=color, endcolor=colorama.Fore.RESET)
        formatter = logging.Formatter(fmt)
        self.addFormatter(formatter, **kargs)
