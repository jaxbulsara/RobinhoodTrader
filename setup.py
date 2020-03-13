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
    version="0.1.2",
    author="Jay Bulsara",
    author_email="jaxbulsara@gmail.com",
    packages=[
        "RobinhoodTrader",
        "RobinhoodTrader.common",
        "RobinhoodTrader.common.mixins",
        "RobinhoodTrader.crypto",
        "RobinhoodTrader.crypto.mixins",
        "RobinhoodTrader.endpoints",
        "RobinhoodTrader.session",
        "RobinhoodTrader.session.mixins",
        "RobinhoodTrader.stocks",
        "RobinhoodTrader.stocks.mixins",
    ],
    license="MIT",
    include_package_data=True,
    description="Package to interface with the Robinhood API.",
    classifiers=["Programming Language :: Python :: 3.5",],
    keywords="Robinhood trade buy sell API stocks crypto cryptocurrency",
    install_requires=["requests>=2.22.0"],
)
