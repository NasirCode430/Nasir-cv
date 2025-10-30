"""📦 Common Components and Utilities for the Streamlit Portfolio App

This module contains helper functions and UI components used across the app.
It handles dynamic page loading, embeds media content, extends default Streamlit widgets,
and includes small UI utilities like horizontal rulers and styled titles.

Author: Muhammad Nasir
"""

import base64
import importlib
import logging
import sys
from typing import Any, List

import streamlit as st

# ------------------------------------------------------
# ✅ Logging Configuration
# ------------------------------------------------------
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


# ------------------------------------------------------
# 🔁 Page Reload and Writer
# ------------------------------------------------------
def _reload_module(page):
    """
    Reloads a specified Streamlit page/module.
    Used for hot-reloading deeply imported modules when developing locally.

    Args:
        page (module): A Python module representing a page.
    """
    logging.debug(f"Attempting reload of module: {page.__name__}")
    try:
        importlib.import_module(page.__name__)
        importlib.reload(page)
    except ImportError:
        logging.warning(f"Could not reload module: {page.__name__}")


def write_page(page):
    """
    Writes the specified Streamlit page/module to the app.

    Each module must contain a `def write()` function.

    Args:
        page (module): A module with a `write()` function.
    """
    try:
        page.write()
    except AttributeError:
        logging.error(f"The module {page.__name__} does not have a write() function.")


# ------------------------------------------------------
# 🎥 YouTube Video Embed
# ------------------------------------------------------
def video_youtube(src: str, width: str = "100%", height: int = 315):
    """
    Embeds a YouTube video inside the Streamlit app.

    Args:
        src (str): YouTube embed URL (e.g. 'https://www.youtube.com/embed/VIDEO_ID').
        width (str, optional): Video width. Defaults to "100%".
        height (int, optional): Video height. Defaults to 315.
    """
    st.markdown(
        f"""
        <iframe width="{width}" height="{height}" src="{src}" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------
# 🧩 Multiselect Helper
# ------------------------------------------------------
def multiselect(
    label: str,
    options: List[Any],
    default: List[Any],
    format_func=str,
) -> List[Any]:
    """
    Extends Streamlit's multiselect widget to support object-based selections
    (not just strings).

    Args:
        label (str): The label for the widget.
        options (List[Any]): List of selectable objects.
        default (List[Any]): Default selected objects.
        format_func (function, optional): Function to format object display. Defaults to `str`.

    Returns:
        List[Any]: The selected objects.
    """
    options_dict = {format_func(option): option for option in options}
    default_labels = [format_func(option) for option in default]

    selected_labels = st.multiselect(
        label, options=list(options_dict.keys()), default=default_labels
    )
    return [options_dict[label] for label in selected_labels]


# ------------------------------------------------------
# 🏷️ Styled Title with “Awesome” Badge
# ------------------------------------------------------
def title_awesome(body: str):
    """
    Displays a custom title with the 'Awesome Streamlit' badge and link.

    Args:
        body (str): The text to display after 'Awesome Streamlit'.
    """
    st.markdown(
        f"""
        # Awesome Streamlit {body} 
        [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/
        d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]
        (https://github.com/MarcSkovMadsen/awesome-streamlit)
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------
# 🖼️ SVG Renderer
# ------------------------------------------------------
def write_svg(svg: str):
    """
    Renders an inline SVG image in Streamlit using base64 encoding.

    Args:
        svg (str): SVG XML as string.
    """
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" style="max-width:100%;"/>'
    st.markdown(html, unsafe_allow_html=True)


# ------------------------------------------------------
# ➖ Horizontal Ruler
# ------------------------------------------------------
def horizontal_ruler(in_sidebar: bool = False):
    """
    Inserts a horizontal separator (like <hr> in HTML).

    Args:
        in_sidebar (bool, optional): If True, inserts in sidebar. Defaults to False.
    """
    markdown_target = st.sidebar if in_sidebar else st
    markdown_target.markdown("---")
