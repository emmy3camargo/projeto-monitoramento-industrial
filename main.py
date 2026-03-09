import time
import random

def monitorar_secador():
    print("--- SISTEMA DE MONITORAMENTO DE SECAGEM - SUDATI/PORTO ---")
    print("Iniciando leitura dos sensores...\n")
    
    # Simula 5 leituras de temperatura
    for i in range(1, 6):
        temp = random.randint(60, 120) # Gera temperatura entre 60 e 120 graus
        print(f"Leitura {i}: Temperatura atual em {temp}°C")
        
        if temp > 100:
            print("⚠️ ALERTA: Temperatura acima do limite! Risco de incêndio ou dano à lâmina.")
        elif temp < 70:
            print("❄️ AVISO: Temperatura baixa. Processo de secagem lento.")
        else:
            print("✅ Estabilizado: Temperatura ideal para produção.")
        
        time.sleep(1) # Pausa de 1 segundo entre leituras

    print("\nRelatório final gerado com sucesso.")

if __name__ == "__main__":
    monitorar_secador()
