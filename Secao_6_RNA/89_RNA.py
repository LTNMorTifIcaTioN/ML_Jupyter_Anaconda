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