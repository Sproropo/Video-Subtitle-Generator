import sys
import subprocess
import speech_recognition as sr

# Check if the video file path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the path to the video file as an argument.")
    sys.exit(1)

video_file = sys.argv[1]
audio_file = "temp_audio.wav"
srt_file = "subtitles.srt"

# Extract audio from video using ffmpeg
ffmpeg_command = [
    'ffmpeg',
    '-i', video_file,
    '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2',
    audio_file
]

try:
    subprocess.run(ffmpeg_command, check=True)
except subprocess.CalledProcessError as e:
    print("Error occurred during audio extraction.")
    print(e)
    sys.exit(1)

# Speech Recognition
r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

transcription = r.recognize_google(audio)

# Generate SRT subtitles
lines = transcription.split('\n')
num_lines = len(lines)

# Calculate the duration per subtitle line
total_duration = num_lines * 0.5  # Adjust the duration per line as needed
start_time = 0.0

with open(srt_file, 'w') as f:
    for i, line in enumerate(lines):
        if line.strip():
            end_time = start_time + 0.5  # Adjust the duration per line as needed

            start_timecode = format(start_time, '.3f').replace('.', ',')
            end_timecode = format(end_time, '.3f').replace('.', ',')

            f.write(f"{i+1}\n")
            f.write(f"{start_timecode} --> {end_timecode}\n")
            f.write(f"{line}\n")
            f.write("\n")

            start_time = end_time

print("SRT subtitles generated successfully.")
