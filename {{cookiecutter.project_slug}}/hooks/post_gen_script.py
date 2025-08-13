import subprocess
import os

# Inizializza il repository Git
print("Initializing Git repository...")
subprocess.run(['git', 'init'])

# Inizializza DVC
print("Initializing DVC...")
subprocess.run(['dvc', 'init'])

print("\nProject {{ cookiecutter.project_slug }} created successfully!")
print("Next steps:")
print("1. Create and activate the Conda environment using environment.yml.")
print("2. Run 'dvc remote add -d origin {{ cookiecutter.dvc_remote_storage }}' to set up your DVC remote storage.")
print("3. Add your raw data to 'data/raw' and run 'dvc add data/raw' to start versioning.")