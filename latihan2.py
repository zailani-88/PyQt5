import PySimpleGUI as sg
sg.theme("#00FFFF")
sg.theme_text_color("#0000FF")

layout = [
    [sg.Text("Mengubah font,teks dan begron",text_color="green",font=("Arial,25"))],
    [sg.Text("NPM      : 2210010451")],
    [sg.Text("Nama     : Ahmad Zailani")],
    [sg.Text("Kelas    : 5O Reguler Banjarmasin")],
    [sg.Text("Matkul   : Pemrograman Visual 3")]
]

window = sg.Window("Latihan Python", layout, size=(400, 200))
window()
window.close()