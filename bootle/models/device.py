class Device:
    def __init__(self, device_path, device_size, device):
        self.path = device_path
        self.size = device_size
        self.device = device

    def __str__(self):
        return f"{self.device} ({self.path}) - Total Size: {self.size['total']}, Available Space: {self.size['available']}"