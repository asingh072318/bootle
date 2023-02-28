import os
import urllib.request
import tarfile
import logging
from setuptools.command.install import install


class UpgradeCommand(install):
    """Custom command to upgrade Bootle from GitHub"""

    def run(self):
        # Get the latest release version from GitHub
        url = 'https://api.github.com/repos/asingh072318/bootle/releases/latest'
        try:
            response = urllib.request.urlopen(url)
            if response.getcode() == 200:
                release = eval(response.read())
                tag_name = release['tag_name']
                assets = release['assets']
                # Get the URL for the source code tarball
                tarball_url = next(asset['browser_download_url'] for asset in assets if asset['name'].endswith('.tar.gz'))
                # Download the source code tarball
                filename = os.path.basename(tarball_url)
                urllib.request.urlretrieve(tarball_url, filename=filename)
                # Install the source code from the tarball using pip
                tar = tarfile.open(filename, 'r:gz')
                tar.extractall()
                tar.close()
                os.system(f'pip install {os.path.splitext(filename)[0]}')
            else:
                logging.error(f'Could not fetch latest version from {url}')
        except Exception as e:
            logging.error(f'Error while upgrading Bootle: {str(e)}')