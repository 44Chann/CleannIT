from setuptools import setup

setup(
    name='cleanit',
    version='1.0',
    description='A Cli To Clean Your Downloads Folder and Keep Things Organize ',
    author='Vikash Manda',
    author_email='yes_vikash@yahoo.com',
    py_modules=['main', 'join_dir'],
    # install_requires=[
    #     'shutil'
    # ],
    entry_points='''
        [console_scripts]
        cleanit=main:main
    '''
)
