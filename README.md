# Conway’s Game of Life — Interactive Visualization

An interactive, browser-based visualization of **Conway’s Game of Life**, built in Python and deployed using **Streamlit**.

This project explores **cellular automata**, emergent behavior, and how simple local rules can lead to complex global patterns.

🔗 **Live app:**  
👉 https://conway-game-of-life-uhwekm3s7cdqucq9fp5vke.streamlit.app/

---

## 🧠 About Conway’s Game of Life

Conway’s Game of Life is a zero-player game invented by mathematician John Conway.  
Each cell on an infinite grid is either *alive* or *dead*, and the grid evolves in discrete time steps according to simple rules based on neighboring cells.

Despite its simplicity, the Game of Life is:
- computationally universal (Turing complete),
- a classic example of emergence,
- widely studied in mathematics and computer science.

---

## ✨ Features of This Implementation

- Interactive **Streamlit web app**
- All available Life patterns selectable dynamically
- **Color-coded cells based on age**
  - 🟢 young cells
  - 🟡 mature cells
  - 🔴 old cells
- Adjustable controls:
  - number of generations
  - animation speed (FPS)
  - cell size
- Large view window suitable for complex patterns like the **Gosper Glider Gun**
- Deployed and accessible directly in the browser (no local setup required)

---

## 🛠️ Technical Overview

- **Core logic** implemented in Python using a clean model–view separation:
  - `LifeGrid` handles evolution rules
  - patterns loaded from a TOML data file
- **Rendering** done using HTML + CSS inside Streamlit for color support
- Animation achieved via incremental updates and frame timing
- UI built entirely with Streamlit widgets (sliders, dropdowns, buttons)

---

## 📚 Credits & Attribution

This project was inspired by and initially learned from the following excellent tutorial:

> **Real Python — Conway’s Game of Life in Python**  
> https://realpython.com/conway-game-of-life-python/

I used the Real Python article and its accompanying repository as a **learning reference** to understand:
- the Game of Life rules,
- clean Python implementation patterns,
- basic grid evolution logic.

### My original contributions include:
- Porting the project from a terminal-based implementation to a **Streamlit web application**
- Implementing **cell age tracking**
- Adding **color-coded visualization based on cell age**
- Designing an interactive UI with sliders and pattern selection
- Handling large patterns via adjustable view windows
- Deploying the app publicly for interactive exploration

All extensions, UI design, and deployment were implemented independently.

---

## 🚀 Running Locally (Optional)

```bash
pip install -r requirements.txt
streamlit run app.py
