#!/bin/bash
set -e

echo "Setting up TKH Data Science Environment..."

# Install Python packages
echo "Installing Python packages..."
pip install -r requirements.txt

# Install tkh_utils package
echo "Installing tkh_utils..."
pip install -e utils/

# Register Jupyter kernel
echo "Registering Jupyter kernel..."
python -m ipykernel install --user \
    --name tkh \
    --display-name "TKH Data Science"

# Enable ipywidgets
echo "Enabling ipywidgets..."
jupyter nbextension enable \
    --py widgetsnbextension --sys-prefix

# Enable plotly
echo "Enabling plotly..."
jupyter nbextension enable \
    --py --sys-prefix plotly

echo ""
echo "✓ TKH Data Science Environment ready!"
echo "  Kernel: TKH Data Science"
echo "  Python: $(python --version)"
echo ""
echo "To launch Jupyter:"
echo "  jupyter notebook"
