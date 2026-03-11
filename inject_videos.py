
import os

memorylane_path = "/home/devloper/Desktop/Birthday/memorylane.html"
videos = ["important/200.mp4", "important/3 (2).mp4"]

with open(memorylane_path, 'r') as f:
    lines = f.readlines()

new_lines = []
in_memories = False

for line in lines:
    if "const memories = [" in line:
        in_memories = True
        new_lines.append(line)
        # Add videos at the beginning
        for i, vid in enumerate(videos):
            new_lines.append(f"""  {{
    "img": "{vid}",
    "title": "Special Moment {i+1}",
    "desc": "A precious memory in motion. 🎥",
    "quote": "Every moment with you is magic.",
    "type": "video"
  }},
""")
        continue
    
    if "];" in line and in_memories:
        in_memories = False
        new_lines.append(line)
        continue

    new_lines.append(line)

with open(memorylane_path, 'w') as f:
    f.writelines(new_lines)

print("memorylane.html updated with videos.")
