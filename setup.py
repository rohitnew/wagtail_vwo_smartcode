from setuptools import setup, find_packages

setup(
    name="wagtail_vwo_smartcode",
    version="0.2",
    description="Injects VWO SmartCode (sync or async) into Wagtail pages for A/B testing",
    author="VWO",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wagtail>=4.0",
        "Django>=3.2"
    ],
    classifiers=[
        "Framework :: Django",
        "Framework :: Wagtail",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)

