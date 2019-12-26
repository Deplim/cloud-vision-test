import io
import os
import time

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

path="/Users/wisesolution/Documents/GitHub/cloud-vision-test/tant1.jpg"
cre_path="/Users/wisesolution/Documents/GitHub/cloud-vision-test/loyal-optics-263106-21e5d799dc78.json"

if not os.path.exists(path):
    print("no path file")
if not os.path.exists(cre_path):
    print("no cre_path file")

# Instantiates a client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=cre_path

def detect_text(path):
    start = time.time()
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    print("time check 1 : ", time.time()-start)
    response = client.document_text_detection(image=image)
    print("time check 2 : ", time.time() - start)
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        if "kg" in text.description:
            print(text.description)
        if "Kg" in text.description:
            print(text.description)
    print("time check 2 : ", time.time() - start)

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    start = time.time()
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    print("time check 1 : ", time.time() - start)
    response = client.document_text_detection(image=image)
    print("time check 2 : ", time.time() - start)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    print("time check 2 : ", time.time() - start)

detect_text(path)

