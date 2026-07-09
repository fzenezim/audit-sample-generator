import customtkinter as ctk
import random
from tkinter import messagebox
import traceback
import sys
import pyautogui
from datetime import datetime
from PIL import Image
import ctypes

try:
    # CORREÇÃO DO PRINT PRETO: Torna o app consciente de DPI no Windows
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass # Ignora se não for Windows

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    class AuditSampleApp(ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("Audit Sample Generator - v1.4")
            self.geometry("550x700")

            self.box_principal = ctk.CTkFrame(self, corner_radius=15)
            self.box_principal.pack(padx=20, pady=20, fill="both", expand=True)

            self.txt_titulo = ctk.CTkLabel(
                self.box_principal, 
                text="Gerador de Amostras de Auditoria", 
                font=ctk.CTkFont(size=20, weight="bold")
            )
            self.txt_titulo.pack(pady=(20, 20))

            self.box_entradas = ctk.CTkFrame(self.box_principal, fg_color="transparent")
            self.box_entradas.pack(padx=20, pady=10, fill="x")

            self.lbl_univ = ctk.CTkLabel(self.box_entradas, text="Tamanho do Universo:")
            self.lbl_univ.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            self.ent_univ = ctk.CTkEntry(self.box_entradas, placeholder_text="Ex: 100")
            self.ent_univ.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

            self.lbl_size = ctk.CTkLabel(self.box_entradas, text="Tamanho da Amostra:")
            self.lbl_size.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            self.ent_size = ctk.CTkEntry(self.box_entradas, placeholder_text="Ex: 25")
            self.ent_size.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

            self.lbl_seed = ctk.CTkLabel(self.box_entradas, text="Seed (Semente):")
            self.lbl_seed.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            
            self.seed_container = ctk.CTkFrame(self.box_entradas, fg_color="transparent")
            self.seed_container.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
            self.seed_container.grid_columnconfigure(0, weight=1)

            self.ent_seed = ctk.CTkEntry(self.seed_container, placeholder_text="Ex: 1 a 99999 (opcional)")
            self.ent_seed.grid(row=0, column=0, padx=(0, 10), sticky="ew")

            self.btn_rand_seed = ctk.CTkButton(
                self.seed_container, 
                text="🎲", 
                width=40,
                command=self.acao_seed_aleatoria
            )
            self.btn_rand_seed.grid(row=0, column=1)

            self.btn_gerar = ctk.CTkButton(
                self.box_principal, 
                text="Gerar Amostra", 
                command=self.acao_gerar,
                font=ctk.CTkFont(weight="bold")
            )
            self.btn_gerar.pack(pady=20)

            self.lbl_res = ctk.CTkLabel(self.box_principal, text="Resultado (Sorteio - Item):")
            self.lbl_res.pack(padx=20, pady=(10, 0), anchor="w")
            
            # CORREÇÃO DA RESPONSIVIDADE: fill="both" e expand=True
            self.txt_res = ctk.CTkTextbox(self.box_principal)
            self.txt_res.pack(padx=20, pady=10, fill="both", expand=True)

            self.box_acoes = ctk.CTkFrame(self.box_principal, fg_color="transparent")
            self.box_acoes.pack(pady=(0, 20))

            self.btn_copiar = ctk.CTkButton(
                self.box_acoes, 
                text="Copiar Resultado", 
                command=self.acao_copiar,
                fg_color="#1e293b", 
                hover_color="#334155"
            )
            self.btn_copiar.pack(side="left", padx=10)

            self.btn_salvar = ctk.CTkButton(
                self.box_acoes, 
                text="📸 Salvar Evidência", 
                command=self.acao_salvar_print,
                fg_color="#059669", 
                hover_color="#10b981"
            )
            self.btn_salvar.pack(side="left", padx=10)

            self.box_entradas.grid_columnconfigure(1, weight=1)

        def acao_seed_aleatoria(self):
            random_seed = str(random.randint(1, 999999))
            self.ent_seed.delete(0, "end")
            self.ent_seed.insert(0, random_seed)

        def acao_gerar(self):
            try:
                u_size = int(self.ent_univ.get())
                s_size = int(self.ent_size.get())
                s_val = self.ent_seed.get().strip()
                
                if u_size <= 0 or s_size <= 0:
                    messagebox.showwarning("Aviso", "Os tamanhos devem ser números positivos.")
                    return
                if s_size > u_size:
                    messagebox.showwarning("Aviso", f"A amostra ({s_size}) não pode ser maior que o universo ({u_size}).")
                    return
                
                if s_val:
                    random.seed(s_val)
                else:
                    random.seed()

                amostra = random.sample(range(1, u_size + 1), s_size)
                amostra.sort()
                linhas = []
                for i, item_num in enumerate(amostra, 1):
                    linhas.append(f"{i} - item {item_num}")
                texto_final = "\n".join(linhas)
                self.txt_res.delete("1.0", "end")
                self.txt_res.insert("1.0", texto_final)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

        def acao_copiar(self):
            self.clipboard_clear()
            self.clipboard_append(self.txt_res.get("1.0", "end-1c"))
            messagebox.showinfo("Sucesso", "Resultado copiado para a área de transferência!")

        def acao_salvar_print(self):
            try:
                x = self.winfo_rootx()
                y = self.winfo_rooty()
                w = self.winfo_width()
                h = self.winfo_height()
                
                screenshot = pyautogui.screenshot(region=(x, y, w, h))
                
                agora = datetime.now()
                data_str = agora.strftime("%Y-%m-%d_%H-%M-%S")
                seed_val = self.ent_seed.get().strip() or "S_ALEATORIA"
                nome_arquivo = f"{data_str}_{seed_val}.png"
                
                screenshot.save(nome_arquivo)
                messagebox.showinfo("Evidência Salva", f"Print salvo com sucesso como:\n{nome_arquivo}")
            except Exception as e:
                messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar a imagem:\n{e}")

    if __name__ == "__main__":
        app = AuditSampleApp()
        app.mainloop()

except Exception as e:
    with open("erro_log.txt", "w") as f:
        f.write("Erro crítico detectou ao abrir o app:\n")
        f.write(traceback.format_exc())
