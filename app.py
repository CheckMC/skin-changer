from flask import Flask, request, render_template
import SkinGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print_color', methods=['POST'])
def print_color():
    data = request.get_json()
    color = data.get('color')
    contrast = data.get('sliderValue')

    # convert that rgb color (formatted orginally as "rgb(255, 255, 255)") to hex
    color = color[4:-1].split(", ")
    color = [int(i) for i in color]
    color = '#%02x%02x%02x' % tuple(color)
    print(color)

    # generate the skin
    SkinGenerator.generate_skin(color, contrast)

    return 'Color received successfully'

if __name__ == '__main__':
    app.run(debug=True)
