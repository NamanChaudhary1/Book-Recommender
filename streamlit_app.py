import streamlit as st
import pytube
from io import BytesIO

def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video_bytes = BytesIO()
    video.download(output_path=video_bytes)
    return video_bytes

def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        video_bytes = download_video(video_url)
        st.download_button(
            label="Click here to download the video",
            data=video_bytes,
            file_name="video.mp4",
            mime="video/mp4"
        )
        st.success("Video downloaded successfully!")

if __name__ == "__main__":
    main()
