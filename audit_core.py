import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def generate_sample(universe_size, sample_size, seed_val=None):
    """Lógica pura de sorteio reprodutível."""
    if seed_val:
        random.seed(seed_val)
    else:
        random.seed()
    
    sample = random.sample(range(1, universe_size + 1), sample_size)
    sample.sort()
    
    # Formata como lista de strings "1 - item X"
    return [f"{i+1} - item {item}" for i, item in enumerate(sample)]

def generate_evidence_image(universe_size, sample_size, seed_val, results, output_path=None):
    """Lógica pura de geração de imagem de evidência."""
    num_itens = len(results)
    altura_total = 300 + (num_itens * 22) + 50
    largura = 600
    
    cor_fundo = (15, 23, 42)
    cor_texto = (255, 255, 255)
    cor_detalhe = (59, 130, 246)

    img = Image.new("RGB", (largura, altura_total), color=cor_fundo)
    draw = ImageDraw.Draw(img)

    try:
        font_titulo = ImageFont.truetype("arial.ttf", 30)
        font_corpo = ImageFont.truetype("arial.ttf", 18)
        font_itens = ImageFont.truetype("consola.ttf", 16)
    except:
        font_titulo = ImageFont.load_default()
        font_corpo = ImageFont.load_default()
        font_itens = ImageFont.load_default()

    draw.text((largura//2, 30), "Audit Sample Generator v2.1", fill=cor_detalhe, font=font_corpo, anchor="mm")
    draw.text((largura//2, 70), "CERTIFICADO DE SORTEIO", fill=cor_detalhe, font=font_titulo, anchor="mm")
    draw.text((largura//2, 110), "Evidência de Amostragem de Auditoria", fill=cor_texto, font=font_corpo, anchor="mm")
    draw.line((50, 130, largura-50, 130), fill=cor_detalhe, width=2)

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    detalhes = [
        f"Data/Hora: {agora}",
        f"Tamanho do Universo: {universe_size}",
        f"Tamanho da Amostra: {sample_size}",
        f"Seed Utilizada: {seed_val or 'S_ALEATORIA'}"
    ]
    
    y_offset = 160
    for linha in detalhes:
        draw.text((50, y_offset), linha, fill=cor_texto, font=font_corpo)
        y_offset += 30

    draw.text((50, y_offset + 20), "Itens Sorteados:", fill=cor_detalhe, font=font_corpo)
    y_offset += 50
    
    for item in results:
        draw.text((60, y_offset), item, fill=cor_texto, font=font_itens)
        y_offset += 22

    if output_path is None:
        output_path = f"Evidencia_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{seed_val or 'S_ALEATORIA'}.png"
    
    img.save(output_path)
    return output_path
