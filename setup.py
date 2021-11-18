from setuptools import setup, find_packages
setup(
    name='lotusdb',
    version='0.0.9',
    author='d3tu',
    author_email='jpafly@gmail.com',
    description='pydb',
    packages=find_packages(),
    install_requires=['ujson', 'python-rapidjson'],
    keywords=['database'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)