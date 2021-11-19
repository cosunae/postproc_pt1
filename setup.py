import setuptools

setuptools.setup(
    name="postproc_pt1",
    version='0.0.1',
    description="prototype for metadata and field units consistency",
    author="lonely guy",
    author_email="lonely.guy@universe.com",
    license="MIT",
    url="https://github.com/ecmwf/cfgrib",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["cfgrib", "pint"],
    python_requires=">=3.7",
    extras_require={
        "xarray": ["xarray>=0.15"],
        "tests": ['unittest'],
    },
    zip_safe=True,
)
