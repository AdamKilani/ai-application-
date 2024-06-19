from flask import Flask, request, jsonify
from flask_cors import CORS
from app1 import download_video
from app2 import extract_audio_features
from app3 import extract_video_frames
from app4 import find_interesting_segments
from app5 import create_short_clips

app = Flask(__name__)
CORS(app)

@app.route('/generate_shorts', methods=['POST'])
def generate_shorts():
    print("Received request")
    try:
        data = request.json
        url = data.get('url')
        print(f"URL received: {url}")
        video_path = download_video(url)
        
        # Process video to find interesting segments
        audio_features = extract_audio_features(video_path)
        video_frames = extract_video_frames(video_path)
        segments = find_interesting_segments(audio_features, video_frames)
        
        # Create short clips
        create_short_clips(video_path, segments)
        
        print("Shorts created successfully")
        return jsonify({'message': 'Shorts created successfully'})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

