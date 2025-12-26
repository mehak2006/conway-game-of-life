import streamlit as st
import time
import tomllib

from rplife.grid import LifeGrid
from rplife.patterns import get_pattern, PATTERNS_FILE

# ---------- Page setup ----------
st.set_page_config(layout="wide")
st.title("Conway's Game of Life")

# ---------- Load all pattern names safely ----------
data = tomllib.loads(PATTERNS_FILE.read_text(encoding="utf-8"))
pattern_names = sorted(data.keys())

# ---------- UI controls ----------
pattern_name = st.selectbox(
    "Choose pattern",
    pattern_names
)

generations = st.slider("Generations", 10, 300, 100)
fps = st.slider("Frames per second", 1, 20, 7)
cell_size = st.slider("Cell size (px)", 8, 30, 15)

# Camera window
bbox = (0, 0, 60, 25)

# ---------- HTML renderer ----------
def render_html(grid, bbox, cell_size):
    start_col, start_row, end_col, end_row = bbox
    html = "<div style='line-height:0;'>"

    for row in range(start_row, end_row):
        html += "<div style='display:flex;'>"
        for col in range(start_col, end_col):
            if (row, col) in grid.pattern.alive_cells:
                age = grid.ages.get((row, col), 1)
                if age <= 2:
                    color = "#2ecc71"
                elif age <= 5:
                    color = "#f1c40f"
                else:
                    color = "#e74c3c"
            else:
                color = "#111111"

            html += (
                f"<div style='width:{cell_size}px;"
                f"height:{cell_size}px;"
                f"background-color:{color};"
                f"margin:1px'></div>"
            )
        html += "</div>"

    html += "</div>"
    return html

# ---------- Run simulation ----------
if st.button("Run"):
    pattern = get_pattern(pattern_name)
    grid = LifeGrid(pattern)

    placeholder = st.empty()

    for _ in range(generations):
        placeholder.markdown(
            render_html(grid, bbox, cell_size),
            unsafe_allow_html=True
        )
        grid.evolve()
        time.sleep(1 / fps)
