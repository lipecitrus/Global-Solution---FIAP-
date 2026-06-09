# Dados Simulados

    # Status de Módulos Críticos
modulos = {
        "suporte_vida": 1,
        "energia": 1,
        "comunicacao": 1,
        "habitat": 1,
        "laboratorio": 0,
        "armazenamento": 1
    }

    # Geração e Consumo de Energia
energia = [
    {
        "horario": "00:00",
        "geracao_solar": 0,
        "geracao_nucelar": 60,
        "consumo": 45,
        "reserva": 800,
    },
    {
        "horario": "04:00",
        "geracao_solar": 0,
        "geracao_nucelar": 60,
        "consumo": 42,
        "reserva": 818,
    },
    {
        "horario": "08:00",
        "geracao_solar": 35,
        "geracao_nucelar": 60,
        "consumo": 50,
        "reserva": 863,
    },
    {
        "horario": "12:00",
        "geracao_solar": 85,
        "geracao_nucelar": 60,
        "consumo": 58,
        "reserva": 950,
    },
    {
        "horario": "16:00",
        "geracao_solar": 50,
        "geracao_nucelar": 60,
        "consumo": 55,
        "reserva": 1005,
    },
    {
        "horario": "20:00",
        "geracao_solar": 5,
        "geracao_nucelar": 60,
        "consumo": 48,
        "reserva": 1022,
    }
    ]

# Matriz de Variáveis Ambientais
matriz_ambiente = [
    ["Horario", "temp_int", "temp_ext", "radiacao", "comunicacao"],
    ["00:00", 21, -75, 2.4, 95],
    ["04:00", 21, 120, 2.7, 93],
    ["08:00", 22, -60, 2.1, 97],    
    ["12:00", 23, -15, 1.8, 99],
    ["16:00", 22, -35, 2.0, 96],
    ["20:00", 21, -68, 2.3, 94]
    ]

# Log de Eventos 
eventos = [
        {"horario": "00:30", "evento": "Início da rotina automática de monitoramento dos módulos"},
        {"horario": "03:15", "evento": "Alerta de aumento de radiação cósmica"},
        {"horario": "05:40", "evento": "Sensor meteorológico recalibrado"},
        {"horario": "08:20", "evento": "Painéis solares iniciaram operação máxima"},
        {"horario": "11:10", "evento": "Detectada tempestade de poeira a 40 km da colônia"},
        {"horario": "13:50", "evento": "Comunicação com satélite orbital estabilizada"},
        {"horario": "17:30", "evento": "Sistema entrou em modo de economia preventiva"},
        {"horario": "21:05", "evento": "Verificação completa dos sistemas concluída sem falhas críticas"}
    ]


# FIFO
from collections import deque

fila_alertas = deque([
    "Aumento de radiação cósmica",
    "Tempestade de poeira detectada",
    "Modo de economia preventiva"
])

alerta_atual = fila_alertas.popleft()

# LIFO
pilha_eventos = []

pilha_eventos.append("Aumento de radiação cósmica")
pilha_eventos.append("Tempestade de poeira detectada")
pilha_eventos.append("Modo de economia preventiva")

ultimo_evento = pilha_eventos.pop()

# Limites de operação normal
limites = {
    "temp_int_min": 20,
    "temp_int_max": 25,
    "radiacao_max": 2.5,
    "comunicacao_min": 95,
    "vento_max": 35,
    "reserva_energia_min": 850,
    "consumo_max": 55
}

# Condicoes
if matriz_ambiente[3][1] < limites["temp_int_min"] or matriz_ambiente[3][1] > limites["temp_int_max"]:
    print("ALERTA: Temperatura fora da faixa segura")
else:
    print("Temperatura normal")

if matriz_ambiente[2][3] > 2.5 and matriz_ambiente[2][4] < 95:
    print("ALERTA CRÍTICO: Radiação alta e comunicação comprometida.")

if not modulos["laboratorio"]:
    print("ALERTA: Laboratório fora de operação.")

# Dados da reserva de energia
x = [0, 1, 2, 3, 4, 5]
y = [800, 818, 863, 950, 1005, 1022]

n = len(x)

soma_x = sum(x)
soma_y = sum(y)

soma_xy = 0
soma_x2 = 0

for i in range(n):
    soma_xy += x[i] * y[i]
    soma_x2 += x[i] ** 2

# Coeficiente angular (a)
a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)

# Coeficiente linear (b)
b = (soma_y - a * soma_x) / n

# Previsão para próximo período
proximo_x = 6
previsao = a * proximo_x + b

print(f"Taxa de crescimento: {a:.2f}")
print(f"Previsão da reserva às 00:00: {previsao:.2f}")

if previsao < limites["reserva_energia_min"]:
    print("ALERTA: ativar modo de economia de energia.")
else:
    print("Sistema operando normalmente.")