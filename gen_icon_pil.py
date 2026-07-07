
from PIL import Image, ImageDraw

def create_icon_pil(size, filename):
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background Circle (Indigo)
    draw.ellipse([0, 0, size, size], fill="#4F46E5")
    
    # Shield (White) - Approximated closely
    margin = size * 0.25
    center = size / 2
    bottom = size - margin
    
    # Shield shape points
    # Top Left, Top Right, Bottom Center (Curve control?)
    # Simple Triangle + Rectangle combo for robustness
    
    # Draw simple "H" for HLCA
    font_size = size // 2
    # Since we don't know font paths, draw lines
    
    w = size * 0.1
    h = size * 0.4
    x = size * 0.35
    y = size * 0.3
    
    # Left bar
    draw.rectangle([x, y, x+w, y+h], fill="white")
    # Right bar
    draw.rectangle([x+w*3, y, x+w*4, y+h], fill="white")
    # Cross bar
    draw.rectangle([x, y+h/2-w/2, x+w*4, y+h/2+w/2], fill="white")
    
    img.save(filename)
    print(f"Created {filename}")

if __name__ == "__main__":
    try:
        create_icon_pil(16, "extension/icon16.png")
        create_icon_48 = create_icon_pil(48, "extension/icon48.png")
        create_icon_128 = create_icon_pil(128, "extension/icon128.png")
    except Exception as e:
        print(f"Error: {e}")
