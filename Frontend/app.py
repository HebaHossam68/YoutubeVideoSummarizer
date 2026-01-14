import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model_API.Call_API import summarize_youtube_video

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon="🎬",
    layout="wide",
)

# ---------------------------
# Custom CSS for Cards, Buttons & Gradient
# ---------------------------
st.markdown("""
<style>
.card {
    background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}
h1, h2, h3 {
    color: #0077b6;
}
.stButton>button {
    background-color: #0077b6;
    color: white;
    height: 45px;
    width: 160px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #0096c7;
}
.copy-btn {
    background-color: #00b4d8;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
}
.copy-btn:hover {
    background-color: #0096c7;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Page Header
# ---------------------------
st.markdown("<h1 style='text-align:center;'>🎬 YouTube Video Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px;'>Paste your YouTube video link and get a professional summary instantly!</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2 = st.tabs(["💡 Video Summary", "📝 Instructions"])

with tab1:
    video_url = st.text_input("Enter the YouTube video link here:", "")

    if st.button("Get Summary"):
        if video_url.strip() == "":
            st.warning("Please enter a valid YouTube link.")
        else:
            with st.spinner("Generating summary..."):
                try:
                    summary = summarize_youtube_video(video_url)
                    st.success("✅ Summary generated successfully!")

                    # Card with summary
                    st.markdown(f"""
                    <div class="card">
                        <h3>📝 Video Summary:</h3>
                        <p>{summary}</p>
                        <button class="copy-btn" onclick="navigator.clipboard.writeText(`{summary}`)">📋 Copy Summary</button>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"An error occurred: {e}")

with tab2:
    st.markdown("""
    <div class="card">
        <h3>How to use this app:</h3>
        <ul>
            <li>Copy the YouTube video link.</li>
            <li>Paste it in the "Enter the YouTube video link here" field.</li>
            <li>Click the "Get Summary" button.</li>
            <li>Wait a few seconds to see your summary displayed in a professional card.</li>
            <li>Click the "📋 Copy Summary" button to copy the text instantly.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:12px; color:gray;">
    Developed with ❤️ by Heba Hossam
</div>
""", unsafe_allow_html=True)
