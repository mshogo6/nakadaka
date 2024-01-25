from huggingsound import SpeechRecognitionModel

def model():
	model = SpeechRecognitionModel("mshogo6/nakadaka", device='cpu')
	audio_paths = ['./audio.wav']
	transcriptions = model.transcribe(audio_paths, batch_size=1)
	return transcriptions[0]['transcription']