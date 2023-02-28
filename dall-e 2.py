import openai
from PIL import Image
import requests
from io import BytesIO
import random

openai.api_key = "YOURapiKEY"

def resize(image, name):
  # Open the image file
  img = Image.open(image)

  # Convert the image to RGBA format
  img = img.convert('RGBA')

  img = img.resize((1024, 1024))

  img.save(name)

resize("sunflowers.png", "input.png")
resize("mask.png", "input-mask.png")

response = openai.Image.create_edit(
  image=open("input.png", "rb"),
  mask=open("input-mask.png", "rb"),
  prompt="A cute tortoiseshell cat sniffing the sunflowers",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
count = random.randint(0, 1111)
img.save(f"cat-sniffing-sunflowers{count}.png")
