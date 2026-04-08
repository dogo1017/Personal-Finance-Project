import sys
import subprocess
import importlib.util

def check_and_install(packages):
    missing_packages = []
    
    for package in packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)
            
    if not missing_packages:
        return

    print(f"Missing libraries: {', '.join(missing_packages)}")
    
    choice = input(f"Do you want to install {', '.join(missing_packages)}? (y/n): ").lower()
    if choice == 'y':
        for package in missing_packages:
            print(f"Installing {package}...")

            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("Installation complete. Please rerun the script.")
        sys.exit()
    else:
        print("Installation skipped. The script will stop.")
        sys.exit()

