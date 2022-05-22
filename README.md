# OlxAutoSearch

### Run 
```bash
# Install google-chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Clone repo
git clone https://git.kobiela.click/wiktor.kobiela/OlxAutoSearch.git
cd OlxAutoSearch

# Create and activate venv
mkdir venv
python3 -m venv venv/
source venv/bin/activate

# Install requirements
python3 -m pip install -r requirements.txt

# Run the script
python3 olx.py -h
```