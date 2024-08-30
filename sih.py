import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

def draw_flowchart():
    fig, ax = plt.subplots(figsize=(10, 12))

    # Function to draw a box
    def draw_box(text, xy, width=0.6, height=0.1):
        box = FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.1", edgecolor="black", facecolor="lightgrey")
        ax.add_patch(box)
        ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha='center', va='center', fontsize=10)

    # Function to draw arrows
    def draw_arrow(start, end):
        ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color="black"))

    # Start
    draw_box("Start", (0.4, 0.95))

    # User Visits Website
    draw_box("User Visits Website", (0.4, 0.85))
    draw_arrow((0.5, 0.95), (0.5, 0.85))

    # Is User Logged In? Decision Box
    draw_box("Is User Logged In?", (0.4, 0.75), width=0.8, height=0.1)
    draw_arrow((0.5, 0.85), (0.5, 0.75))

    # Yes and No paths
    draw_box("Access Personalized Content", (0.1, 0.65), width=0.6)
    draw_arrow((0.4, 0.75), (0.4, 0.65))
    draw_box("Prompt Login/Signup", (0.7, 0.65), width=0.6)
    draw_arrow((0.6, 0.75), (0.7, 0.65))

    # Continue to "User Interacts with Different Plants/Herbs"
    draw_box("User Interacts with\nDifferent Plants/Herbs", (0.4, 0.55), height=0.15)
    draw_arrow((0.4, 0.65), (0.4, 0.55))
    draw_arrow((0.8, 0.65), (0.6, 0.55))

    # View Plant Details? Decision Box
    draw_box("View Plant Details?", (0.4, 0.4), width=0.6)
    draw_arrow((0.5, 0.55), (0.5, 0.4))

    # Yes and No paths
    draw_box("View 3D Models/Videos/\nAudio Clips, Gather Comprehensive\nInformation", (0.1, 0.3), width=0.6, height=0.15)
    draw_arrow((0.4, 0.4), (0.4, 0.3))
    draw_box("Explore Medicinal Plants", (0.7, 0.3), width=0.6)
    draw_arrow((0.6, 0.4), (0.7, 0.3))

    # Filter/Sort Plants?
    draw_box("Filter/Sort Plants?", (0.4, 0.2), width=0.6)
    draw_arrow((0.5, 0.3), (0.5, 0.2))

    # Yes and No paths
    draw_box("Apply Filters/Sort Criteria", (0.1, 0.1), width=0.6)
    draw_arrow((0.4, 0.2), (0.4, 0.1))
    draw_box("Search/Filter Plants", (0.7, 0.1), width=0.6)
    draw_arrow((0.6, 0.2), (0.7, 0.1))

    # Final steps
    draw_box("Bookmark/Share?", (0.4, 0.0), width=0.6)
    draw_arrow((0.5, 0.1), (0.5, 0.0))

    draw_box("Exit", (0.4, -0.1))
    draw_arrow((0.5, 0.0), (0.5, -0.1))

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.2, 1)
    ax.axis('off')
    plt.show()

draw_flowchart()
