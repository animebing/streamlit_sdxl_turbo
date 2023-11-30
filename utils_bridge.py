from utils_queue import TaskQueue
from utils_sdxl_turbo import generate_image


task_queue = TaskQueue(generate_image)
task_queue.start()
