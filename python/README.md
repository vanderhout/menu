How to install (if not copying files manually):

1. Clone the repo:
git clone https://github.com/vanderhout/menu

2. Build:
cd menu\python\
"C:\python\python_3_13_3\python.exe" setup.py sdist bdist_wheel -d "C:\python\wheels"

3. Install:
"C:\python\python_3_13_3\Scripts\pip.exe" install  --force-reinstall C:\python\wheels\menu-0.0.1-py3-none-any.whl

4. Import:
from menu import Menu