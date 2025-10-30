"""Professional Recommendations Page — Streamlit Version"""
import streamlit as st

def write():
    """Renders the Recommendations page in the Streamlit application."""
    st.set_page_config(page_title="💬 Recommendations", layout="wide")

    # --- Page Header ---
    st.title("💬 Recommendations & Testimonials")
    st.markdown(
        "<p style='font-size:18px; color:gray;'>Words from leaders, peers, and collaborators who’ve experienced my work first-hand.</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # --- Recommendation 1 ---
    with st.container():
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/1946/1946429.png", width=70)
        with col2:
            st.subheader("🗣️ Faizan Ahmed")
            st.caption("**Head of Digital Transformation | Cynergy Bank (UK)** · April 2024 · [LinkedIn](https://www.linkedin.com/)")
            st.markdown(
                """
                > *"Nasir is a technically brilliant and dependable engineer who has been pivotal in scaling our mobile banking platform.  
                > His mastery of Flutter architecture and ability to lead distributed teams make him an indispensable asset.  
                > He consistently delivers high-quality, secure, and maintainable code — often exceeding expectations to ensure project success."*
                """
            )

    st.divider()

    # --- Recommendation 2 ---
    with st.container():
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/2922/2922561.png", width=70)
        with col2:
            st.subheader("👩‍💻 Sara Khan")
            st.caption("**Senior Software Engineer | Peek International** · November 2023 · [LinkedIn](https://www.linkedin.com/)")
            st.markdown(
                """
                > *"Working with Nasir was a masterclass in clean architecture and craftsmanship.  
                > His commitment to SOLID principles streamlined our development workflow and boosted overall team velocity.  
                > Beyond his technical skill, Nasir’s mentorship profoundly shaped my growth as both a developer and a problem-solver.  
                > A true leader who brings clarity and quality to every project."*
                """
            )

    st.divider()

    # --- Recommendation 3 ---
    with st.container():
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70)
        with col2:
            st.subheader("🔧 James Walker")
            st.caption("**CTO | TechNest Solutions** · August 2022 · [LinkedIn](https://www.linkedin.com/)")
            st.markdown(
                """
                > *"Nasir is among the rare engineers who combine technical excellence with exceptional leadership.  
                > His work on our cross-platform initiatives brought reliability, scalability, and performance to our mobile apps.  
                > He set a gold standard for code quality, CI/CD automation, and architectural rigor across the engineering organization."*
                """
            )

    st.divider()

    # --- Peer Quotes ---
    st.markdown("### 💡 What People Say")
    st.markdown(
        """
        > “Clean, scalable, and forward-thinking — that’s how Nasir codes.”  
        >  
        > “A dependable leader who inspires both confidence and curiosity.”  
        >  
        > “He doesn’t just solve problems — he engineers long-term solutions.”  
        """
    )

    st.divider()

    # --- Contact ---
    st.markdown("### 🤝 Let’s Collaborate")
    st.markdown(
        """
        If you’d like to share a recommendation or discuss a project collaboration, feel free to connect:  
        📧 [**muhammadnasir6688@gmail.com**](mailto:muhammadnasir6688@gmail.com) | 🔗 [**LinkedIn**](https://www.linkedin.com/in/muhammad-nasir-69a7b0233/)
        """
    )

if __name__ == "__main__":
    write()
