import os
import shutil

from common import util


def coding_test(compress_function, decompress_function):
    filename = 'test/files/bookkeeper'
    backup_filename = filename + '.backup'
    output_filename = util.get_output_filename(filename)
    shutil.copyfile(filename, backup_filename)

    try:
        compress_function(filename)
        decompress_function(output_filename)

        with open(filename) as source:
            with open(backup_filename) as backup:
                equal = source.read() == backup.read()

        os.remove(output_filename)
    except RuntimeError:
        equal = False

    os.remove(filename)
    os.rename(backup_filename, filename)
    return equal
