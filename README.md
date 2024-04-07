# Intelligent EYE
<p align="center">
  <img src="https://github.com/shetumohanto/mistral/assets/53278488/5343483e-5212-44bf-bb2a-2cc25a98d424">
</p>

### Introduction

The Intelligent EYE enables users to query images using text input. Users can select specific objects for their queries, streamlining the process of asking questions and eliminating the need to describe the position of objects within the image using words.

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
### 🔗 Related Works

Intelligent EYE uses the following technologies at its core architecture:
- [Segment Anything](https://github.com/facebookresearch/segment-anything): Segment anything
- [SoM](https://github.com/microsoft/SoM): Set-of-Mark Visual Prompting for GPT-4V

### Show some example
### Add some sample image
