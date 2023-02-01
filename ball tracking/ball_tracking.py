# Rastreador de bolas utilizando a técnica de transformação de semicírculos

# Importando bibliotecas necessárias
import cv2 as cv
import numpy as np
# Capturando video a ser utilizado
videoCapture = cv.VideoCapture('ball_tracking_example.mp4')

# Essa variável vai servir para capturar círculos de frames anteriores, auxiliando no processo de detectar mais círculos 'sólidos' e menos aleatórios.
prevCircle = None

# Essa função vai calcular a distância do quadrado da distância entre os 2 pontos de cada frame no vídeo.
dist = lambda x1, y1, x2, y2: (x1-x2)**2+(y1-y2)**2

# Criando função com gerenciamento de erros (caso não seja encontrado um vídeo). Caso haja algum erro, o código será parado.
while True:
    ret, frame = videoCapture.read()
    if not ret: break
    
    # Iniciando o processo de eliminação de possíveis ruídos grosseiros no vídeo.
    # Convertendo o vídeo para ser trabalhado no cinza.
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Adicionando uma taxa de blur (como um 'borrão' numa tela) na tela. (Quanto maior os valores, mais borrado o frame ficará).
    blurFrame = cv.GaussianBlur(grayFrame, (17,17), 0)
    # A importância do processo acima dá-se por diminuir o 'risco' do programa captar círculos indesejados causados pelos ruídos da imagem, atrapalhando no processo de transformação dos círculos.
    
    # Iniciando o processo de transformação dos semicírculos utilizando o método HoughCircles. 
    # Valores: 
    # (Vídeo que utilizaremos[blurFrame], o método de transformada[HOUGH__GRADIENT], dp[1.2], distância mín.[500(distância entre os círculos que serão rastreados, quanto maior o número, menos círculos serão rastreados, e quanto menor, o oposto ocorrerá)], param1=sensibilidade (se for muito alto não encontrará muitos círculos e se for muito baixo, o oposto), param2=precisão do detector(número de pontos que precisaremos para identificar um círculo, minRadius = menor raio de círculo a ser detectado, maxRadius = maior raio de círculo a ser detectado)
    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 500, param1=140, param2=30, minRadius=35, maxRadius=75)
    # Este método resultará nos círculos que serão detectados ao longo da exebição do vídeo.

    # Função para detectar se há ou não círculos presentes no vídeo.
    if circles is not None:
        # Caso haja círculos, eles serão armazenados na variável 'circles'.
        circles = np.uint16(np.around(circles))
        # Variável que recebe as coordenadas.
        chosen = None
        # Checando se o círculo não se configura como um 'None'
        for i in circles[0, :]:
            if chosen is None: chosen = i
            # Checando se o círculo for de fato um círculo
            if prevCircle is not None:
                # Cálculo para validação de um círculo através das coordenadas recebidas pelas variáveis.
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    # Caso um círculo seja identificado no ponto central, ele será a referência.
                    chosen = i
        # Desenhando o círculo.
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0,100,100), 3)
        # Desenhando a circunferência do círculo detectado.
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255), 3)
        # Configurando o círculo anterior como círculo atual.
        prevCircle = chosen
    
    # Exibindo o círculo nos frames.
    cv.imshow('circles', frame)
    
    # Criando um mecanismo de saída da execução. Caso Q seja pressionado, o programa será finalizado.
    if cv.waitKey(1) & 0xFF == ord('q'): break

#Saindo e fechando as janelas de execução. 
videoCapture.release()
cv.destroyAllWindows()