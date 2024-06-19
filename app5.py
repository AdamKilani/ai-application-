from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def create_short_clips(video_path, segments, output_folder='shorts'):
    for i, (start, end) in enumerate(segments):
        output_path = f"{output_folder}/clip_{i}.mp4"
        ffmpeg_extract_subclip(video_path, start, end, targetname=output_path)
