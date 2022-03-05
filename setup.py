import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaptcha",
    version="1.0.0",
    author="AntonVanke",
    description="一个图形验证码生成工具",
    author_email="antonvanke@hotmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonvanke/kaptcha",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pillow"],
    keywords="captcha",
    include_package_data=True,
    python_requires=">3.7"
)
