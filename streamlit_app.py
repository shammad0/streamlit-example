from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc
import streamlit_canvas as st_canvas

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):

    # Define the dimensions of the canvas
    canvas_width = 500
    canvas_height = 500

    # Define the initial coordinates of the first box
    x1, y1 = 100, 100

    # Define the size of the boxes
    box_width, box_height = 100, 50

    # Define the canvas
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)", stroke_width=2, stroke_color="red",
        background_color="#FFF", height=canvas_height, width=canvas_width,
        drawing_mode="free", key="canvas")

    # If the user has drawn something on the canvas
    if canvas_result.image_data is not None:

        # Draw the first box
        st_canvas.draw_rectangle(canvas_result.image_data, x1, y1, x1 + box_width, y1 + box_height)

        # Draw the arrows and boxes for the subsequent steps based on user input
        if st.button('Add Step'):
            x2, y2 = x1, y1 + box_height + 50
            st_canvas.draw_line(canvas_result.image_data, x1 + box_width/2, y1 + box_height, x2 + box_width/2, y2)
            st_canvas.draw_rectangle(canvas_result.image_data, x2, y2, x2 + box_width, y2 + box_height)
            x1, y1 = x2, y2

    # Display the canvas
    stc.html(canvas_result._get_streamlit_html())
