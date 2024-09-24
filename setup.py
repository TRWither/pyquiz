from setuptools import setup, find_packages

setup(
    name="quiz",
    version="0.1.0",
    author="TheWither",
    description="A Python library to facilitate the quiz creation.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TRWither/pyquiz",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
