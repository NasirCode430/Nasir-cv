"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the Skills page in the app"""
    st.title("⚙️ Skills Overview")

    with st.expander("💻 Programming Languages", expanded=True):
        st.markdown(
            """
- **Java**
- **Dart**
- **Python** *(Beginner)*
- **PHP**
- **JavaScript (Node.js – Beginner)*
            """
        )

    with st.expander("📱 Frameworks & Platforms", expanded=True):
        st.markdown(
            """
- **Flutter**
- **Laravel**
- **Android Development**
- **Streamlit** *(Beginner)*
            """
        )

    with st.expander("🧠 Tools & Technologies", expanded=False):
        st.markdown(
            """
- **MS Office Suite** – Excel, PowerPoint, Word, Project  
- **Version Control** – Git, GitHub  
- **API Integration** – RESTful APIs, JSON  
- **Database** – MySQL, Firebase, SQLite  
- **Basic Cloud Knowledge** – Firebase Hosting, AWS *(Intro Level)*
            """
        )

    with st.expander("📊 Other Skills", expanded=False):
        st.markdown(
            """
- Strong Problem-Solving & Debugging  
- UI/UX-Oriented Flutter App Development  
- Clean Architecture & SOLID Principles (Flutter)  
- Team Collaboration with GetX / MVC patterns
            """
        )

    st.markdown("---")
    st.markdown(
        "_“Code is like humor. When you have to explain it, it’s bad.”_ 😄"
    )

if __name__ == "__main__":
    write()
