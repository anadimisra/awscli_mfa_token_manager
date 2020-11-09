import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="awscli_mfa_token_manager",
    version="1.0.0",
    author="Anadi Misra",
    author_email="anadi.msr@gmail.com",
    description="Module to generate credentials from MFA device for AWS CLI ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anadimisra/awscli_mfa_token_manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.8',
    scripts=['bin/manage_credentials'],
    install_requires=[
        'boto3==1.16.12',
    ]
)
