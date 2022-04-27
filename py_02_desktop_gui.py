import pywinauto
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import keyboard as kb

app = Application().start("Notepad")
window = app.Notepad
window.wait("ready")
time.sleep(2)
# window.maximize()
time.sleep(2)
window.menu_item(u'&Ajuda->&Sobre Bloco de Notas').click()
app.Dialog.OKButton.click()
time.sleep(2)
window[u'Edit'].type_keys("Automate with Python")
#
window.menu_item("&Editar->Selecionar tudo")
#
app.Font[u'ComboBox0'].select(u'Fira Code')
app.Font[u'ComboBox1'].select(u'Oblíquo e negrito')
app.Font[u'ComboBox2'].select(u'24')
time.sleep(3)
