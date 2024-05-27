# 103. Agrupamento
"""
Agrupamento (Clustering)
> Aplicado em problemas de aprendizagem não supervisionada.
> Realiza agrupamento de dados com base em características similares.
> Exemplos:
    >> Identificação de perfis de clientes.
    >> Segmentação de produtos semelhantes.
    >> Agrupamento de sintomas característicos de doenças.
    >> Perfis nos streamings (Netflix, Spotify, Globoplay)
"""
#%%
# 107. K-Means (teoria)
"""
Algoritmo K-Means
> Utiliza a Distância Euclidiana para definir os grupos:
    >> Bidimensional: d(x,y) = sqrt(sum(y[i]-x[i])^2)
    >> Multidimensional: dAB = sqrt((xB-xA)^2+(yB-yA)^2+...+(zB-zA)^2)
    https://www.ml-science.com/k-means-clustering
    
Definição do número de clusters
> Elbow Method
    >> Testa vários valores de k.
    >> Define i número de clusters através do ponto de inflexão no gráfico do WCSS (Within Cluster Sum of Squares) em
    função do número de clusters.
    WCSS = sum(Xi-Yi)^2

Técnica básica do agrupamento K-Means
> Algoritmo K-Means++: Evita centróides em posições ruins
"""
#%%