import streamlit as st
import pytube

def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    return video.title

def main():
    st.title("YouTube Video Downloader")

    video_url = st.text_input("Enter the YouTube video URL:")

    if st.button("Download"):
        video_title = download_video(video_url)
        st.success("Video downloaded successfully!")

        # Provide a download link to the user
        video_path = f"./{video_title}.mp4"
        st.markdown(f"Download the video: [Video Download Link]({video_path})")

if __name__ == "__main__":
    main()
