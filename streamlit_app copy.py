import streamlit as st
from streamlit_elements import elements, mui, html
import time
import threading
from datetime import datetime

time_till_date = (0, 0, 0, 0)


# def main():
#     st.title("Dashboard by Sean")
#     with elements("nested_children"):
#         with mui.Paper:
#             with mui.Card:
#                 with mui.CardContent:
#                     with mui.Typography:
#                         html.h1("Hello world")
#                         # elementT = html.p("Hello world")

#                         # print(elementT)
#                         # elementT.text = "Goodbye world"
#                         # st.set_page_config()
#                         # mui.Button("By Sean", onClick=clicke(), variant="contained", color="success")
#                         html.h2(f"Time until: {future_datetime.strftime('%Y-%m-%d')}")
#                         html.b(f"{time_till_date[0]} days, {time_till_date[1]} hours, {time_till_date[2]} minutes, {time_till_date[3]} seconds")
#                         # ph = st.empty()
#                         # N = 5*60
#                         # for secs in range(N,0,-1):
#                         #     mm, ss = secs//60, secs%60
#                         #     ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#                         #     time.sleep(1)
#                         N = 5*60
#                         for secs in range(N,0,-1):
#                         #     mm, ss = secs//60, secs%60
#                             mui.Typography("countdown")
#                         #     # ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#                         #     time.sleep(1)
#     pass

# if __name__ == "__main__":
#     st.set_page_config(page_title="Dashboard by Sean", page_icon="🎈", layout="wide")
#     main()



import os
import streamlit as st
import asyncio


backgroundText= None
# Define variable to track the tasks
if 'keep_running' not in st.session_state:
    st.session_state.keep_running = False

future_datetime = datetime(2034, 1, 27, 0, 0, 0)

# # Any asyncronous task
# async def run_task():
#     while st.session_state.keep_running:
#         print('Background Task running...')
#         backgroundText.metric('Background Task', 'Running')
#         await asyncio.sleep(1)


def time_until(target_datetime):
    now = datetime.now()
    delta = target_datetime - now
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds

# Any asyncronous task
async def run_task():
    while st.session_state.keep_running:
        print('Background Task running...')
        # backgroundText.metric('Background Task', 'Running')
        # backgroundText("Background Task", "Running")
        st.session_state["countDown"] = "Running"
        # time_till_date = time_until(future_datetime)
        st.rerun()
        # backgroundText= html.h3('Background Task ', 'Running')
        # html.b(f"{time_till_date[0]} days, {time_till_date[1]} hours, {time_till_date[2]} minutes, {time_till_date[3]} seconds")
        await asyncio.sleep(1)

# Streamlit
# def main():
#     st.title('Background Task with streamlit')

#     st.session_state.keep_running = True
#     global backgroundText
#     st.session_state["countDown"] = "Offline"

#     with elements("nested_children"):
#         with mui.Paper:
#             with mui.Card:
#                 with mui.CardContent:
#                     with mui.Typography:
#                         html.h1("Hello world")
#                         # elementT = html.p("Hello world")

#                         # print(elementT)
#                         # elementT.text = "Goodbye world"
#                         # st.set_page_config()
#                         # mui.Button("By Sean", onClick=clicke(), variant="contained", color="success")
#                         html.h2(f"Time until: {future_datetime.strftime('%Y-%m-%d')}")
#                         # html.b(f"{time_till_date[0]} days, {time_till_date[1]} hours, {time_till_date[2]} minutes, {time_till_date[3]} seconds")

#                         html.h3('Background Task ', st.session_state["countDown"])
#                         # ph = st.empty()
#                         # N = 5*60
#                         # for secs in range(N,0,-1):
#                         #     mm, ss = secs//60, secs%60
#                         #     ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#                         #     time.sleep(1)
#                         # N = 5*60
#                         # for secs in range(N,0,-1):
#                         # #     mm, ss = secs//60, secs%60
#                         #     mui.Typography("countdown")
#                         # #     # ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
#                         # #     time.sleep(1)
#     if st.session_state.keep_running:
#         st.toast('Running background Tasks', icon='🤖')
#         # THE CODE IS STUCK HERE
#         asyncio.run(run_task())
#     else:
#         os.system('cls' if os.name == 'nt' else 'clear')

# # Execute Streamlit
# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import numpy as np
def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1

    st.write("Time Up!")

def main():
    st.title("Pomodoro")
    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=25)

    time_in_seconds = time_minutes * 60
    if st.button("START"):
        count_down(int(time_in_seconds))
        # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        # st.bar_chart(chart_data)
    else:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.bar_chart(chart_data)
if __name__ == '__main__':
    main()