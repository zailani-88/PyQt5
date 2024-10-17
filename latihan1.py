import PySimpleGUI as sg
sg.theme("BlueMono")
layout = [
    [sg.Text("NPM      : 2210010451")],
    [sg.Text("Nama     : Ahmad Zailani")],
    [sg.Text("Kelas    : 5O Reguler Banjarmasin")],
    [sg.Text("Matkul   : Pemrograman Visual 3")]
]

window = sg.Window("Latihan Python", layout, size=(400, 200))
window()
window.close()