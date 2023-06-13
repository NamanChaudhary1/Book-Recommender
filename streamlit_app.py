import streamlit as st
import pytube
import tempfile
import os

def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    return video

def save_temporary_file(video):
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, "video.mp4")
    video.download(output_path=temp_file_path)
    return temp_file_path

def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        video = download_video(video_url)
        temp_file_path = save_temporary_file(video)
        st.markdown(get_download_link(temp_file_path), unsafe_allow_html=True)
        st.success("Video downloaded successfully!")

def get_download_link(file_path):
    with open(file_path, "rb") as file:
        file_bytes = file.read()
        base64_encoded = file_bytes.encode("base64").decode()
        href = f'<a href="data:file/mp4;base64,{base64_encoded}" download>Click here to download the video</a>'
        return href

if __name__ == "__main__":
    main()
