from flask import Flask, request, jsonify
from PIL import Image
import os
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/convert', methods=['POST'])
def convert_png_to_pdf():
    try:
        print(request.form)
        if 'file' not in request.files :
            return jsonify({'error': 'Missing file or data'}), 400
        png_file = request.files['file']
        print(png_file.filename)

        png_file = request.files['file']
        # data = json.loads(request.form['data'])
        #
        if png_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        #
        if png_file and png_file.filename.endswith('.png'):
            png_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')
            png_file.save(png_filename)

            pdf_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output.pdf')

            # Open the PNG file using Pillow
            img = Image.open(png_filename)

            # Create a new PDF file
            img.save(pdf_filename, "PDF", resolution=100.0, save_all=True)

            return jsonify({'message': 'Conversion successful', 'pdf_filename': pdf_filename}), 200

        return jsonify({'error': 'Invalid file format'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
