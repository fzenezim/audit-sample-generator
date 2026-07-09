import argparse
from audit_core import generate_sample, generate_evidence_image

def main():
    parser = argparse.ArgumentParser(description="Audit Sample Generator CLI for Automation")
    parser.add_argument("--universo", type=int, required=True, help="Tamanho do universo")
    parser.add_argument("--amostra", type=int, required=True, help="Tamanho da amostra")
    parser.add_argument("--seed", type=str, help="Semente para reprodutibilidade")
    parser.add_argument("--evidencia", action="store_true", help="Gerar imagem de evidência")

    args = parser.parse_args()

    try:
        # 1. Gera a amostra
        amostra = generate_sample(args.universo, args.amostra, args.seed)
        
        # 2. Imprime a lista no terminal (stdout) para o n8n capturar
        print("\n".join(amostra))
        
        # 3. Se solicitado, gera a imagem de evidência
        if args.evidencia:
            path = generate_evidence_image(args.universo, args.amostra, args.seed, amostra)
            print(f"\n--- EVIDENCIA_PATH: {path} ---")
            
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()
