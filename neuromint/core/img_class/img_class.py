# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("zero-shot-image-classification", model="openai/clip-vit-large-patch14")

result = pipe("imgs/test_neuro_img.png", candidate_labels=["label1", "label2", "label3"])
print(result)