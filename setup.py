from setuptools import setup, find_packages

setup(
    name="contact_manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Leonardo Yves",
    author_email="leoyves@matematica.ufrj.br",
    description="A simple contact manager",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lyvesmatufrj/contact_manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
