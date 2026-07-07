
from reportlab.graphics.shapes import Drawing, Rect, Path, Group
from reportlab.graphics import renderPM
from reportlab.lib import colors

def create_icon(size, filename):
    d = Drawing(size, size)
    
    # Background (Blue/Purple Gradient simulation using simple shapes or solid)
    # ReportLab gradients are complex, let's stick to a solid nice color
    d.add(Rect(0, 0, size, size, fillColor=colors.HexColor("#4F46E5"), strokeColor=None, rx=size*0.2, ry=size*0.2))
    
    # Shield Path scale factor
    s = size / 24.0 # Base on 24x24 grid
    
    # White Shield
    # Path d="M12 2L3 7v9c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"
    # Centered: Translate(0,0) -> Scale(s,s)
    
    shield_path = f"M{12*s} {4*s} L{4*s} {8*s} V{16*s} C{4*s} {21*s} {8*s} {25*s} {12*s} {27*s} C{16*s} {25*s} {20*s} {21*s} {20*s} {16*s} V{8*s} L{12*s} {4*s} Z"
    
    d.add(Path(d=shield_path, fillColor=colors.white, strokeColor=None))
    
    # Lock inside (Blue)
    # Simple Rect + Circle arc? Or just a keyhole.
    # Let's simple keyhole: Circle + Trapeze
    
    renderPM.drawToFile(d, filename, fmt='PNG')
    print(f"Created {filename}")

if __name__ == "__main__":
    try:
        create_icon(16, "extension/icon16.png")
        create_icon(48, "extension/icon48.png")
        create_icon(128, "extension/icon128.png")
    except Exception as e:
        print(f"Error: {e}")
