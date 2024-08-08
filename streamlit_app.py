import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image

# Constants
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 50
UNICORN_START_X = 10
UNICORN_START_Y = 20
HEART_SPAWN_CHANCE = 0.1
ANIMATION_INTERVAL = 0.1

# Colors
COLORS = ['pink', 'red', 'blue', 'green', 'yellow', 'orange']

def draw_unicorn(ax, x, y):
    """
    Draw a unicorn on the given axes at the specified position.
    
    :param ax: Matplotlib axes
    :param x: x-coordinate of the unicorn's position
    :param y: y-coordinate of the unicorn's position
    """
    # Body
    ax.add_patch(patches.Rectangle((x, y), 30, 15, edgecolor='black', facecolor='white'))
    # Legs
    ax.add_patch(patches.Rectangle((x+5, y-7), 2, 7, edgecolor='black', facecolor='white'))
    ax.add_patch(patches.Rectangle((x+23, y-7), 2, 7, edgecolor='black', facecolor='white'))
    # Head
    ax.add_patch(patches.Rectangle((x+25, y+5), 10, 10, edgecolor='black', facecolor='white'))
    # Horn
    ax.add_patch(patches.Polygon([[x+30, y+15], [x+35, y+12.5], [x+37.5, y+20]], edgecolor='black', facecolor='yellow'))
    # Eye
    ax.add_patch(patches.Circle((x+27, y+12), 1, edgecolor='black', facecolor='white'))
    ax.add_patch(patches.Circle((x+27, y+12), 0.5, edgecolor='black', facecolor='black'))
    # Smile
    ax.add_patch(patches.Arc((x+28, y+7), 2, 2, angle=180, theta1=0, theta2=180, edgecolor='black'))

def draw_heart(ax, x, y, color):
    """
    Draw a heart on the given axes at the specified position.
    
    :param ax: Matplotlib axes
    :param x: x-coordinate of the heart's position
    :param y: y-coordinate of the heart's position
    :param color: Color of the heart
    """
    ax.add_patch(patches.Circle((x - 1.6, y + 2), 3, edgecolor=color, facecolor=color))
    ax.add_patch(patches.Circle((x + 1.6, y + 2), 3, edgecolor=color, facecolor=color))
    ax.add_patch(patches.Polygon([[x - 5, y + 2], [x + 5, y + 2], [x, y - 5]], edgecolor=color, facecolor=color))

@st.cache_resource
def setup_figure():
    """
    Set up and return the Matplotlib figure and axes.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, CANVAS_WIDTH)
    ax.set_ylim(0, CANVAS_HEIGHT)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax

def update_animation(fig, ax, unicorn_pos, sweethearts):
    """
    Update the animation frame.
    
    :param fig: Matplotlib figure
    :param ax: Matplotlib axes
    :param unicorn_pos: Current position of the unicorn
    :param sweethearts: List of sweetheart positions and colors
    :return: Updated sweethearts list and PIL Image of the current frame
    """
    ax.clear()
    ax.set_xlim(0, CANVAS_WIDTH)
    ax.set_ylim(0, CANVAS_HEIGHT)
    ax.set_aspect('equal')
    ax.axis('off')

    draw_unicorn(ax, unicorn_pos[0], unicorn_pos[1])

    if np.random.rand() > 1 - HEART_SPAWN_CHANCE:
        color = np.random.choice(COLORS)
        sweethearts.append([unicorn_pos[0] + 35, unicorn_pos[1] + 7, color])

    for heart in sweethearts:
        heart[0] += 1
        draw_heart(ax, heart[0], heart[1], heart[2])

    sweethearts = [heart for heart in sweethearts if heart[0] < CANVAS_WIDTH]

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    image = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    
    return sweethearts, image

def main():
    st.title("💻 Here's one I made earlier! 🌈")
    st.write("")
    st.write("Select one of Jamie's apps:")

    apps = {
        "Machine Learning": "https://blochai-machinelearning.streamlit.app/",
        "Process Mining": "https://blochai-processmining.streamlit.app/",
        "Large Language Model": "https://blochai-largelanguagemodel.streamlit.app/",
    }
    for app_name, app_url in apps.items():
        st.markdown(f"[{app_name}]({app_url})")
    st.write("")

    fig, ax = setup_figure()

    if 'unicorn_pos' not in st.session_state:
        st.session_state.unicorn_pos = [UNICORN_START_X, UNICORN_START_Y]
    if 'sweethearts' not in st.session_state:
        st.session_state.sweethearts = []

    animation_placeholder = st.empty()

    while True:
        try:
            st.session_state.sweethearts, image = update_animation(
                fig, ax, st.session_state.unicorn_pos, st.session_state.sweethearts
            )
            animation_placeholder.image(image)
            time.sleep(ANIMATION_INTERVAL)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            break

    add_footer()

def add_footer():
    st.markdown(
        '''
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: black !important;
            color: white !important;
            text-align: center;
            padding: 10px 0;
        }
        .footer p {
            color: white !important;
            margin: 0;
        }
        .footer a {
            color: white !important;
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            <p>© 2024 Bloch AI LTD - All Rights Reserved. <a href="https://www.bloch.ai">www.bloch.ai</a></p>
        </div>
        ''',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
