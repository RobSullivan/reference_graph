from setuptools import setup, find_packages

setup(
    name='reference_graph',
    version='0.1.0',
    description='Article references as a graph',
    long_description="<add a longer description>",
    author='Written by Robert Sullivan',
    author_email='robertjsullivan@gmail.com',
    url='https://github.com/RobSullivan/reference_graph',
    license='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)
