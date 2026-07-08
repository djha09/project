import streamlit as st
from pipeline import runSearch

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
)

# ---------- CSS ----------
st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.block-container{
    padding-top:2rem;
}

.title{
    font-size:55px;
    font-weight:800;
    background: linear-gradient(90deg,#00DBDE,#FC00FF);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    color:#A9A9A9;
    font-size:18px;
}

.step-box{
    background:#161B22;
    padding:18px;
    border-radius:12px;
    border:1px solid #2A2F3A;
    margin-bottom:15px;
}

.report{
    background:#161B22;
    padding:20px;
    border-radius:15px;
    border:1px solid #30363D;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<p class="title">🤖 AI Research Assistant</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Search • Read • Write • Critique • Rewrite</p>',
    unsafe_allow_html=True
)

st.divider()

# ---------- Sidebar ----------
with st.sidebar:

    st.header("⚙️ Settings")

    topic = st.text_input(
        "Research Topic",
        placeholder="Example: Artificial General Intelligence"
    )

    run = st.button(
        "🚀 Generate Report",
        use_container_width=True
    )

    st.divider()

    st.info(
        """
        **Pipeline**

        🔍 Search

        📖 Scrape

        ✍️ Write

        🧐 Critique

        ♻️ Rewrite
        """
    )

# ---------- Main ----------

if run:

    if topic == "":
        st.warning("Please enter a topic.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    with st.spinner("Running AI Research Pipeline..."):

        status.info("🔍 Searching...")
        progress.progress(15)

        state = runSearch(topic)

        progress.progress(100)
        status.success("Completed Successfully!")

    st.success("Research Finished!")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔍 Search",
        "📖 Scraped",
        "📝 Report",
        "🧐 Critique",
        "✨ Final"
    ])

    with tab1:
        st.markdown(state["search_results"])

    with tab2:
        st.markdown(state["scraped_content"])

    with tab3:
        st.markdown(state["report"])

    with tab4:
        st.markdown(state["feedback"])

    with tab5:

        st.markdown("## ✨ Final Report")

        st.markdown(state["rewrite"])

        st.download_button(
            "📥 Download Report",
            state["rewrite"],
            file_name="research_report.md",
            mime="text/markdown"
        )