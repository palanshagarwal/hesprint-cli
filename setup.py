from setuptools import setup, find_packages


CLASSIFIERS = [
]


entry_points = {
        'console_scripts': [
            'sprint=sprint.main:main'
     ]
}


install_requires = [
        'argparse==1.2.1',
        'requests==2.10.0',
        'wsgiref==0.1.2'
]

tests_require = [
]


setup(
    name="sprint",
    version='1.0.1',
    description="Python client for HackerEarth sprint",
    url='https://www.hackerearth.com',
    author='Palansh Agarwal',
    author_email='palansh@hackerearth.com',
    license='MIT',
    packages=find_packages(),
    keywords=['hackerearth', 'sprint'],
    classifiers=CLASSIFIERS,
    zip_safe=True,
    include_package_data=True,
    entry_points=entry_points,
    install_requires=install_requires,
)
