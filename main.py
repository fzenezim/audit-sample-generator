import customtkinter as ctk
import random
from tkinter import messagebox

# Configuração de Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AuditSampleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Audit Sample Generator - v1.1")
        self.geometry("500x600")

        # Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Gerador de Amostras de Auditoria", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=(20, 20))

        # Input Section
        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.input_frame.pack(padx=20, pady=10, fill="x")

        # Universe Size
        self.univ_label = ctk.CTkLabel(self.input_frame, text="Tamanho do Universo:")
        self.univ_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.univ_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Ex: 100")
        self.univ_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Sample Size
        self.size_label = ctk.CTkLabel(self.input_frame, text="Tamanho da Amostra:")
        self.size_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.size_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Ex: 25")
        self.size_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Seed
        self.seed_label = ctk.CTkLabel(self.input_frame, text="Seed (Semente):")
        self.seed_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.seed_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Ex: 12345")
        self.seed_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Button
        self.generate_button = ctk.CTkButton(
            self.main_frame, 
            text="Gerar Amostra", 
            command=self.generate_sample,
            font=ctk.CTkFont(weight="bold")
        )
        self.generate_button.pack(pady=20)

        # Result Section
        self.result_label = ctk.CTkLabel(self.main_frame, text="Resultado (Sorteio - Item):")
        self.result_label.pack(padx=20, pady=(10, 0), anchor="w")
        self.result_text = ctk.CTkTextbox(self.main_frame, height=250)
        self.result_text.pack(padx=20, pady=10, fill="x")

        # Copy Button
        self.copy_button = ctk.CTkButton(
            self.main_frame, 
            text="Copiar Resultado", 
            command=self.copy_result,
            fg_color="#1e293b", 
            hover_color="#334155"
        )
        self.copy_button.pack(pady=(0, 20))

        self.input_frame.grid_columnconfigure(1, weight=1)

    def generate_sample(self):
        try:
            # Captura inputs
            universe_size = int(self.univ_entry.get())
            sample_size = int(self.size_entry.get())
            seed_val = self.seed_entry.get()
            
            if universe_size <= 0 or sample_size <= 0:
                messagebox.showwarning("Aviso", "Os tamanhos devem ser números positivos.")
                return

            if sample_size > universe_size:
                messagebox.showwarning("Aviso", f"A amostra ({sample_size}) não pode ser maior que o universo ({universe_size}).")
                return

            # Lógica da Seed para reprodutibilidade
            if seed_val:
                random.seed(seed_val)
            else:
                random.seed() # Random real

            # Sorteio de números únicos dentro do universo
            # range(1, universe_size + 1) cria a lista de 1 até o total
            sample = random.sample(range(1, universe_size + 1), sample_size)
            
            # Ordenamos a amostra para facilitar a auditoria (opcional, mas recomendado)
            sample.sort()
            
            # Formatação do resultado (Ex: 1 - item 12)
            result_lines = []
            for i, item_num in enumerate(sample, 1):
                result_lines.append(f"{i} - item {item_num}")
            
            final_result = "\\n".join(result_lines)
            
            # Exibe no resultado
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", final_result)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

    def copy_result(self):
        self.result_text.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(self.result_text.get("1.0", "end-1c"))
        messagebox.showinfo("Sucesso", "Resultado copiado para a área de transferência!")

if __name__ == "__main__":
    app = AuditSampleApp()
    app.mainloop()
