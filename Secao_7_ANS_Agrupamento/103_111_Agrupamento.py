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
# 111. Agrupamento Hierárquico (teoria)
"""
Agrupamento Hierárquico (Agglomerative Hierarchical Clustering, AH)

> Aplicado em problemas de aprendizagem não supervisionada.
> Busca construir uma hierarquia de grupos, de forma aninhada, mesclando-os ou dividindo-os sucessivamente.
> Esquematizada como forma de uma árvore e representada graficamente através de um dendrograma.

Métodos
> Métodos aglomerativos (das folhas pra raiz);
> Métodos divisivos (da raiz para as folhas);
> Dendrograma por distância (agrupa pela distância euclidiana);
> Dendrograma por similaridade (agrupa pelo coeficiente de similaridade);

Tipos diferentes de Ligações
> Simples (single linkage):
    >> A distância entre dois clusters é a mínima distância entre observações de pares de clusters.
> Média (average linkage):
    >> A distância entre dois clusters é a distância média entre cada ponto em um cluster para cada particular em outro.
> Completa (complete linkage):
    >> A distância entre dois clusters é a máxima distância entre observações de pares de clusters.
> Ala (ward linkage):
    >> A distância entre clusters é a soma das diferenças quadradas em todos os clusters.
    

"""