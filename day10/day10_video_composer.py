import json
import os
from moviepy import ImageClip, AudioFileClip, TextClip, CompositeVideoClip

def create_video():
    # 1. Load the manifest
    with open("video_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    print(f"Loaded manifest: {manifest['title']}")
    
    # 2. Load audio and get duration
    audio = AudioFileClip(manifest['audio_path'])
    duration = audio.duration
    print(f"Audio duration: {duration:.2f} seconds")
    
    # 3. Create background image clip
    # Set the duration to match the audio
    bg_clip = ImageClip(manifest['bg_image']).with_duration(duration)
    
    # 4. Create text overlay
    # Using Noto Sans CJK SC Regular
    font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    
    # Ensure size is integer
    text_width = int(bg_clip.w * 0.8)
    
    text_clip = TextClip(
        text=manifest['text'],
        font=font_path,
        font_size=int(manifest['style']['font_size']),
        color=manifest['style']['color'],
        method='caption',
        size=(text_width, None)
    ).with_duration(duration).with_position('center')
    
    # 5. Combine everything
    # Background + Text
    video = CompositeVideoClip([bg_clip, text_clip])
    # Set the audio
    video = video.with_audio(audio)
    
    # 6. Export the video
    output_filename = "midnight_haven_ep01.mp4"
    print(f"Exporting video to {output_filename}...")
    
    # MoviePy v2: write_videofile
    video.write_videofile(output_filename, fps=24, codec="libx264", audio_codec="aac")
    
    print("Video creation complete!")

if __name__ == "__main__":
    try:
        create_video()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"An error occurred: {e}")
