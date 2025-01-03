import streamlit as st
from typing import Callable, Optional


def page_group(param):
    key = f"{__name__}_page_group_{param}"

    if key not in st.session_state:
        st.session_state[key] = PageGroup(param)

    return st.session_state[key]


class PageGroup:

    def __init__(self, param):
        self._param: str = param
        self._default: str = None
        self._selected_page: str = None
        self._selected: str = None
        self._items: dict = {}

        # Fix some rollback issues when multiple pages are selected in the same run.
        self._backup: Optional[str] = None


    def return_boxes(self, key, selected, label, page):
        st.session_state[key] = selected
        st.checkbox(
            label, key=key, on_change=self._on_change, args=(page,), value=selected
        )

    def item(self, label: str, callback: Callable, default=False) -> None:
        self._backup = None
        page = self._normalize_label(label)
        key = f"{__name__}_{self._param}_{page}"
        
        if self._selected_page is None and default:
            self._selected_page = page

        is_selected = self._selected_page == page
        
        if self._items.get(key) is not None:
            self._items[key]["selected"] = is_selected
            self.return_boxes(key, is_selected, label, page)
            return
            
        self._items[key] = {
            "label": label,
            "callback": callback,
            "default": default,
            "selected": is_selected,
        }
        self.return_boxes(key, is_selected, label, page)

    def read_query(self):
        params = st.query_params
        if self._param in params:
            self._selected_page = params[self._param]
    
    def show(self) -> None:
        print('awdaw', self._selected_page)
        selected_items = list(filter(lambda item: item["selected"], self._items.values()))
        default_items = list(filter(lambda item: item["default"], self._items.values()))

        if len(selected_items) <= 0:
            for item in default_items:
                item["callback"]()
        else:
            for item in selected_items:
                item["callback"]()

    def _on_change(self, page: str) -> None:
        self._selected_page = page
        params = st.query_params

        if self._backup is None:
            if self._param in params:
                self._backup = params[self._param][0]
            params[self._param] = [page]
        else:
            params[self._param] = [self._backup]

        st.query_params = params

    def _normalize_label(self, label: str) -> str:
        return (
            "".join(char.lower() for char in label if char.isascii())
            .strip()
            .replace(" ", "-")
        )
