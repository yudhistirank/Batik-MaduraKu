class ModelLoadError(Exception):
    def __init__(self, message="Failed to load model", status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
