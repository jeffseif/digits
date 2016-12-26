from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

from digits import __author__
from digits import __description__
from digits import __email__
from digits import __program__
from digits import __url__
from digits import __version__


def add_post_build_to_run(cls):

    original_run = cls.run

    def run_with_post_build(self):
        # Run intact method
        original_run(self)

        # Fetch corpus
        import subprocess
        subprocess.run(['./scripts/fetch_corpus.sh'])

        # Train model
        from digits.main import train_model_for_setup_dot_py
        train_model_for_setup_dot_py()

    cls.run = run_with_post_build

    return cls


setup(
    author=__author__,
    author_email=__email__,
    cmdclass={
        'develop':add_post_build_to_run(develop),
        'install':add_post_build_to_run(install),
    },
    description=__description__,
    install_requires=[
        'numpy>=1.11.3',
        'Pillow>=3.4.2',
        'scikit-learn>=0.18.1',
        'scipy>=0.18.1',
    ],
    name=__program__,
    packages=[__program__],
    platforms='all',
    setup_requires=[
        'setuptools',
        'tox',
    ],
    test_suite='tests',
    url=__url__,
    version=__version__,
)
