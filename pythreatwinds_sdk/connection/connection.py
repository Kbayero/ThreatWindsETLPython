class ConnectionMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Connection(metaclass=ConnectionMeta):
    """
    Template for make a connection object
    """

    def __init__(self):
        self.endpoint = None

    def add_connection(self,url):
        self.endpoint = url