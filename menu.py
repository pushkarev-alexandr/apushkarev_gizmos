import nuke # type: ignore
import os

menu = nuke.menu('Nodes').addMenu('apushkarev', icon='apushkarev.png')

cur_dir = os.path.dirname(__file__).replace("\\","/")
for folder_name in os.listdir(cur_dir):
    folder = f"{cur_dir}/{folder_name}"
    if os.path.isdir(folder) and folder_name[0] not in [".","_"]:
        for file in os.listdir(folder):
            spl = os.path.splitext(file)
            if spl[1] in [".gizmo", ".nk"]:
                menu.addCommand(f"{folder_name}/{spl[0]}",
                                f"nuke.{'createNode' if spl[1]=='.gizmo' else 'nodePaste'}('{folder}/{file}')")
