import os
import shutil

# Example: move generated .github folder to another location if needed
source_dir = '.github'
target_dir = '../.github'  # Adjust path as necessary

print(os.path.abspath(source_dir))

if os.path.exists(source_dir) and not os.path.exists(target_dir):
    shutil.move(source_dir, target_dir)
    shutil.rmtree(os.path.abspath("./"))
    print(f"Moved {source_dir} to {target_dir}")
else:
    print("No action needed.")
