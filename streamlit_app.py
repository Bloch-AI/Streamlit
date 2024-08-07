import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Function to draw a unicorn
def draw_unicorn(ax, x, y):
    # Body
    ax.add_patch(patches.Rectangle((x, y), 30, 15, edgecolor='black', facecolor='purple'))
    # Legs
    ax.add_patch(patches.Rectangle((x+5, y-7), 2, 7, edgecolor='black', facecolor='purple'))
    ax.add_patch(patches.Rectangle((x+23, y-7), 2, 7, edgecolor='black', facecolor='purple'))
    # Head
    ax.add_patch(patches.Rectangle((x+25, y+5), 10, 10, edgecolor='black', facecolor='purple'))
    # Horn
    ax.add_patch(patches.Polygon([[x+30, y+15], [x+35, y+12.5], [x+37.5, y+20]], edgecolor='black', facecolor='yellow'))
    # Eye
    ax.add_patch(patches.Circle((x+27, y+12), 1, edgecolor='black', facecolor='white'))
    ax.add_patch(patches.Circle((x+27, y+12), 0.5, edgecolor='black', facecolor='black'))
    # Smile
    ax.add_patch(patches.Arc((x+28, y+7), 2, 2, angle=180, theta1=0, theta2=180, edgecolor='black'))

# Function to draw a heart
def draw_heart(ax, x, y, color):
    # Create a heart shape using two circles and a triangle
    ax.add_patch(patches.Circle((x - 2, y + 2), 3, edgecolor=color, facecolor=color))
    ax.add_patch(patches.Circle((x + 2, y + 2), 3, edgecolor=color, facecolor=color))
    ax.add_patch(patches.Polygon([[x - 5, y + 2], [x + 5, y + 2], [x, y - 5]], edgecolor=color, facecolor=color))

# Initialize positions
unicorn_pos = [10, 20]  # Adjusted the unicorn's y position down
sweethearts = []

# List of colors
colors = ['pink', 'red', 'blue', 'green', 'yellow', 'orange']

# Main Streamlit app
st.title("💻 Here's one I made earlier! 🌈")
st.write("")
st.write("Select one of Jamie's apps:")

# List of other Streamlit apps with their URLs
apps = {
    "Machine Learning": "https://blochai-machinelearning.streamlit.app/",
    "Process Mining": "https://blochai-processmining.streamlit.app/",
    "Large Language Model": "https://blochai-largelanguagemodel.streamlit.app/",
}

for app_name, app_url in apps.items():
    st.markdown(f"[{app_name}]({app_url})")

st.write("")

fig, ax = plt.subplots(figsize=(12, 6))  # Make the figure larger
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)  # Adjust the y-limit to fit the new aspect ratio
ax.set_aspect('equal')
ax.axis('off')

# Initialize animation
animation_placeholder = st.empty()

# Add footer
footer = st.container()
footer.markdown(
    '''
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: black;
        color: white;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    <div class="footer">
        <p>© 2024 Bloch AI LTD - All Rights Reserved. <a href="https://www.bloch.ai" style="color: white;">www.bloch.ai</a></p>
    </div>
    ''',
    unsafe_allow_html=True
)

# Animation loop
while True:  # Run the animation indefinitely
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)  # Adjust the y-limit to fit the new aspect ratio
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw the unicorn
    draw_unicorn(ax, unicorn_pos[0], unicorn_pos[1])

    # Add new sweetheart
    if np.random.rand() > 0.9:
        color = np.random.choice(colors)
        sweethearts.append([unicorn_pos[0] + 35, unicorn_pos[1] + 7, color])

    # Move sweethearts
    for heart in sweethearts:
        heart[0] += 1

    # Draw sweethearts
    for heart in sweethearts:
        draw_heart(ax, heart[0], heart[1], heart[2])

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
