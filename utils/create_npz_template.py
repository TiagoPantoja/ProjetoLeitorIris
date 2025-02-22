import numpy as np

# Definindo um user_id e um array de features (pode ser numpy.array ou list)
meu_user_id = "user123"
minhas_features = np.array([0.1, 0.2, 0.3, 0.4])

# Salvando em um arquivo .npz chamado "template_user123.npz"
np.savez("template_user123.npz", user_id=meu_user_id, features=minhas_features)

print("Arquivo .npz criado com sucesso!")