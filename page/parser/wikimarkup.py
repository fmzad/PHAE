import re

class Parser:
    eol_re = re.compile(r'\r?\n', re.UNICODE)
    result = ''
    def __init__(self, raw):
        self.raw = raw # class attribute <raw>
    def parse(self):
        print(self.raw)
        self.lines = self.eol_re.split(self.raw)
        for i, line in enumerate(self.lines):
            self.result += line
            if i != len(self.lines)-1:
            	self.result += "<br>"
        return self.result