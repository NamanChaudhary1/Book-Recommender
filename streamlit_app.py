import streamlit as st
import khtube

def download_video(url):
    video = khtube.single_video(url, quality="best")
    return video

def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        video = download_video(video_url)
        st.download_button(
            label="Click here to download the video",
            data=video,
            file_name="video.mp4",
            mime="video/mp4"
        )
        st.success("Video downloaded successfully!")

if __name__ == "__main__":
    main()
