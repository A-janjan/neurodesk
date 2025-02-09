from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


# Load pre-trained BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


# Load your screenshot (make sure to replace 'your_image.png' with the actual file path)
image = Image.open("../assets/pic1.png").convert("RGB")

# Preprocess the image and prepare the inputs for the model
inputs = processor(images=image, return_tensors="pt")

# Generate caption for the image
out = model.generate(**inputs)

# Decode the generated caption
caption = processor.decode(out[0], skip_special_tokens=True)

# Print the caption
print("Generated Caption:", caption)
