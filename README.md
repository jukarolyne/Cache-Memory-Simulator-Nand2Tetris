# CacheMap: Simulador de Cache Memory

**CacheMap** é uma ferramenta educacional interativa para simular e visualizar o comportamento de Cache Memory (L1, L2) em uma CPU. Desenvolvida para estudantes aprenderem sobre Hits/Misses, Políticas de Substituição (LRU, FIFO), e Hierarquia de Memória.

## 📚 O que você vai aprender

- **Hit e Miss:** Entender quando a CPU encontra dados no cache e quando precisa buscar da memória
- **Políticas de Substituição:** Comparar LRU (Least Recently Used) e FIFO (First In, First Out)
- **Configuração de Cache:** Tamanho, Tamanho de Bloco, Associatividade
- **Hierarquia de Memória:** Interação entre L1, L2 e Memória Principal
- **Análise Visual:** Diagramas lógicos interativos que mostram o fluxo de dados em tempo real

## 🛠️ Pré-requisitos

Você precisa ter **Python 3.7 ou superior** instalado. As dependências Python serão instaladas automaticamente via `pip`.

### Windows

1. **Instale Python:**
   - Acesse [python.org](https://www.python.org/downloads/)
   - Download a versão mais recente para Windows
   - **Importante:** Durante a instalação, marque a opção "Add Python to PATH"

2. **Verifique a instalação:**
   ```bash
   python --version
   pip --version
   ```

### Linux (Ubuntu/Debian)

Python geralmente já vem instalado. Verifique:
```bash
python3 --version
pip3 --version
```

Se não estiver instalado:
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### macOS

1. **Com Homebrew (recomendado):**
   ```bash
   brew install python3
   ```

2. **Ou baixe direto:**
   - Acesse [python.org](https://www.python.org/downloads/) e baixe para macOS

Verifique a instalação:
```bash
python3 --version
pip3 --version
```

## 📦 Instalação e Configuração

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/jukarolyne/Cache-Memory-Simulator-Nand2Tetris.git
cd Cache-Memory-Simulator-Nand2Tetris
```

### Passo 2: Instalar Dependências

#### Windows (PowerShell ou CMD)
```bash
pip install -r requirements.txt
```

#### Linux/macOS (Terminal)
```bash
pip3 install -r requirements.txt
```

### Passo 3: Executar a Aplicação

#### Windows (PowerShell ou CMD)
```bash
python cms/web_backend.py
```

#### Linux/macOS (Terminal)
```bash
python3 cms/web_backend.py
```

Você deverá ver uma mensagem como:
```
 * Running on http://127.0.0.1:5000
 * WARNING: This is a development server. Do not use it in production.
```

### Passo 4: Acessar o Simulador

Abra seu navegador e acesse:
```
http://127.0.0.1:5000
```

**Crie sua conta de usuário na primeira execução e comece a simular!**

## 📂 Estrutura do Projeto

```
Cache-Memory-Simulator/
├── app.py                 # Servidor Flask (backend)
├── binary_store.py        # Módulo auxiliar
├── static/
│   ├── style.css          # Estilos da interface
│   └── app.js             # Lógica do frontend
├── templates/
│   └── index.html         # Interface principal
├── requirements.txt       # Dependências Python
└── README.md              # Este arquivo
```

## 🎮 Guia de Uso: Simulando Programas em Assembly

### 1. Preparar seu Arquivo Assembly

Crie um arquivo com extensão `.asm` com suas instruções. Exemplo: `programa.asm`

```asm
// programa.asm - Leitura e escrita em memória
@16384
M=1      // Escreve 1 na memória (endereço 16384)

@16385
M=2      // Escreve 2 na memória (endereço 16385)

@16384
D=M      // Lê valor da memória (endereço 16384)

@16640
M=D      // Escreve o valor lido em outro endereço
```

**Formatos suportados:**
- Código Hack Assembly (`.asm`, `.hack`): contém instruções com `@`, `M=`, `D=`, etc.
- Sequência de memória (`.txt`): lista de acessos já compilada

### 2. Usar o Simulador

O simulador aceita arquivos `.asm` (Hack Assembly) e `.txt` (sequência de memória) automaticamente. Basta fazer upload e clicar em "Run Simulation"!

**Próxima etapa:** Acessar o dashboard do simulador

### 3. Acessar o Dashboard

1. Abra o navegador em `http://127.0.0.1:5000`
2. Crie sua conta de usuário
3. Faça login

### 4. Configurar a Simulação

Na aba **Simulation**:

1. **Selecione seu arquivo:** Clique em "Choose File" e selecione seu arquivo `.asm` ou `.txt`
2. **Configure os parâmetros de cache:**
   - **Cache Size:** Tamanho total em bytes (ex: 256, 512, 1024)
   - **Block Size:** Tamanho do bloco em bytes (ex: 4, 8, 32, 64)
   - **Associativity:** 1 (Direct Mapped), 2, 4, 8, etc.
   - **Replacement Policy:** LRU (Least Recently Used) ou FIFO (First In First Out)

3. **Clique em "Run Simulation"**

O simulador irá:
- Detectar se é código Hack Assembly
- Converter automaticamente para sequência de memória
- Executar a simulação de cache
- Exibir resultados em tempo real

### 5. Analisar os Resultados

Na aba **Results**, você verá:

- **Hit Rate:** Percentual de hits
- **Miss Rate:** Percentual de misses
- **Total Hits:** Número total de hits
- **Total Misses:** Número total de misses
- **Access Trace:** Detalhamento de cada acesso à memória

### 6. Interagir com o Diagrama Lógico

Na aba **Logic Diagram**:

- Os circuitos ficam **verdes para HIT** e **vermelhos para MISS**
- Selecione linhas da tabela de verdade para ver em tempo real como os sinais mudam
- Entenda visualmente como tag matching, bits de validade e portas lógicas determinam um HIT ou MISS

## � Formatos de Entrada Suportados

### Formato 1: Código Hack Assembly (.asm)

O simulador aceita código assembly Hack completo:

```asm
// Escrita em memória
@16384
M=1

// Leitura de memória
@16384
D=M

// Escrita do resultado
@16640
M=D
```

**Instruções reconhecidas:**
- `@valor` - Carrega endereço no registrador A
- `M=expressão` - Escreve na memória (gera acesso de `write`)
- `D=M` - Lê da memória (gera acesso de `read`)
- `(LABEL)` - Define um rótulo
- `0;JMP` - Instrumento de salto

**O simulador converte automaticamente para sequências de memória!**

### Formato 2: Sequência de Memória Direta (.txt)

Se preferir, pode fornecer uma sequência de memória já compilada:

```
Read 4 0x4000
Write 4 0x4000
Read 4 0x4004
Write 4 0x4004
Read 4 0x4000
```

**Formato:** `[operação] [tamanho] [endereço_hex]`
- **operação:** `Read` ou `Write` (case-insensitive)
- **tamanho:** número de bytes acessados (ex: 1, 2, 4, 8)
- **endereço_hex:** endereço em hexadecimal (ex: 0x0, 0x1000, 0x10000)

## ❓ Perguntas

**P: Preciso gerar um arquivo de sequência de memória antes de usar o simulador?**  
R: **Não!** O simulador detecta automaticamente se seu arquivo é código Hack Assembly e converte para sequência de memória. Basta fazer upload do `.asm` e clicar em "Run Simulation".

**P: Qual formato usar: .asm ou .txt?**  
R: Use `.asm` se tiver código assembly completo. Use `.txt` apenas se já tiver a sequência de memória compilada. O simulador aceita ambos!

**P: O simulador não inicia - "Connection refused"**  
R: O servidor Flask pode não estar rodando ou ainda está iniciando. Tente:
1. Verifique se você executou `python cms/web_backend.py` (ou `python3 cms/web_backend.py` no macOS/Linux)
2. Aguarde 3-5 segundos após iniciar o servidor
3. Atualize a página no navegador (F5 ou Ctrl+R)
4. Verifique a saída do terminal para mensagens de erro
5. Se a porta 5000 estiver em uso, procure fechar outros programas usando essa porta

## 📝 License
This project is open-source and available under the MIT License.

## 🙏 Créditos

Este projeto é baseado no trabalho original de [Sarvagya Chaturvedi](https://github.com/Sarvagya-24-chaturvedi/Cache-Memory-Simulator). Foi adaptado para a disciplina de Elementos de Sistemas Computacionais, presente no curso de Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE).

**Repositório Original:** https://github.com/Sarvagya-24-chaturvedi/Cache-Memory-Simulator