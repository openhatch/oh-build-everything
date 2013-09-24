import contextlib
import os
import os.path


@contextlib.contextmanager
def pushd(path):
    '''A context manager which acts like bash "pushd",
    where you can easily restore the old directory.'''
    current_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_cwd)


def get_file(name):
    path_to_this = os.path.abspath(__file__)
    dir_of_this = os.path.dirname(path_to_this)
    return os.path.join(dir_of_this, name)
