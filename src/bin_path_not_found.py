class BinPathNotFound(Exception):
    interpreter_name: str

    def __init__(self, *args: object, interpreter_name: str):
        super().__init__(*args)
        self.interpreter_name = interpreter_name