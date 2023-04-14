import os

# Create project directory
project_name = "1D-Two-Stream-Instability-Simulation"
if not os.path.exists(project_name):
    os.makedirs(project_name)

# Create subdirectories
dirs = ["data", "notebooks", "scripts"]
for d in dirs:
    dir_path = os.path.join(project_name, d)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Create README file
description = "1D-Two-Stream-Instability-Simulation is a simulation of the 1D-Two-Stream-Instability problem."
readme = f"# {project_name}\n\n{description}"
with open(os.path.join(project_name, "README.md"), "w") as f:
    f.write(readme)

# Create requirements file
requirements = ["numpy", "matplotlib", "scipy"]
with open(os.path.join(project_name, "requirements.txt"), "w") as f:
    f.write("\n".join(requirements))

# Create license file
license_text = "MIT License"
with open(os.path.join(project_name, "LICENSE"), "w") as f:
    f.write(license_text)

# Create gitignore file
gitignore_text = "data/\n*.pyc\n__pycache__/\n"
with open(os.path.join(project_name, ".gitignore"), "w") as f:
    f.write(gitignore_text)

# Create main script file
main_script = """import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

# Your code here

if __name__ == '__main__':
    main()
"""
with open(os.path.join(project_name, "scripts", "main.py"), "w") as f:
    f.write(main_script)
