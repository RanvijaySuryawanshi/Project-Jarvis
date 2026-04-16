from setuptools import setup, find_packages

setup(
    name="voice-assistant-app",
    version="0.1",
    author="Ranvijay",
    author_email="ranvijaysuryawanshi@gmail.com",
    description="A voice assistant application that recognizes speech and executes commands.",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "speech_recognition",
        "pyttsx3",
        "webbrowser",
    ],
    entry_points={
        'console_scripts': [
            'voice-assistant=main:main',
        ],
    },
)