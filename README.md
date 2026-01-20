# People Counter

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)

Este projeto implementa um sistema de monitoramento de fluxo bidirecional em tempo real. O algoritmo contabiliza entradas ("In") e saídas ("Out"), gerando métricas de tráfego total em ambientes controlados.

O sistema utiliza YOLOv8 combinada com técnicas de processamento de imagem (OpenCV) para focar a detecção em uma Região de Interesse (ROI), otimizando o desempenho e evitando contagens falsas fora da área monitorada.

> A visualização processada é exportada automaticamente para o arquivo `people_control.mp4` ao final da execução.

## Funcionalidades

- **Detecção Otimizada em ROI:** O processamento da IA é restrito a uma área de corte específica, economizando recursos computacionais.
- **Contagem Bidirecional:** Monitoramento inteligente de cruzamento de linha para distinguir quem entra e quem sai.
- **Exportação de Vídeo:** Gravação automática do resultado da análise em arquivo `.mp4`.

## Tecnologias Utilizadas
- **Linguagem:** Python.
- **Bibliotecas:**
    - YOLOv8.
    - OpenCV.
    - NumPy.

## Dataset para Teste

O vídeo original utilizado no projeto é muito grande para o GitHub. Os resultados e o video original estão disponíveis no link abaixo:

[![Download Video](https://img.shields.io/badge/Visualizar/Dowload-Video-red?style=for-the-badge&logo=google-drive&logoColor=white)](https://drive.google.com/drive/folders/1HsWtsfTKCyB1dqiItrqT6CyESdKwLY3K?usp=drive_link)

> **Nota:** Após baixar, salve o arquivo na pasta `Data/` com o nome `people.mp4`.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/caio-alm/Counter-People-YOLO.git
   cd Counter-People-YOLO
   ```

2. Instale as Dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o programa:
   ```bash
   python counter.py
   ```
