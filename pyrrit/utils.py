import config

__author__ = 'arnav'


#Console colsor constants
class Col:
    ylw = '\033[93m'
    pnk = '\033[95m'
    grn = '\033[92m'
    rst = '\033[0m'


def change_path_to_project_url(path):
    path = path.replace('/', '_')
    path = config.g_proj_basedir + path
    return path


def change_projname_to_dirpath(projname):
    # remove the project's base dir (for eg. the "AOKP/" part
    dirpath = projname.replace(projname[:len(config.g_proj_basedir)], '')
    dirpath = dirpath.replace('_', '/')
    return dirpath
