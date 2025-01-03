import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group

def main():
    # st.write("Hello, world!")   
    page = page_group("p")
    page.read_query()

    with st.sidebar:
        st.title("Sean's Gallery")
        with st.expander("✨ Documents", True):
            page.item("Readme", apps.gallery, default=True)
        with st.expander("🧩 COMPONENTS", True):
            page.item("Dashboard", components.elements)
            page.item("Count Down", components.count_down)
    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Gallery by Okld", page_icon="🎈", layout="wide")
    main()
