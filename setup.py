from setuptools import setup, find_packages
from setuputils.clean_command import CleanCommand
from setuputils.upgrade_command import UpgradeCommand
from setuputils.logging_config import LOGGING_CONFIG
import logging.config


class BootleSetup:
    def __init__(self):
        self.name = 'bootle'
        self.version = '0.1'
        self.packages = find_packages(include=['bootle', 'bootle.*'])
        self.include_package_data = True
        self.install_requires = ['click','termcolor','psutil']
        self.entry_points = {
            'console_scripts': [
                'bootle = bootle.bootle:main',
            ],
        }
        self.cmdclass = {
            'clean': CleanCommand,
            'upgrade': UpgradeCommand
        }

    def setup(self):
        logging.config.dictConfig(LOGGING_CONFIG)

        setup(
            name=self.name,
            version=self.version,
            packages=self.packages,
            include_package_data=self.include_package_data,
            install_requires=self.install_requires,
            entry_points=self.entry_points,
            cmdclass=self.cmdclass,
        )


if __name__ == '__main__':
    bootle_setup = BootleSetup()
    bootle_setup.setup()
