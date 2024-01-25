from flask import Flask, request, render_template
import speech_recognition as sr
from pydub import AudioSegment
import subprocess
import os
import my_tdmelodic, my_model, roman2kana, visualize

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
	if 'file' not in request.files:
		return "No file part"
	
	file = request.files['file']
	
	if file.filename == '':
		return "No selected file"
	
	if file:
		file = request.files['file']
		file_path = os.path.join(file.filename)
		file_name, file_extension = os.path.splitext(file_path)
		file.save(file_path)
		input_file = file_name + file_extension
		output_file = 'audio.wav'
		subprocess.run(["ffmpeg", "-i", input_file, "-ar", "16000", "-ac", "1", output_file, "-y"], stdout=subprocess.PIPE)
		os.remove(input_file)

		r = sr.Recognizer()
		with sr.AudioFile(output_file) as source:
			audio_data = r.listen(source)
			text = r.recognize_google(audio_data, language='ja-JP')
	return render_template("upload.html", text=text)


@app.route('/inference', methods=['POST'])
def inference():
	if 'text' not in request.form:
		return "No text part"
	
	text = request.form['text']
	
	if text:
		tdmelodic_result = my_tdmelodic.tdmelodic(text)
		model_result = my_model.model()
		nakadaka_result = roman2kana.convert(model_result)
		tdm_acc, tdm_lnum = visualize.visualize(tdmelodic_result)
		nkd_acc, nkd_lnum = visualize.visualize(nakadaka_result)
		return render_template("inference.html", tdm_acc = tdm_acc, nkd_acc = nkd_acc, lnum = max(tdm_lnum, nkd_lnum))


if __name__ == '__main__':
	app.run(debug=True)
