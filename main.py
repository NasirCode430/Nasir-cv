### Main page for streamlit resume
import streamlit as st
import time
import pages.about
import pages.skills
import pages.projects
import pages.edu
import pages.recommendations

import resources.ast as ast

PAGES = {
    "About": pages.about,
    "Education" : pages.edu,
    "Skills": pages.skills,
    "Projects": pages.projects,
    "Recommendations": pages.recommendations
}


def main():
    """Main function of App with a professional sidebar"""
    # --- Sidebar Branding ---
    with st.sidebar:
        st.markdown(
            "<h2 style='text-align:center; margin-top:-10px;'>Muhammad Nasir</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align:center; color:gray; font-size:14px;'>Lead Flutter Engineer</p>",
            unsafe_allow_html=True
        )
        st.markdown("---")

        # --- Navigation ---
        st.markdown("### 🧭 Navigation")
        selection = st.radio(
            "Choose a section:",
            list(PAGES.keys()),
            label_visibility="collapsed",
            key="nav_radio"
        )
        st.markdown("<br>", unsafe_allow_html=True)

        # --- Hire Me Section ---
        st.markdown("### 💼 Hire Me")
        st.info(
            """
            🚀 **Available for Remote & Contract Roles**

            📧 [**Email Me**](mailto:muhammadnasir6688@gmail.com)  
            🔗 [**LinkedIn Profile**](https://www.linkedin.com/in/muhammad-nasir-69a7b0233/)
            """
        )

        # --- Quick Stats / Highlights ---
        st.markdown("---")
        st.markdown("### 📊 Highlights")
        st.markdown(
            """
            - 🧠 8+ Years in Software Development  
            - 💻 Expert in Flutter, Android, Clean Architecture  
            - 🌍 Worked remotely with UK-based teams  
            - 🏆 Passionate about scalable mobile systems
            """
        )

        # --- Footer Section ---
        st.markdown("---")
        st.caption(
            "📱 Built with ❤️ using **Streamlit**",
            unsafe_allow_html=True
        )

    # --- Page Loading Spinner ---
    page = PAGES[selection]
    with st.spinner(f"✨ Loading {selection} ..."):
        time.sleep(0.3)
        ast.write_page(page)


if __name__ == "__main__":
    main()

