from flask import Flask, request
import boto3

app = Flask(__name__)

# S3 configuration
S3_BUCKET_NAME = "mys3bucket"   # your bucket name
s3 = boto3.client('s3', region_name='ap-south-1')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        if file:
            try:
                s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)
                return "File uploaded successfully!"

            except Exception as e:
                return f"Error uploading file: {str(e)}"

    return '''
    <!doctype html>
    <html>
    <head>
        <title>Upload File</title>
    </head>
    <body>
        <h1>Upload a File to AWS S3</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
