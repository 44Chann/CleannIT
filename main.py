import os
import shutil
import sys
from join_dir import join_dir_path

# All the dirs where files will move from Downloads  to these Dirs
BASE_DIR = os.environ['HOME']
DOWNLOADS = join_dir_path(BASE_DIR, 'Downloads')
PICTURES = join_dir_path(BASE_DIR, 'Pictures')
MUSIC = join_dir_path(BASE_DIR, 'Music')
DOCUMENTS = join_dir_path(BASE_DIR, 'Public')
CODE = join_dir_path(BASE_DIR, 'snippites')
VIDEO = join_dir_path(BASE_DIR, 'Video')


# list for file types  that can be moved to a folder
# jpeg, png, svg can be moved to pictures
picture_file_types = ['.jpg', '.jpeg', '.png', '.svg']
music_file_types = ['.mp3', ]
video_file_types = ['.mp4', '.mov', '.wmv', '.webm']
document_file_types = ['.docx', '.pdf', '.odds', '.pptx', '.txt', ]
code_file_types = [
    '.js',
    '.py',
]

# list of all dirs to itrate and find anyof these exists or not
DIRS = [DOCUMENTS, PICTURES, MUSIC, CODE, VIDEO]


def check_path():
    """
    Check If a path or dir exists or not
    :return:
    """
    for dir in DIRS:
        # if folder is on Home DO NOthing
        if os.path.exists(dir):
            pass
        else:
            # create dir
            try:
                os.makedirs(dir)
            except:
                pass


def move():
    for dir in os.listdir(DOWNLOADS):

        file_name, ex = os.path.splitext(dir)
        src = os.path.join(DOWNLOADS, dir)

        if ex in picture_file_types:

            dest = os.path.join(PICTURES, dir)
            print(f'{dir} is moved to {dest}')
            shutil.move(src=src, dst=dest)

        elif ex in code_file_types:

            dest = os.path.join(CODE, dir)
            print(f'{dir} is moved to {dest}')
            shutil.move(src=src, dst=dest)

        elif ex in document_file_types:

            dest = os.path.join(DOCUMENTS, dir)
            print(f'{dir} is moved to {dest}')
            shutil.move(src=src, dst=dest)

        elif ex in video_file_types:

            dest = os.path.join(VIDEO, dir)
            print(f'{dir} is moved to {dest}')
            shutil.move(src=src, dst=dest)

        elif ex in music_file_types:

            dest = os.path.join(MUSIC, dir)
            print(f'{dir} is moved to {dest}')
            shutil.move(src=src, dst=dest)


def main():

    check_path()
    move()

    print('Clean Done')
