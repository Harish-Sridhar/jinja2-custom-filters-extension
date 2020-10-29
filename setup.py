import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jinja2_custom_filters_extension",
    version="0.0.2",
    author="Harish Sridhar",
    author_email="harish.18.sridhar@gmail.com",
    description="A package containing custom filters for jinja2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harish-Sridhar/jinja2-custom-filters-extension",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)