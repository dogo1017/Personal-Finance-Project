import requirements
required_packages = ['customtkinter', 'numpy', 'pandas']
required_files = []
requirements.check_and_install(required_packages)

import entry

entry.login()

while True:
    print(1234)