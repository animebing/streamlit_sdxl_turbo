import streamlit as st
from st_keyup import st_keyup

from utils_bridge import task_queue


title = "SDXL Turbo"
st.set_page_config(page_title=title)
st.title(title)

text = st_keyup("text on the fly", debounce=200, key="text")
if text:
    task_id, task_event = task_queue.put(text)
    task_event.wait()
    image = task_queue.get(task_id)
    st.image(image)
