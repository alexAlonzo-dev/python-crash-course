import tkinter as uk
import pyautogui
import threading
import time
import sys
import random
import keyboard  # Nueva librería para la tecla de escape

# Configuración
TIEMPO_ESPERA = 10  # Segundos para colocar el mouse
TECLA_SALIDA = 'q'  # Presiona esta tecla para detener todo

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitch Clicker")
        self.root.geometry("300x130+10+10") 
        self.root.attributes('-topmost', True)
        self.root.configure(bg='#18181b')

        self.running = True
        self.is_clicking = False
        self.click_count = 0

        # UI Elements
        self.lbl_status = uk.Label(root, text=f"Iniciando en: {TIEMPO_ESPERA}s", 
                                   font=("Arial", 14, "bold"), fg="#efeff1", bg='#18181b')
        self.lbl_status.pack(pady=10)

        self.lbl_clicks = uk.Label(root, text="Clics: 0", 
                                   font=("Arial", 12), fg="#a970ff", bg='#18181b')
        self.lbl_clicks.pack(pady=5)

        # Instrucción de salida
        self.lbl_info = uk.Label(root, text=f"Mantén presionado '{TECLA_SALIDA.upper()}' para parar", 
                                 font=("Arial", 10, "bold"), fg="#ff4f4d", bg='#18181b')
        self.lbl_info.pack(pady=5)

        self.thread = threading.Thread(target=self.start_process)
        self.thread.daemon = True
        self.thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_process(self):
        # Cuenta regresiva
        for i in range(TIEMPO_ESPERA, 0, -1):
            if not self.running or keyboard.is_pressed(TECLA_SALIDA): 
                self.on_close()
                return
            self.update_label(self.lbl_status, f"¡Coloca el mouse! {i}s")
            time.sleep(1)

        # Inicio de clics
        self.is_clicking = True
        self.update_label(self.lbl_status, "¡CLICKING ACTIVO!", "#00ff7f")
        
        # Guardamos posición
        target_x, target_y = pyautogui.position()
        
        while self.running:
            # 1. VERIFICAR SI SE PRESIONÓ LA TECLA DE SALIDA
            if keyboard.is_pressed(TECLA_SALIDA):
                self.update_label(self.lbl_status, "DETENIDO POR USUARIO", "yellow")
                time.sleep(1) # Pausa breve para leer el mensaje
                self.on_close()
                break

            # 2. Hacer Clic
            pyautogui.click(x=target_x, y=target_y)
            self.click_count += 1
            
            if self.click_count % 5 == 0: # Actualizar GUI cada 5 clics
                self.update_label(self.lbl_clicks, f"Clics: {self.click_count}")

            # 3. ANTI-BAN: Intervalo aleatorio (Humanización)
            # Espera un tiempo aleatorio entre 0.01 y 0.08 segundos
            time.sleep(random.uniform(0.01, 0.08))

    def update_label(self, label, text, color=None):
        try:
            label.config(text=text)
            if color:
                label.config(fg=color)
        except:
            pass

    def on_close(self):
        self.running = False
        try:
            self.root.destroy()
        except:
            pass
        sys.exit()

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    root = uk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()