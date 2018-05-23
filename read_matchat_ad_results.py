from admanager.AdManager import *

if __name__ == '__main__':

    this_dir = os.path.dirname(__file__)
    resource_path = os.path.join(this_dir, 'resources')

    admanager = AdManager(resource_path)
    print admanager.listAllAdsets()
