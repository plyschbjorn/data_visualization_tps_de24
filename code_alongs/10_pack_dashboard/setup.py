from setuptools import setup, find_packages

print(find_packages())

setup(
    name="plysch_yh-dashboard",
    version="0.0.1",
    description="""
    This package is used for creating a dashboard in taipy
    """,
    author="Plysch",
    author_email="plysch@my_mail.com",
    install_requires=["pandas", "taipy", "duckdb"],
    packages=find_packages(exclude=("test*", "explorations", "assets")),
)