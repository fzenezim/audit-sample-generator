import customtkinter as ctk
import random
from tkinter import messagebox
import traceback
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import ctypes

try:
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    class AuditSampleApp(ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("Audit Sample Generator - v2.0")
            self.geometry("600x750")
            self.minsize(500, 600)

            self.box_principal = ctk.CTkFrame(self, corner_radius=15)
            self.box_principal.pack(padx=40, pady=30, fill="both", expand=True)

            self.txt_titulo = ctk.CTkLabel(
                self.box_principal, 
                text="Gerador de Amostras de Auditoria", 
                font=ctk.CTkFont(size=22, weight="bold")
            )
            self.txt_titulo.pack(pady=(30, 20))

            self.box_entradas = ctk.CTkFrame(self.box_principal, fg_color="transparent")
            self.box_entradas.pack(padx=20, pady=10, fill="x")

            self.box_entradas.grid_columnconfigure(1, weight=1)

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
                font=ctk.CTkFont(size=15, weight="bold"),
                height=40
            )
            self.btn_gerar.pack(pady=30)

            self.lbl_res = ctk.CTkLabel(self.box_principal, text="Resultado (Sorteio - Item):")
            self.lbl_res.pack(padx=20, pady=(10, 0), anchor="w")
            
            self.txt_res = ctk.CTkTextbox(self.box_principal, font=ctk.CTkFont(family="Consolas", size=13))
            self.txt_res.pack(padx=20, pady=10, fill="both", expand=True)

            self.box_acoes = ctk.CTkFrame(self.box_principal, fg_color="transparent")
            self.box_acoes.pack(pady=(0, 30))

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
                command=self.acao_salvar_evidencia,
                fg_color="#059669", 
                hover_color="#10b981"
            )
            self.btn_salvar.pack(side="left", padx=10)

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

        def acao_salvar_evidencia(self):
            try:
                u_size = self.ent_univ.get()
                s_size = self.ent_size.get()
                seed_val = self.ent_seed.get().strip() or "S_ALEATORIA"
                resultados = self.txt_res.get("1.0", "end-1c").strip()
                
                if not resultados:
                    messagebox.showwarning("Aviso", "Gere uma amostra antes de salvar a evidência.")
                    return

                itens = resultados.split("\n")
                num_itens = len(itens)
                
                # CÁLCULO DE ALTURA DINÂMICA
                # Cabeçalho (~150px) + Itens (num * 22px) + Rodapé (~60px) + Margens
                altura_dinamica = 200 + (num_itens * 22) + 100
                largura = 600
                
                cor_fundo = (15, 23, 42)
                cor_texto = (255, 255, 255)
                cor_detalhe = (59, 130, 246)

                img = Image.new("RGB", (largura, altura_dinamica), color=cor_fundo)
                draw = ImageDraw.Draw(img)

                try:
                    font_titulo = ImageFont.truetype("arial.ttf", 30)
                    font_corpo = ImageFont.truetype("arial.ttf", 18)
                    font_itens = ImageFont.truetype("consola.ttf", 16)
                except:
                    font_titulo = ImageFont.load_default()
                    font_corpo = ImageFont.load_default()
                    font_itens = ImageFont.load_default()

                draw.text((largura//2, 50), "CERTIFICADO DE SORTEIO", fill=cor_detalhe, font=font_titulo, anchor="mm")
                draw.text((largura//2, 90), "Evidência de Amostragem de Auditoria", fill=cor_texto, font=font_corpo, anchor="mm")
                draw.line((50, 110, largura-50, 110), fill=cor_detalhe, width=2)

                agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                detalhes = [
                    f"Data/Hora: {agora}",
                    f"Tamanho do Universo: {u_size}",
                    f"Tamanho da Amostra: {s_size}",
                    f"Seed Utilizada: {seed_val}"
                ]
                
                y_offset = 150
                for linha in detalhes:
                    draw.text((50, y_offset), linha, fill=cor_texto, font=font_corpo)
                    y_offset += 30

                draw.text((50, y_offset + 20), "Itens Sorteados:", fill=cor_detalhe, font=font_corpo)
                y_offset += 50
                
                for item in itens:
                    if item.strip():
                        draw.text((60, y_offset), item, fill=cor_texto, font=font_itens)
                        y_offset += 22

                # RODAPÉ SEMPRE NO FINAL DA IMAGEM DINÂMICA
                draw.text((largura//2, altura_dinamica - 40), "Gerado por Audit Sample Generator v2.0", fill=cor_detalhe, font=font_corpo, anchor="mm")

                nome_arquivo = f"Evidencia_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{seed_val}.png"
                img.save(nome_arquivo)
                
                messagebox.showinfo("Evidência Salva", f"Relatório digital salvo com sucesso como:\n{nome_arquivo}")
            except Exception as e:
                messagebox.showerror("Erro ao Salvar", f"Não foi possível gerar a imagem:\n{e}")

    if __name__ == "__main__":
        app = AuditSampleApp()
        app.mainloop()

except Exception as e:
    with open("erro_log.txt", "w") as f:
        f.write("Erro crítico detectou ao abrir o app:\n")
        f.write(traceback.format_exc())
