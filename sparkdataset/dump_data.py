# dump_data.py
# initialize SPARKDATASET_HOME, and
# dump sparkdataset/resources.tar.gz into $HOME/.sparkdataset/

import tarfile
from os import mkdir as os_mkdir
from os import path as os_path
from os.path import join as path_join


def __setup_db():
    homedir = os_path.expanduser('~')
    SPARKDATASET_HOME = path_join(homedir, '.sparkdataset/')

    if not os_path.exists(SPARKDATASET_HOME):
        # create $HOME/.sparkdataset/
        os_mkdir(SPARKDATASET_HOME)
        print('initiated datasets repo at: {}'.format(SPARKDATASET_HOME))

        # copy the resources.tar.gz from the module files.

        # # There should be a better way ? read from a URL ?
        import sparkdataset
        filename = path_join(sparkdataset.__path__[0], 'resources.tar.gz')
        tar = tarfile.open(filename, mode='r|gz')

        # # reading 'resources.tar.gz' from a URL
        # try:
        #     from urllib.request import urlopen # py3
        # except ImportError:
        #     from urllib import urlopen # py2
        # import tarfile
        #
        # targz_url = 'https://example.com/resources.tar.gz'
        # httpstrem = urlopen(targz_url)
        # tar = tarfile.open(fileobj=httpstrem, mode="r|gz")

        # extract 'resources.tar.gz' into SPARKDATASET_HOME
        # print('extracting resources.tar.gz ... from {}'.format(targz_url))
        tar.extractall(path=SPARKDATASET_HOME)
        # print('done.')
        tar.close()
