import requirements
required_packages = ["customtkinter", "matplotlib", "numpy", "pandas"]
requirements.check_and_install(required_packages)

import entry
entry.launch()