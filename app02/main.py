import streamlit as st
from streamlit_option_menu import option_menu
import account, about, home, your_posts, trending

def main():
    st.set_page_config(
        page_title='Streamlit App', 
        page_icon='📊'
    )
    app = MultiApp()
    app.run()
    pass
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Menu title",
                options=['Home', 'Account', 'Trending', 'Your Posts', 'About'],
                icons=['1-circle', '2-circle', '3-circle', '4-circle', '5-circle'],   
                default_index= 0,
                menu_icon='0-circle'
            )
            if app == 'Home':
                home.app()
            elif app == 'Account':
                account.app()
            elif app == 'Trending':
                trending.app()
            elif app == 'Your Posts':
                your_posts.app()
            elif app == 'About':
                about.app()
if __name__ == '__main__':
    main()