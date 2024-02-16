
# Video Subtitle Generator
This Python script generates SRT format subtitles from a video file. It extracts the audio using FFmpeg, performs speech recognition, and creates a timed subtitle file.

# Prerequisites
- `FFmpeg`: Install from here https://ffmpeg.org
- `speech_recognition` python library: "pip3 install speech_recognition"

# Usage
- Save this script in the same directory as your video file.
- Run the following: 'python generate_subtitles.py your_video.mp4'
- An SRT file named `subtitles.srt` will be created in the same directory.
