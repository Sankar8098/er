import subprocess

def download_video(video_url, file_name, resolution):
    output_path = f"downloads/{file_name}_{resolution}.mp4"
    ffmpeg_cmd = ["ffmpeg", "-i", video_url, "-c", "copy", "-b:v", resolution, output_path]
    subprocess.run(ffmpeg_cmd)
    return output_path
