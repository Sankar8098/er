import requests

def get_zee5_metadata(url):
    video_id = url.split("/")[-1]
    api_url = f"https://gwapi.zee5.com/content/details/{video_id}?translation=en&country=IN"
    stream_url = f"https://spapi.zee5.com/player/getDetails?content_id={video_id}&platform_name=web"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(api_url, headers=headers)
    stream_response = requests.get(stream_url, headers=headers)
    
    if response.status_code == 200 and stream_response.status_code == 200:
        data = response.json()
        stream_data = stream_response.json()
        return data.get("title"), data.get("description"), data.get("image"), stream_data.get("video", {}).get("hls", "")
    return None, None, None, None
