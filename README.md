# Intelligent EYE
<p align="center">
  <img src="https://github.com/shetumohanto/mistral/assets/53278488/5343483e-5212-44bf-bb2a-2cc25a98d424">
</p>

### Introduction

### Intelligent EYE Architecture
<p align="center">
  <img src="https://github.com/shetumohanto/mistral/assets/53278488/ba3c39fe-042b-44a9-8726-d1d7c154f029">
</p>

### 🔗 System requirements
* Requires a `CUDA compatible GPU` with minimum `8gb VRAM`
* `Python 3.8` or higher

### :rocket: Quick Start
* Add your `GPT-4 Vision API` using a `global environment variable` defined as `OPEN_AI_API`
* Steps for Ubuntu
```bash
sudo nano /etc/environment
OPEN_AI_API="<Paste_Your_GPT4_Vision_API_Here>"
# Exit by pressing Ctrl+X and typing Y when prompted to save the changes
sudo nano ~/.bashrc
export OPEN_AI_API="<Paste_Your_GPT4_Vision_API_Here>"
# Exit bashrc by pressing Ctrl+X and typing Y when prompted to save the changes
```

* Install required dependencies
```bash
pip install -r requirements.txt
```
* Run Intelligent EYE
```bash
streamlit run app.py
```

### Add API key addition instruction and link to the tutorial
### Install dependencies from requirements.txt
### Show how to launch using streamlit command
### Show some example
### Add some sample image
