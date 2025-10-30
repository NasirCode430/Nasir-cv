"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the Projects page in the app.py file"""
    st.title("👨‍💻 Projects Showcase")

    st.markdown("### 📱 Mobile App Projects")

    projects = [
        {
            "title": "Find My Lost Phone – Mobologics",
            "tools": "Android Studio, Firebase Realtime Database",
            "link": "https://play.google.com/store/apps/details?id=com.findmyphone.findmydevice&hl=en",
            "description": "Developed a real-time phone tracking and recovery app using Firebase, WebRTC, and FCM notifications."
        },
        {
            "title": "Speak & Translate – All Languages – Mobologics",
            "tools": "Android Studio, Google Translation API, Firebase, AdMob",
            "link": "https://play.google.com/store/apps/details?id=com.alllanguagetranslator.voicetranslation&hl=en",
            "description": "Built a multilingual translation app with voice recognition and background translation services."
        },
        {
            "title": "VPN Browser – Mobologics",
            "tools": "Android Studio, WebView, AdMob, Facebook Ads",
            "link": "https://play.google.com/store/apps/details?id=com.vpnbrowser.securebrowser&hl=en",
            "description": "Created a secure browser with built-in VPN functionality and ad monetization."
        },
        {
            "title": "Route Planner – TechNest",
            "tools": "Flutter, Google Maps API, MapBox SDK, SQLite",
            "link": "https://play.google.com/store/apps/details?id=com.app.freevideodownloader.allvideodownloader.fb.insta.video.downloader",
            "description": "Implemented a route optimization app integrating MapBox and Google Maps for smooth navigation."
        },
        {
            "title": "Remove Objects 2021 – TechNest",
            "tools": "Android Studio (Java), OpenCV, AdMob",
            "link": "https://play.google.com/store/apps/details?id=remove.unwanted.object",
            "description": "Developed an AI-powered photo editing app for removing unwanted objects using OpenCV."
        },
        {
            "title": "Photo Video Maker 2021 – TechNest",
            "tools": "Android Studio (Java), OpenCV, NDK",
            "link": "https://play.google.com/store/apps/details?id=com.app.video.maker.videoeditor.videotrimmer.photovideomaker.audioconverter",
            "description": "Built a multimedia editor for creating photo slideshows and trimming videos with background music."
        },
        {
            "title": "Photo Background Changer – TechNest",
            "tools": "Android Studio (Java), OpenCV",
            "link": "https://play.google.com/store/apps/details?id=com.apps.photo.backgroundchanger.backgrounderaser.removebackground.autocutter",
            "description": "Created a background remover app with AI-based segmentation and auto-cut features."
        },
        {
            "title": "Chatto App – Peek International *(In Progress)*",
            "tools": "Flutter, WebRTC, Socket.IO, REST APIs",
            "link": None,
            "description": "Developing a real-time chat and video calling SDK for enterprise communication."
        },
        {
            "title": "Ringy – Peek International",
            "tools": "Flutter, WebRTC, Jitsi SDK, Retrofit API",
            "link": "https://play.google.com/store/apps/details?id=com.ringy.ringychat",
            "description": "Engineered a cross-platform chat and video call app using Flutter and Jitsi Meet SDK."
        },
        {
            "title": "Maps & Navigation – Mobologics",
            "tools": "Android Studio, Google Maps API, MapBox",
            "link": "https://play.google.com/store/apps/details?id=com.gpsnavigationmaps.routefinder&hl=en",
            "description": "Implemented GPS navigation app with real-time routing, geolocation, and live map integration."
        },
    ]

    # Display all projects in collapsible expanders
    for project in projects:
        with st.expander(f"📂 {project['title']}", expanded=False):
            st.markdown(f"**🧰 Tools:** {project['tools']}")
            if project["link"]:
                st.markdown(f"🔗 [Google Play Link]({project['link']})")
            st.markdown(f"📄 {project['description']}")

    st.markdown("---")
    st.markdown("_“Turning ideas into digital products that make a difference.”_ 💡")

if __name__ == "__main__":
    write()
