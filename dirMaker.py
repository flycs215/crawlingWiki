import sys
import os

class dirMaker:

    dir_path = ''
    def dirMake(self):
        dir_path = sys.argv[1]
        dir_pathTotal = './' + dir_path
        if os.path.isdir(dir_pathTotal):
            print('already exist!')
        else:
            os.makedirs(dir_pathTotal)
        return dir_pathTotal