import numpy as np

# Lista de user_ids e respectivas features
user_ids = ["user001", "user002", "user003"]
feature_arrays = [
    np.array([0.1, 0.2, 0.3]),
    np.array([0.3, 0.7, 0.5]),
    np.array([0.9, 0.1, 0.2])
]

for uid, feats in zip(user_ids, feature_arrays):
    filename = f"template_{uid}.npz"
    # Salva 'uid' e 'feats' no arquivo .npz
    np.savez(filename, user_id=uid, features=feats)
    print(f"Arquivo {filename} criado com user_id='{uid}' e features={feats.tolist()}")