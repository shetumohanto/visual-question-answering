# Intelligent EYE

<p align="center">
  <img width="300px" src="https://github.com/shetumohanto/mistral/assets/53278488/5343483e-5212-44bf-bb2a-2cc25a98d424">
</p>

### Introduction

The Intelligent EYE enables users to query images using text input. Users can select specific objects for their queries, streamlining the process of asking questions and eliminating the need to describe the position of objects within the image using words.

### Intelligent EYE Architecture
<p align="center">
  <img src="https://github.com/shetumohanto/mistral/assets/53278488/ba3c39fe-042b-44a9-8726-d1d7c154f029">
</p>

### 🔗 System requirements
* Requires a `CUDA compatible GPU` with minimum `8gb VRAM`
* `Python>=3.8`

### :rocket: Quick Start
* Add your `GPT-4 Vision API Key` using an `environment variable` defined as `OPENAI_API_KEY`
```bash
sudo nano ~/.bashrc
# Insert the line at the last of the file
export OPENAI_API_KEY="<Paste_Your_GPT4_Vision_API_Key_Here>"
# Exit bashrc by pressing Ctrl+X and typing Y when prompted to save the changes, press Enter to complete
source ~/.bashrc
```

* Clone the repository
```bash
git clone https://github.com/shetumohanto/mistral.git
cd mistral
```

* Download checkpoint for the `segment anything` `vit_h` model. 
```bash
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
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

### Sample output
![example](https://github.com/shetumohanto/mistral/assets/53278488/c652ec68-4514-4be3-8b6c-17db04d37fc7)
