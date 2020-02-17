from distutils.core import setup


def getRequirements():
    with open("requirements.txt") as requirementsFile:
        requirements = requirementsFile.readlines()

    requirementsWithoutNewlines = map(
        lambda line: line.replace("\\n", ""), requirements
    )
    return requirementsWithoutNewlines


setup(
    name="RobinhoodTrader",
    version="0.1.0",
    author="Jay Bulsara",
    author_email="jaxbulsara@gmail.com",
    packages=["RobinhoodTrader"],
    license="MIT",
    include_package_data=True,
    description="Package to interface with the Robinhood API.",
    classifiers=["Programming Language :: Python :: 3.5",],
    keywords="Robinhood trade buy sell API stocks crypto cryptocurrency",
    install_requires=getRequirements(),
)
