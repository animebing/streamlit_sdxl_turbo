from diffusers import AutoPipelineForText2Image
import torch


def generate_image(text):
    generator = torch.Generator()
    generator.manual_seed(seed)
    image = pipe(prompt=text, num_inference_steps=1, guidance_scale=0.0, generator=generator).images[0]
    return image


seed = 0

model_name = 'stabilityai/sdxl-turbo' # or local path
pipe = AutoPipelineForText2Image.from_pretrained(model_name, torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")
pipe(prompt='a cat', num_inference_steps=1, guidance_scale=0.0) # warmup
