# Sistema de Monitoramento da Colônia Aurora

## Integrantes

| Integrante            | RM       |
| --------------------- | -------- |
| Filipe Augusto Chaves | RM570827 |

---

## Resumo do Problema e Cenário Analisado

O projeto simula o monitoramento operacional da Colônia Aurora, uma instalação espacial que depende do funcionamento contínuo de módulos críticos, geração de energia e controle ambiental.

O sistema realiza o acompanhamento do estado dos módulos da colônia, monitora variáveis ambientais, registra eventos operacionais e analisa a disponibilidade energética. Além disso, utiliza uma técnica de previsão para estimar a reserva de energia futura e gerar alertas preventivos quando necessário.

O objetivo é fornecer um diagnóstico automatizado do estado da missão, auxiliando na tomada de decisões e aumentando a segurança operacional.

---

## Estruturas de Dados Utilizadas

### Dicionários (dict)

Utilizados para armazenar:

- Status dos módulos críticos;
- Limites operacionais do sistema.

Exemplo:

```python
modulos = {
    "suporte_vida": 1,
    "energia": 1,
    "comunicacao": 1,
    "habitat": 1,
    "laboratorio": 0,
    "armazenamento": 1
}
```

Motivo: permitem acesso rápido às informações através de chaves identificadoras.

### Listas (list)

Utilizadas para armazenar:

- Dados históricos de energia;
- Eventos registrados;
- Valores usados na previsão.

Motivo: facilitam o armazenamento sequencial e a iteração dos dados.

### Matrizes (listas bidimensionais)

Utilizadas para representar as variáveis ambientais em diferentes horários.

Exemplo:

```python
matriz_ambiente = [
    ["Horario", "temp_int", "temp_ext", "radiacao", "comunicacao"],
    ...
]
```

Motivo: organização tabular dos dados ambientais.

### Fila FIFO (deque)

Utilizada para gerenciamento de alertas.

```python
fila_alertas = deque([...])
```

Motivo: o primeiro alerta registrado é o primeiro a ser processado.

### Pilha LIFO (list)

Utilizada para armazenar eventos recentes.

```python
pilha_eventos = []
```

Motivo: o último evento registrado é o primeiro a ser consultado.

---

## Regras Lógicas Principais do Diagnóstico

O sistema utiliza operadores lógicos AND, OR e NOT para avaliar condições de segurança.

### Regra 1 – Temperatura Interna

```python
if temperatura < minimo or temperatura > maximo
```

Gera alerta quando a temperatura estiver fora da faixa segura.

### Regra 2 – Radiação e Comunicação

```python
if radiacao > limite and comunicacao < limite
```

Gera alerta crítico quando há radiação elevada simultaneamente a falha de comunicação.

### Regra 3 – Estado do Laboratório

```python
if not modulos["laboratorio"]
```

Gera alerta quando o laboratório está fora de operação.

---

## Técnica de Previsão Utilizada e Resultado

Foi utilizada Regressão Linear Simples para estimar a evolução da reserva de energia da colônia.

A técnica calcula:

- Coeficiente Angular (taxa de crescimento);
- Coeficiente Linear;
- Previsão para o próximo período.

Resultado obtido:

```text
Taxa de crescimento: 49.63
Previsão da reserva às 00:00: 1085.80
```

Como o valor previsto está acima do limite mínimo de segurança (850 unidades), o sistema considera a operação energética estável.

---

## Como Executar

Certifique-se de possuir Python 3 instalado.

Execute o sistema através do terminal:

```bash
python src/sistema.py
```

---

## Exemplo de Entrada e Saída do Sistema

### Entrada

Dados simulados da Colônia Aurora:

- Status dos módulos;
- Dados energéticos;
- Variáveis ambientais;
- Eventos operacionais.

### Saída

```text
Temperatura normal

ALERTA: Laboratório fora de operação.

Taxa de crescimento: 49.63

Previsão da reserva às 00:00: 1085.80

Sistema operando normalmente.
```

---

## Recomendações Geradas pelo Sistema

- Manter monitoramento contínuo da radiação cósmica;
- Verificar a disponibilidade do laboratório e planejar manutenção corretiva;
- Continuar acompanhando os níveis de comunicação;
- Preservar a reserva energética acima do limite mínimo de segurança;
- Manter o modo de economia preventiva disponível para situações de emergência.

---

## Link do Vídeo no YouTube

Inserir aqui o link da demonstração do projeto:

```text
https://youtu.be/UDgvR-v3stw
```

---

## Conclusões e Aprendizados

O desenvolvimento do Sistema de Monitoramento da Colônia Aurora permitiu aplicar conceitos fundamentais de programação e análise de dados, incluindo estruturas de dados, operadores lógicos, filas, pilhas e regressão linear.

O projeto demonstrou como técnicas computacionais podem ser utilizadas para monitorar sistemas críticos, gerar diagnósticos automáticos e apoiar decisões operacionais.

Entre os principais aprendizados destacam-se:

- Organização de dados em estruturas adequadas;
- Implementação de regras lógicas para diagnóstico;
- Manipulação de filas e pilhas;
- Aplicação prática de regressão linear para previsão;
- Desenvolvimento de sistemas de monitoramento automatizado.
