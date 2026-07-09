import customtkinter as ctk
import random
from tkinter import messagebox

# Configuração de Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AuditSampleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Audit Sample Generator - v1.0")
        self.geometry("600x700")

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

        # Sample Size
        self.size_label = ctk.CTkLabel(self.input_frame, text="Tamanho da Amostra:")
        self.size_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.size_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Ex: 10")
        self.size_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Seed
        self.seed_label = ctk.CTkLabel(self.input_frame, text="Seed (Semente):")
        self.seed_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.seed_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Ex: 12345")
        self.seed_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Item List
        self.items_label = ctk.CTkLabel(self.main_frame, text="Lista de Itens (um por linha):")
        self.items_label.pack(padx=20, pady=(10, 0), anchor="w")
        self.items_text = ctk.CTkTextbox(self.main_frame, height=200)
        self.items_text.pack(padx=20, pady=10, fill="x")

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
        self.result_text = ctk.CTkTextbox(self.main_frame, height=200)
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
            sample_size = int(self.size_entry.get())
            seed_val = self.seed_entry.get()
            items_raw = self.items_text.get("1.0", "end-1c")
            
            if not items_raw.strip():
                messagebox.showwarning("Aviso", "Por favor, insira a lista de itens.")
                return

            # Limpa a lista de itens
            items = [line.strip() for line in items_raw.split('\\n') if line.strip()]
            
            if sample_size <= 0:
                messagebox.showwarning("Aviso", "O tamanho da amostra deve ser maior que zero.")
                return

            if sample_size > len(items):
                messagebox.showwarning("Aviso", f"O tamanho da amostra ({sample_size}) é maior que o universo de itens ({len(items)}).")
                return

            # Lógica da Seed
            if seed_val:
                random.seed(seed_val)
            else:
                random.seed() # Random real

            # Sorteio sem repetição
            sample = random.sample(items, sample_size)
            
            # Formatação do resultado
            result_lines = []
            for i, item in enumerate(sample, 1):
                result_lines.append(f"{i} - {item}")
            
            final_result = "\\n".join(result_lines)
            
            # Exibe no resultado
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", final_result)

        except ValueError:
            messagebox.showerror("Erro", "O tamanho da amostra deve ser um número inteiro.")

    def copy_result(self):
        self.result_text.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(self.result_text.get("1.0", "end-1c"))
        messagebox.showinfo("Sucesso", "Resultado copiado para a área de transferência!")

if __name__ == "__main__":
    app = AuditSampleApp()
    app.mainloop()
