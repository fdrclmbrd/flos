import subprocess
import json

user_home_path = subprocess.getoutput("echo $HOME")

clients_properties = json.loads(subprocess.getoutput("hyprctl -j clients"))

current_file_index = 0

created_files = list()

for client_properties in clients_properties:

    client_workspace = client_properties["workspace"]["name"]
    
    if client_workspace != "":

        client_class = client_properties["class"]

        client_title = client_properties["title"]

        client_description = F"{client_workspace} {client_class} {client_title}\n"

        client_address = client_properties["address"]

        open_window_file_content = F"[Desktop Entry]\nType=Application\nName={client_workspace}\nComment={client_workspace}  {client_class.split('.')[-1].title()}  {client_title}\nIcon={client_class}\nExec=sh -c 'hyprctl dispatch workspace {client_workspace} && hyprctl dispatch focuswindow {client_address}'\nTerminal=false\nCategories=OpenWindow"
        
        open_window_file_full_path = F"{user_home_path}/.local/share/applications/openwindow_{current_file_index}.desktop"

        open_window_file = open(open_window_file_full_path, "w")

        open_window_file.writelines(open_window_file_content)

        open_window_file.close()

        created_files.append(open_window_file_full_path)

        current_file_index += 1

subprocess.Popen(F"rofi -show drun -config /home/fl/.config/rofi/window_switcher.rasi", shell=True).wait()

for file in created_files:
    
    subprocess.Popen(F"rm {file}", shell=True)
