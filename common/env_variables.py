import os
import shutil
print(os.environ['password'])
print(os.path.exists('../helpers'))
print(os.path.basename('../common'))
print(os.path.abspath(__file__))
print(os.getcwd())
absolute = os.getcwd()


def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), destination)


make_archive('./common',
             './common.zip')
"""
print(os.environ)

for k, v in os.environ.items():
    print(f'{k}={v}')
user_Name = os.environ['USERNAME']
password = os.environ['password']
print(f'{user_Name} is environment user name '+f"{password} is environment password")
user_Key = input("Please enter the environment key: ")
print(os.environ[user_Key])
env_var = input("Please enter the environment variable name :")
print(os.environ.get(env_var, 'csv'))
"""
"""
env_var = input('Please enter the environment variable name:\n')

if env_var in os.environ:
    print(f'{env_var} value is {os.environ[env_var]}')
else:
    print(f'{env_var} does not exist')
"""

#env_var = input('Please enter environment variable name:\n')

#env_var_value = input('Please enter environment variable value:\n')

#os.environ[env_var] = env_var_value

#print(f'{env_var}={os.environ[env_var]} environment variable has been set.')

