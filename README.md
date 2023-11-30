# Streamlit SDXL Turbo Demo 

https://github.com/animebing/streamlit_sdxl_turbo/assets/19849456/c8c8572b-9353-4878-962d-e62f1a8d3630

## Getting Started

### Installing

```
pip install -r requirements.txt
```

### Executing program

```
sh scripts/run.sh
```

### Usage

1. change `model_name` in `utils_sdxl_turbo.py` if the model is in a local directory
2. change `debounce` in `app` to determine how often the text is processed
3. change GPU card index and server port in `scripts/run.sh`


## Acknowledgments

* [streamlit-keyup](https://github.com/blackary/streamlit-keyup)
* [sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo)
