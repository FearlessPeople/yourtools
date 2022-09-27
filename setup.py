import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yourtools",
    version="0.0.2",
    author="zfang",
    author_email="founder517518@163.com",
    description="Python helper tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/yourtools/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
