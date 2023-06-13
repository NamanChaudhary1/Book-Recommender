import streamlit as st
from Youtube_Downloader.youtube import download

def main():
    st.title("YouTube Video Downloader")

    link = st.text_input("Enter YouTube video link:")
    path = st.text_input("Enter the path to save the video:")

    if st.button("Download"):
        video = download(link, path)
        video.Download_video_in_360_resolution()
        with open(path, "rb") as f:
            st.download_button(
                label="Click here to download the video",
                data=f,
                file_name="video.mp4",
                mime="video/mp4"
            )
        st.success("Video downloaded successfully!")

if __name__ == "__main__":
    main()
