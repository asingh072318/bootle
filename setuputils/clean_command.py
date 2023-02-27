import os
import shutil
import logging
from distutils.command.clean import clean


try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None):
        return text

class CleanCommand(clean):
    def run(self):
        super().run()
        directories = ['build', 'dist', 'bootle.egg-info']
        files = ['bootle.log']
        
        for rmfile in files:
            if os.path.exists(rmfile):
                try:
                    os.remove(rmfile)
                    logging.info(colored(f"Successfully deleted file {rmfile}.", "green"))
                except OSError as e:
                    logging.error(colored(f"Error: {e.filename} - {e.strerror}.", "red"))

        for directory in directories:
            if os.path.exists(directory):
                try:
                    shutil.rmtree(directory)
                    logging.info(colored(f"Successfully deleted directory {directory}.", "green"))
                except OSError as e:
                    logging.error(colored(f"Error: {e.filename} - {e.strerror}.", "red"))