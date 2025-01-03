
import streamlit as st

from streamlit_elements import elements, sync, event
from streamlit_elements import elements, mui, html

from datetime import datetime

future_datetime = datetime(2034, 1, 27, 0, 0, 0)

def time_until(target_datetime):
    now = datetime.now()
    delta = target_datetime - now
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds

def main():
    time_till_date = time_until(future_datetime)
    with elements("count_down"):
        with mui.Paper(elevation=3, variant="outlined"):
            with mui.Typography:
                with mui.Card:
                    with mui.CardContent:
                        
                        with mui.Box(
                            sx={
                                "p": 2,
                                "minWidth": 300,
                                "textAlign": "center",
                            }
                        ):
                            html.h1("Count down")
                            html.h2(f"Until: {future_datetime.strftime('%Y-%m-%d')}")
                            html.h4(f"{time_till_date[0]} days")


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
