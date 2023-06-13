import streamlit as st
import pytube
import os

def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    return video

def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        video = download_video(video_url)
        file_path = video.download(output_path="./Videos/")
        st.markdown(f"Download the video [here]({file_path})")
        st.success("Video downloaded successfully!")

if __name__ == "__main__":
    main()
