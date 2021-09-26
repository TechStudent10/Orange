import sys

class Error:
    def __init__(self, message, line_number, invoke_error=True):
        self.type = self.__class__.__name__
        self.message = message
        self.line_number = line_number

        self.string = f"{self.type} on line {self.line_number}: {self.message}"
        if invoke_error: self.invoke()
        
    def invoke(self):
        print(self.string)
        sys.exit()

    def __repr__(self):
        return f"<{self.type} line_number={self.line_number} message=\"{self.message}\">"

class SyntaxError(Error):
    def __init__(self, message=None, line_number=None, *args, **kwargs):
        super().__init__(message or "Invalid Syntax", line_number or 1, *args, **kwargs)
