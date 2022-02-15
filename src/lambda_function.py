import base64
import io
import json
import pdf2image

def lambda_handler(event, context):
    event = json.loads(event['body'])
    base64pdf = event['base64pdf'].replace('data:application/pdf;base64,', '')
    images = pdf2image.convert_from_bytes(
        base64.b64decode(base64pdf),
        poppler_path='poppler_binaries/')
    imagesArr = []
    for img in images:
        buffered = io.BytesIO()
        img.save(buffered, format='jpeg')
        imagesArr.append('data:image/jpeg;base64,' + base64.b64encode(buffered.getvalue()).decode('ascii'))
    return {'images': imagesArr}

