from pyrofoke import Client

def upload_video(client: Client, chat_id, file_path, caption):
    client.send_video(chat_id, file_path, caption=caption)
