import librosa

def extract_audio_features(file_path):
    y, sr = librosa.load(file_path)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.times_like(onset_env, sr=sr)
    return times, onset_env
