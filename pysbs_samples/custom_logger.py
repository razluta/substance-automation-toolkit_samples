class CustomLogger(object):
    """
    Creating a custom logger to easily modify logging mechanism.
    """
    def __init__(self):
        pass

    @staticmethod
    def log(message):
        # Currently using the Python 2 print function for logging, but can be changed to something else
        print message
