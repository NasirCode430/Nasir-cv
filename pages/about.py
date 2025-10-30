"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Displays the About page"""
    # --- Hero Section ---
    st.title("👨‍💻 Muhammad Nasir")
    st.caption("Lead Flutter Engineer | 8+ Years in Mobile App Development (Flutter | Android | Cross-Platform)")

    col1, col2 = st.columns([1.2, 2.8])

    with col1:
        st.image("https://cdn.truelancer.com/user-picture/2724270-6196b527e81a6.jpg", width=180)  # Optional profile image

    with col2:
        st.markdown(
            """
📍 **Islamabad, Pakistan** 🌍 *Remote — Cynergy Bank (UK)*  
📞 **+92 312 9038626** ✉️ [**muhammadnasir6688@gmail.com**](mailto:muhammadnasir6688@gmail.com)  
🔗 [**LinkedIn**](https://www.linkedin.com/in/muhammad-nasir-69a7b0233/) | [**GitHub**](https://github.com/muhammadnasir6688)
            """
        )

    st.divider()

    # --- Professional Summary ---
    st.subheader("🧭 Professional Summary")
    st.markdown(
        """
I am a **results-driven Lead Flutter Engineer** with over **8 years** of experience in designing and developing **scalable, secure, and enterprise-grade mobile applications**, including **2.5+ years of leadership experience** at **Cynergy Bank (UK)**.  

With a focus on **clean architecture, SOLID principles**, and **test-driven development**, I create mobile ecosystems that are both **highly performant** and **maintainable**.  
My leadership approach emphasizes technical excellence, code quality, and team empowerment to deliver impactful, user-first digital products.
        """
    )

    with st.expander("🔍 Key Highlights"):
        st.markdown(
            """
- 🚀 **Led Flutter development** for enterprise-grade fintech apps at Cynergy Bank (UK).  
- 🧩 Architected **modular, maintainable codebases** using SOLID & Clean Architecture.  
- ⚙️ Implemented **CI/CD pipelines** (Bitrise, GitHub Actions) ensuring automated testing & deployment.  
- 💬 Mentored cross-functional teams across remote environments with Agile delivery models.  
- 🏗️ Designed **secure API integrations** and scalable backend communication layers.  
            """
        )

    st.divider()

    # --- Areas of Expertise ---
    st.subheader("💼 Areas of Expertise")
    with st.expander("🚀 Areas of Expertise", expanded=True):
       for skill in [
        "✅ Flutter & Dart Architecture – Clean, Modular, SOLID",
        "✅ Android (Java/Kotlin) & Native Integrations",
        "✅ State Management – GetX, Bloc, Riverpod",
        "✅ Secure Mobile Banking Systems & Encryption",
        "✅ RESTful APIs, GraphQL, gRPC",
        "✅ Microservices & DevOps Integration (CI/CD)",
        "✅ App Store / Play Store Deployment & Maintenance",
    ]:
        st.write(skill)

    st.divider()

    # --- Technical Stack ---
    st.subheader("🧰 Tech Stack Highlights")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
**Languages:** Dart, Java, Kotlin, Python  
**Frameworks:** Flutter, Android SDK, Jetpack Compose  
**Architecture:** Clean, SOLID, MVVM, MVC  
**Testing:** Mockito, Flutter Test, Integration Tests  
            """
        )

    with col2:
        st.markdown(
            """
**Tools:** Firebase, Dio, Retrofit, GitHub Actions, Bitrise  
**Cloud & DevOps:** AWS, Docker, Firebase Hosting  
**Databases:** SQLite, MySQL, Firestore  
**Version Control:** Git, GitHub, GitLab  
            """
        )

    st.divider()

    # --- Philosophy ---
    st.subheader("💡 Engineering Philosophy")
    st.info(
        '"Clean code is not just written — it’s designed, reviewed, and evolved."  '
        "\nI believe in building products that combine clarity, maintainability, and long-term scalability."
    )

    st.divider()

    # --- Personal Touch ---
    st.subheader("🌱 Beyond Work")
    st.markdown(
        """
I’m passionate about **mentoring developers**, **architecting clean systems**, and exploring the intersection of **fintech and cross-platform engineering**.  
Outside of work, I enjoy learning new frameworks, contributing to open source, and sharing architectural best practices with the developer community.
        """
    )

    st.divider()

    # --- Connect Section ---
    st.subheader("🤝 Let’s Connect")
    st.markdown(
        """
📧 [**Email Me**](mailto:muhammadnasir6688@gmail.com) | 🔗 [**LinkedIn**](https://www.linkedin.com/in/muhammad-nasir-69a7b0233/) | 💻 [**GitHub**](https://github.com/muhammadnasir6688)
        """
    )

if __name__ == "__main__":
    write()
