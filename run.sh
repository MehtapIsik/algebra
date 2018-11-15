# Create environment
# conda create -n algebra python=3.6

# Activate environment
source activate algebra # For some reason this doesn't work

# Install your package
ipip install -e .

# Install other packages
pip install numpy
pip install yapf
