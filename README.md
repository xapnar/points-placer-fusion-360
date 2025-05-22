# Fusion 360 points placer

### **🧠 How It Works**
	1.	Connects to the currently active Fusion 360 document.
	2.	Adds a new sketch on the XY construction plane.
	3.	Takes your list of 2D points — formatted like [(x1, y1), (x2, y2), ...] — and:
	4.	Converts each to a 3D point with z = 0.
	5.  Draws lines between consecutive points in the list.

### **✍️ How To Use**
	1.	Open Fusion 360.
	2.	Go to Scripts and Add-Ins > Add-Ins tab.
	3.	Load this script (you can just paste it in a .py file).
	4.	Replace the points list in the script with your own:
```
points = [
    (0, 0),
    (1, 1),
    (2, 0),
    (3, 1)
]
```
  5. Click Run. Boom 💥 — you’ve got lines!

### **🛠️ Gotchas**
	•	Z is always zero. This only works for **2D sketches** on the XY plane.
	•	This doesn’t close the shape. If you want to go full circle, manually add the last point to match the first one.
	•	Doesn’t check for duplicate points or handle 3D paths. This is quick and dirty. Like ramen noodles but for CAD.

if you have any problems contact with me at emirlan@parpiev.org
