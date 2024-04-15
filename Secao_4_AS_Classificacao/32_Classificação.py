# Análise de desempenho: Matriz de confusão

vn = 0  # 'verdadeiro negativo'
vp = 0  # 'verdadeiro positivo'
fn = 0  # 'falso negativo'
fp = 0  # 'falso positivo'

accuracy = (vn + vp) / (vn + vp + fn + fp)
precision = vp / (vp + fp)
recall = vp / (vp + fn)
f1_score = 2 * ((precision * recall) / (precision + recall))
