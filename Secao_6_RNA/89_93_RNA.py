# 89. Neurônio Biológico e neurônio artificial
"""
Redes Neurais
'https://www.asimovinstitute.org/neural-network-zoo/'

Principais Redes
> Redes Multilayer Perceptron (classificação binária).
> Redes Naturais Convolucionais (classificar imagens).
> Redes Neurais Recorrentes (processamento de dados sequenciais, como som, dados de séreis temporais ou linguagem
natual).
> Long short-term memory (LSTM): variação da rede recorrente.
> Redes de Hopfield (armazenar memórias).
> Máquinas de Boltzmann (rede neural recorrente estocástica).
> Deep Belied Network (reconhecer, agrupar, gerar imagens, vídeos, dados de captura de movimento e nlp).
> Deep Auto-Encoders (reduzir a dimensionalidade).
> Generative Adversarial Network (imita qualquer distribuição de dados).
> Deep Neural Network Capsules (maior expansão de Deep Learning).
"""
#%%
# 90. Perceptron
"""
Perceptron de uma camada
> Algoritmo mais simples de uma rede neural que pode ser usado para classificação de padrões que sejam
LINEARMENTE SEPARÁVEIS.

> Modelo matemático com mais de uma entrada e uma saída binária
    >> combinador linear: Uk = sum(Wkj * Xi) + b, onde Xn = entrada, Wn = pesos e b = bias;
    >> função de ativação: f(u) = { 1 , se u >= 0 }, { 0 , se u < 0 };
        >>> Bias (Viés): aumenta o grau de liberdade dos ajustes dos pesos;
            >>>> f(u) = { 0 , se w * x + b <= 0 }, { 1 , se w * x + b > 0 };
    >> saída: Yk = f(Uk);
 
Redes Multilayer Perceptron (MLP)
> Todos os neurônios são ligados aos neurônios da camada subsequente, não havendo ligação com os neurônios laterais.
> Usado para classificação de padrões que sejam são linearmente separáveis.

Processo de construção de uma rede neural
1) Função de ativação.
2) Algoritmo de aprendizagem.
3) Topologia da rede neural.
"""
#%%
# 91. Funções de ativação
"""
Função de Ativação
> Permite que pequenas alterações no peso e bias resultem em pequenas modificações no resultado de saída.
> Decide se o neurônio será ativado. Filtra se a informação é relevante.
> Possibilita resoluções de problemas complexos, não lineares.
> Existem várias funções de ativação e a escolha correta para cada aplicação é fundamental para atingir ótimos
resultados.

Principais Funções de Ativação
1) Função de Etapa Binária (Binary Step), ou função degrau, ou função de Heaviside.
    >> Utilizado para classificação binária.
    f(x) = {1 , se x >= 0}, {0 , se x < 0};

2) Função Linear:
    >> Obedece a função: f(x) = ax+b;

3) Função de Sigmoide:
    >> Funcionam melhor em classificadores.
    >> Limitada a duas classes (atributo de saída).
    >> Muito utilizado nos algoritmos.
    f(x) = 1/(1+e^-ax);

4) Função tanh(tangente hiperbólico):
    >> Similar a função sigmoide, mas simétrico à origem.
    f(x) = tanh(x) = 2/(1+e^-2x) - 1;

5) Função ReLU(Rectified Linear Unit):
    >> Muito utilizada.
    >> Não ativa todos os neurônios ao mesmo tempo.
    >> Deve ser usada apenas nas camadas ocultas.
    >> Normalmente é a primeira a ser testada.
    >> f(x) = max(0,x);

6) Função Leaky ReLU:
    >> Evolução da função ReLU.
    f(x) = {a*x, se x < 0}, {x, se x >= 0};

7) Função Softmax:
    >> Utilizada em problemas de classificação.
    >> Sem limitação no número de classes.
    f(x)j = e^Xj / sum(e^Xk), para j = 1, ..., k;
     
"""
#%%
# 92. Aprendizagem nas redes neurais
"""
Aprendizagem nas redes neurais artificiais
> Conjunto de regras ou procedimentos qu adptam ou ajustam parâmetros para que a rede possa aprender uma determinada
função e melhorar seu desempenho.

Tipos de aprendizagens
> Supervisionada.
> Não Supervisionada.
> Por Reforço.

Processo de Aprendizagem
> Rede neural tem a capacidade de aprender e de melhorar seu desempenho por meio de aprendizagem.
> As regras de aprendizado definem como a rede deve ajustar os pesos sinápticos.
> Existem quatro tipos de regras de aprendizagem:
    1. Correção de Erro.
    2. Hebbiana.
    3. Boltzmann.
    4. Competitiva.

Regras de Aprendizagem
1) Regra por Correçao de Erro:
    >> Ajusta os pesos sinápticos por meio do erro, que é obtido através da diferença entre o valor de saída da rede e o
    valor esperado em um ciclo de treinamento. Com isso gradualmente vai diminuindo o erro geral da rede.
2) Regra Hebbiana:
    >> Postulado de Heb: 'Se dois neurônios em ambos os lados de uma sinapse são ativados sincronamente e
    simultâneamente, então a força daquela sinapse é seletivamente aumentada'.
3) Regra Boltzmann:
    >> Procedimento de aprendizagem não-supervisionado para modelar uma distribuição de probabilidade.
    >> Dois estados possíveis: ligado (+1) e desligado (-1).
    >> Neurônios possuem conexões bidirecionais.
4) Regra Competitiva:
    >> Neurônios são forçados a competir entre si e somente um será atibo, ou seja, o que tiver maior similaridade com
    o padrão de entrada.
    >> Todos os pesos dos neurônios próximos ao neurônio vencedor terão seus valores ajustados.
"""
#%%
# 93. Aprendizagem com descida do gradiente
"""
Descida do Gradiente:
> Algoritmo que tem por objetivo encontrar o ponto de mínimo de uma função.
> Uma função pode ter vários pontos de mínimo (locais e globais), o objetivo é encontrar o mínimo global.

Gradiente: G = ∂f(x)/∂x + ∂f(x)/∂y + ∂f(x)/∂z
> Vetor cujo módulo é a derivada direcional máxima (sentido maior da variação).
> Aponta para onde a grandeza resultante da função tem seu maior crescimento.
> Derivada: Taxa de variação instantânea entre grandezas (variáveis) - dy/dx = y'

Funcionamento:
> É utilizado para encontrar o mínimo de uma função de erro (função de perda ou função de custo) quando aplicado a
algoritmos de redes neurais artificiais.

Evolução do algoritmo de descida do gradiente:
> SGD (Stochastic Gradient Descent): Gradiente descendente estocástico. Aumenta o número de atualizações nas interações
(todos os dados atualizam os pesos). Evita erro no mínimo local, mas tem excesso de atualizações.
> SGD Mini-batch: Descida de Gradiente estocástica com mini lotes. Esse é o algoritmo principal da descida dp gradiente.
Diminuí o número de atualizações e aumenta a velocidade de processamento.
> Momento (Momentum): Técnica para aumentar a velocidade do algoritmo de descida do gradiente, reduzir instabilidades e
evitar mínimos locais. Seu valor varia de 0 (não utilização) a 1. O valor recomendado para o termo momentum é 0,3.
"""