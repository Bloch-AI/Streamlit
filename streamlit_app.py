import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Function to draw a unicorn
def draw_unicorn(ax, x, y):
    # Body
    ax.add_patch(patches.Rectangle((x, y), 20, 10, edgecolor='black', facecolor='purple'))
    # Legs
    ax.add_patch(patches.Rectangle((x+2, y-5), 2, 5, edgecolor='black', facecolor='purple'))
    ax.add_patch(patches.Rectangle((x+16, y-5), 2, 5, edgecolor='black', facecolor='purple'))
    # Head
    ax.add_patch(patches.Rectangle((x+18, y+4), 6, 6, edgecolor='black', facecolor='purple'))
    # Horn
    ax.add_patch(patches.Polygon([[x+24, y+10], [x+27, y+10], [x+25.5, y+14]], edgecolor='black', facecolor='yellow'))

# Function to draw a sweetheart
def draw_sweetheart(ax, x, y):
    ax.add_patch(patches.Circle((x, y), 3, edgecolor='red', facecolor='pink'))

# Initialize positions
unicorn_pos = [50, 50]
sweethearts = []

# Main Streamlit app
st.title("💻 Here's one I made earlier! 🌈")
st.write("")
st.write("Select one of Jamie's apps:")

# List of other Streamlit apps with their URLs
apps = {
    "Machine Learning": "https://blochai-machinelearning.streamlit.app/",
    "Process Mining": "https://blochai-processmining.streamlit.app/",
}

for app_name, app_url in apps.items():
    st.markdown(f"[{app_name}]({app_url})")

st.write("")

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.axis('off')

# Initialize animation
animation_placeholder = st.empty()

# Animation loop
for frame in range(200):  # Run the animation for 200 frames
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw the unicorn
    draw_unicorn(ax, unicorn_pos[0], unicorn_pos[1])

    # Add new sweetheart
    if np.random.rand() > 0.9:
        sweethearts.append([unicorn_pos[0] + 25, unicorn_pos[1] + 7])

    # Move sweethearts
    for heart in sweethearts:
        heart[0] += 1

    # Draw sweethearts
    for heart in sweethearts:
        draw_sweetheart(ax, heart[0], heart[1])

    # Remove sweethearts that are off-screen
    sweethearts = [heart for heart in sweethearts if heart[0] < 100]

    # Render the figure to a PIL image
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    image = Image.fromarray(image)

    # Display the image in Streamlit
    animation_placeholder.image(image)

    time.sleep(0.1)

# Add footer
st.markdown('<div class="footer"><p>© 2024 Bloch AI LTD - All Rights Reserved. <a href="https://www.bloch.ai" style="color: black;">www.bloch.ai</a></p></div>', unsafe_allow_html=True)
