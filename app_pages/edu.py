"""Education page shown when the user enters the application"""
import streamlit as st

def write():
    """Displays the Education page in the app"""
    st.title("🎓 Education")

    # --- Bachelor's Degree Section ---
    st.subheader("Bachelor of Science in Computer Science")
    st.markdown("**2014 – 2018** ")
    st.markdown("**GPA:** *[3.4/4.0]*")

    with st.expander("📘 Key Courses"):
        st.markdown(
            """
            - Object-Oriented Programming (Java)  
            - Data Structures & Algorithms  
            - Database Management Systems  
            - Web Development (PHP, Laravel)  
            - Mobile Application Development (Android, Flutter)  
            - Software Engineering  
            - Computer Networks  
            - Operating Systems  
            """
        )

    st.divider()

    # --- Certifications Section ---
    st.subheader("📚 Certifications & Online Learning")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("**🎓 Coursera | Streamlit for Data Science (Beginner)**")
            st.markdown("[View Credential](https://www.coursera.org)")
            st.caption("Covered fundamentals of Streamlit, layout design, and interactive dashboards.")

        with st.container(border=True):
            st.markdown("**💡 Udemy | Flutter & Dart Development Bootcamp**")
            st.caption("Comprehensive hands-on course covering UI design, API integration, and app architecture.")

    with col2:
        with st.container(border=True):
            st.markdown("**🧩 LinkedIn Learning | Git & Version Control**")
            st.caption("Practical understanding of branching, merging, and release workflows for collaborative projects.")

        with st.container(border=True):
            st.markdown("**☁️ AWS Cloud Practitioner Essentials (Optional)**")
            st.caption("Introduction to core AWS services, IAM roles, EC2, and S3.")

    st.divider()

    st.markdown(
        """
        _“Education is not the learning of facts, but the training of the mind to think.”_  
        — **Albert Einstein**
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    write()
