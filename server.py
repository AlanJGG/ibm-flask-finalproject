"""
This module defines a Flask application for emotion detection.
It provides a homepage and an endpoint for analyzing emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the homepage of the application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze emotions in the provided text via a GET request.

    The text is sent as a query parameter named 'textToAnalyze'.
    If the text is invalid, returns an error message. Otherwise,
    it returns a formatted string with detected emotions and the dominant emotion.

    Returns:
        str: A response summarizing detected emotions or an error message.
    """
    input_text = request.args.get('textToAnalyze', '')

    emotion_result = emotion_detector(input_text)

    if emotion_result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    response_text = (
        f"For the given statement, the system response is: "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']}, "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )
    return response_text

if __name__ == '__main__':
    app.run(debug=True, port=5000)
