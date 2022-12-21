from pathlib import  Path

# Absolute path
# C:\Programs Files\Microsoft
# /usr/local/bin
# Relative path
#
#

path = Path()
for file in path.glob('*.py'):
    print(file)


