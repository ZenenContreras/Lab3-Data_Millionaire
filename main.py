import tkinter as tk
from menu_principal import MenuPrincipal

def main():
    
    #Función principal que inicia la aplicación.
    
    root = tk.Tk()
    root.geometry("600x400")
    app = MenuPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    