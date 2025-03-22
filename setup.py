from setuptools import setup, find_packages

setup(
    name="farkle",
    version="0.0.0",
    author="Your Name",
    author_email="bdyer5280@gmail.com",
    description="Farkle dice game in python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["requests", "numpy"],  # Add other dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
