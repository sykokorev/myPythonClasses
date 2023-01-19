class SingletonObject(object):

    class __SingletonObject():
        
        def __init__(self):
            self.val = None

        def __str__(self):
            return f"{self!r} {self.val}"

        def _write_log(self, level, msg):

            with open(self.filename, "a") as log_file:
                log_file.write(f"[{level}] {msg}\n")
        
        def critical(self, msg):
            self._write_log("CRITICAL", msg)
        
        def error(self, msg):
            self._write_log("ERROR", msg)

        def warn(self, msg):
            self._write_log("WARN", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)
    
    instance = None
    
    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()

        return SingletonObject.instance

    def __getatt__(self, name: str):
        return getattr(self.instance, name)


    def __setattr__(self, name: str) -> None:
        return setattr(self.instance, name)


class SingletonLogger(object):
    __instance = None
    def __new__(cls, filename):
        if SingletonLogger.__instance is None:
            SingletonLogger.__instance = object.__new__(cls)
        SingletonLogger.__instance = filename
        return SingletonLogger.__instance

    def __str__(self): return f'Class {self!r}\t{self.__instance}'

    def __getatt__(self, name: str):
        return getattr(self.__instance, name)

    def __setattr__(self, name: str):
        return setattr(self.__instance, name)

    def _write_log(self, level, msg):

        with open(self.filename, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")
    
    def critical(self, msg):
        self._write_log("CRITICAL", msg)
    
    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)    


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class BorgLogger(Borg):
    def __init__(self, *args):
        Borg.__init__(self)
        self.filename = args[0]

    def __str__(self): return f'{self!r}\t{self.filename}'

    def _write_log(self, level, msg):

        with open(self.filename, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")
    
    def critical(self, msg):
        self._write_log("CRITICAL", msg)
    
    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)
