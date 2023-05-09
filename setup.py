from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='this program sorts files by extension',
    url='https://github.com/OleksandrButkov/depositories_os.walk/blob/master/main.py',
    author='OleksandrButkov13',
    author_email='butkov00@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':
                ['clean-folder=clean_folder.clean:main']}

)
