import os
import tempfile
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase
cred = credentials.Certificate(os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON'))
firebase_admin.initialize_app(cred, {
    'storageBucket': f'{os.getenv("FIREBASE_PROJECT_ID")}.appspot.com'
})

def upload_image_to_firebase_storage(file):
    if not file:
        raise ValueError('No image file provided')

    # Create a temporary file to save the uploaded image
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[-1]) as temp_file:
        temp_path = temp_file.name
        temp_file.write(file.read())

    try:
        # Upload the file to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(f'blog-images/{file.name}')
        blob.upload_from_filename(temp_path)

        # Make the blob publicly accessible and get the public URL
        blob.make_public()
        image_url = blob.public_url

        return image_url

    finally:
        # Ensure the temp file is deleted after upload
        os.remove(temp_path)
