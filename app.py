from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Store history (simple in-memory list)
translation_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    input_text = ""

    if request.method == 'POST':
        input_text = request.form.get('english_text')

        if input_text:
            translated_text = GoogleTranslator(source='en', target='kn').translate(input_text)

            # Save to history (latest first)
            translation_history.insert(0, {
                'english': input_text,
                'kannada': translated_text
            })

    return render_template(
        'index.html',
        translated_text=translated_text,
        input_text=input_text,
        history=translation_history[:5]  # show last 5
    )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)


