def find_interesting_segments(audio_features, video_frames, threshold=0.5):
    times, onset_env = audio_features
    peaks = times[onset_env > threshold]
    segments = []
    for peak in peaks:
        start_time = max(0, peak - 2)  # 2 seconds before the peak
        end_time = min(len(video_frames), peak + 2)  # 2 seconds after the peak
        segments.append((start_time, end_time))
    return segments
