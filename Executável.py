import customtkinter as ctk
import random
from tkinter import messagebox
import traceback
import sys

try:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    class AuditSampleApp(ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("Audit Sample Generator - v1.1")
            self.geometry("500x600")

            self.main_frame = ctk.CTkFrame(self, corner_radius=15)
            self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

            self.title_label = ctk.CTkLabel(
                self.main_frame, 
                text="Gerador de Amostras de Auditoria", 
                font=ctk.CTkFont(size=20, weight="bold")
            )
            self.title_label.pack(pady=(20, 20))

            self.input_frame = ctk.CTkFrame(self.main_//_frame, fg_color="transparent") # ERRO NOVAMENTE!
