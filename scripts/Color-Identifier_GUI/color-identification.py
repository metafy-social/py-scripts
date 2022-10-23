import cv2
import pandas as pd
import os
import PySimpleGUI as Sg


def get_color(R, G, B):
    """ Function to calculate minimum distance from all colors and get the most matching color"""
    mini = 766
    name = ''
    for i in range(len(csv)):
        current_color = csv.loc[i]  # Get current row
        # Finding the absolute difference between color given and current color in image
        diff = abs(R - int(current_color["hex"][:2], 16)) + abs(G - int(current_color["hex"][2:4], 16)) + abs(
            B - int(current_color["hex"][4:], 16))
        if diff <= mini:
            mini = diff
            name = current_color["color"]
    return name


# Reading the csv file for colors name
csv = pd.read_csv('colors.csv')
current_path = os.getcwd()
a_id = img = None
Sg.theme("cdc")  # Wrong name so to get random theme
layout = [[Sg.In(default_text=current_path, size=(66, 60)),
           Sg.FileBrowse(initial_folder=current_path, enable_events=True), Sg.Button('Open')],
          [Sg.Graph((600, 400), (0, 400), (600, 0), key='image', enable_events=True, drag_submits=True)],
          [Sg.Graph((200, 40), (0, 40), (200, 0), background_color='#000000', key='color'),
           Sg.Text('#000000', key='hex', size=(10, 1), auto_size_text=True, font=('', 27))],
          [Sg.Text('BLACK', key='color_name', size=(20, 1), auto_size_text=True, font=('', 27))]]
window = Sg.Window("Color Identifier", layout, finalize=True)
# Different elements of windows, so that we don't have to search again and again
image, color, hex_code, color_name = window['image'], window['color'], window['hex'], window['color_name']

while True:
    event, values = window.read()

    if event == Sg.WIN_CLOSED:
        break

    elif event == 'Open':
        # If last extension is not an image extension, show popup
        if values[0].split('.')[-1] not in ['jpg', 'jpeg', 'png']:
            Sg.PopupError("Open image files only!! (JPG, JPEG, PNG)")
            continue
        # Path of image from browse
        img_path = values[0]
        img = cv2.resize(cv2.imread(img_path), (600, 400), interpolation=cv2.INTER_AREA)  # Resize the image
        if a_id is not None:
            image.delete_figure(a_id)  # Delete previous image
        a_id = image.draw_image(data=cv2.imencode('.ppm', img)[1].tobytes(), location=(0, 0))  # Draw new image
        image.send_figure_to_back(a_id)

    elif event == 'image':
        # If there is no image, continue
        if img is None:
            continue
        x, y = values['image']  # Get coordinates of cursor
        try:
            b, g, r = map(int, img[y, x])  # Get color from image on that coordinates
        except IndexError:  # If the coordinates are out of bounds
            continue
        # Updating the elements of GUI
        color.update(background_color="#{:02X}{:02X}{:02X}".format(r, g, b))
        hex_code.update("#{:02X}{:02X}{:02X}".format(r, g, b))
        color_name.update(get_color(r, g, b))

window.close()
