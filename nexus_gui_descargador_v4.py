
import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser

# Diccionario de resoluciones y sus IDs
resoluciones = {
    "SD (480p o menos)": ["278", "602", "603", "160", "269", "242", "604", "133", "229", "243", "605", "134", "230", "244", "606", "135", "231"],
    "HD (720p)": ["247", "609", "136", "232"],
    "Full HD (1080p)": ["248", "614", "137", "270", "616"],
    "2K (1440p)": ["271", "620", "400"],
    "4K (2160p)": ["313", "625", "401"]
}

REQUIRED_EXECUTABLES = {
    "yt-dlp.exe": "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe",
    "ffmpeg.exe": "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",
    "ffprobe.exe": "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
}

def verificar_dependencias():
    faltantes = []
    for exe, url in REQUIRED_EXECUTABLES.items():
        if not os.path.isfile(exe):
            faltantes.append((exe, url))
    
    if faltantes:
        mensaje = "⚠️ Faltan los siguientes archivos necesarios:\n\n"
        for exe, url in faltantes:
            mensaje += f"- {exe}\n  Descarga: {url}\n"
        mensaje += "\n¿Deseas abrir las páginas de descarga ahora?"
        if messagebox.askyesno("Dependencias faltantes", mensaje):
            for _, url in faltantes:
                webbrowser.open(url)
        return False
    return True

def abrir_carpeta(path):
    try:
        if os.name == 'nt':
            os.startfile(path)
        elif os.name == 'posix':
            subprocess.Popen(['xdg-open', path])
    except Exception as e:
        print(f"Error al abrir la carpeta: {e}")

def descargar():
    if not verificar_dependencias():
        return

    url = entry_url.get().strip()
    calidad = combo_calidad.get()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor, ingresa la URL del video.")
        return
    if calidad not in resoluciones:
        messagebox.showwarning("Advertencia", "Selecciona una calidad válida.")
        return

    ids_video = resoluciones[calidad]
    for formato_id in ids_video:
        label_estado.config(text=f"Probando con {formato_id}+bestaudio...")
        ventana.update_idletasks()
        comando = [
            "yt-dlp",
            "-f", f"{formato_id}+bestaudio",
            "--embed-thumbnail",
            "--embed-subs",
            "--recode", "mp4",
            "--write-thumbnail",
            "--write-sub",
            "--sub-lang", "es,en",
            "--output", "MP4/%(title)s.%(ext)s",
            url
        ]
        resultado = subprocess.run(comando)
        if resultado.returncode == 0:
            label_estado.config(text="✅ Descarga completada.")
            abrir_carpeta("MP4")
            return
    label_estado.config(text="❌ No se pudo descargar el video.")

def abrir_paypal():
    webbrowser.open("https://paypal.me/eidosred?country.x=HN&locale.x=es_XC")

# Crear solo la carpeta de salida necesaria
os.makedirs("MP4", exist_ok=True)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Nexus Downloader v4")
ventana.geometry("520x400")
ventana.resizable(False, False)

if os.path.exists("logo.png"):
    try:
        logo_img = Image.open("logo.png").resize((180, 90))
        logo_photo = ImageTk.PhotoImage(logo_img)
        tk.Label(ventana, image=logo_photo).pack(pady=10)
    except Exception as e:
        print("Error al cargar el logo:", e)

tk.Label(ventana, text="Ingresa la URL del video:").pack()
entry_url = tk.Entry(ventana, width=60)
entry_url.pack()

tk.Label(ventana, text="Selecciona la calidad de video:").pack(pady=10)
combo_calidad = ttk.Combobox(ventana, values=list(resoluciones.keys()), state="readonly")
combo_calidad.set("HD (720p)")
combo_calidad.pack()

tk.Button(ventana, text="Descargar Video", command=descargar).pack(pady=15)
label_estado = tk.Label(ventana, text="")
label_estado.pack()

tk.Button(ventana, text="💖 Donar vía PayPal", command=abrir_paypal).pack(pady=10)

ventana.mainloop()
