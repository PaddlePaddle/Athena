import os
import sys
import platform
from setuptools import setup

python_version = platform.python_version()
version_detail = sys.version_info
version = str(version_detail[0]) + "." + str(version_detail[1])
env_version = os.getenv("PY_VERSION", None)

if version_detail < (3, 8):
    raise RuntimeError(
        f"Athena only supports Python version >= 3.8 now,"
        f"you are using Python {python_version}"
    )
elif env_version is None:
    print(f"export PY_VERSION = { version }")
    os.environ["PY_VERSION"] = python_version

elif env_version != version:
    raise ValueError(
        f"You have set the PY_VERSION environment variable to {env_version}, but "
        f"your current Python version is {version}, "
        f"Please keep them consistent."
    )


setup()
