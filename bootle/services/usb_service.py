import os
import logging
import platform
import psutil
from bootle.models.device import Device


logger = logging.getLogger(__name__)


class UsbService:
    # def get_devices(self):
    #     devices = []
    #     if platform.system() == 'Windows':
    #         for drive in range(1, 27):
    #             device_path = f'{chr(drive + 64)}:/'
    #             if os.path.exists(device_path):
    #                 total, used, available = self.get_device_space(device_path)
    #                 device_size = {'total': total, 'used': used, 'available': available}
    #                 devices.append(Device(device_path, device_size, device_path))
    #     else:
    #         media_path = '/media' if platform.system() == 'Linux' else '/Volumes'
    #         for device in os.listdir(media_path):
    #             device_path = os.path.join(media_path, device)
    #             if os.path.isdir(device_path):
    #                 total, used, available = self.get_device_space(device_path)
    #                 device_size = {'total': self.get_human_readable_size(total), 'used': self.get_human_readable_size(used), 'available': self.get_human_readable_size(available)}
    #                 devices.append(Device(device_path, device_size, device))
    #     return devices

    def get_devices(self):
        devices = []
        for partition in psutil.disk_partitions():
            if 'sd' in partition.device:
                device_path = partition.mountpoint
                total, used, available = self.get_device_space(device_path)
                device_size = {
                    'total': self.get_human_readable_size(total),
                    'used': self.get_human_readable_size(used),
                    'available': self.get_human_readable_size(available)
                }
                devices.append(Device(device_path, device_size, device_path))
        return devices

    def get_device_space(self, path):
        st = os.statvfs(path)
        total = st.f_blocks * st.f_frsize
        available = st.f_bavail * st.f_frsize
        used = total - available
        return total, used, available

    @staticmethod
    def get_human_readable_size(size_in_bytes):
        """
        Convert size from bytes to human-readable format.
        """
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.2f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.2f} PB"