import json, numpy as np
from pathlib import Path
import os

BASE = Path(os.environ.get("AzureWebJobsScriptRoot", Path(__file__).resolve().parent))
DATA = BASE / "artifacts"

E = np.load(DATA / "embeddings_clean.npy").astype("float32")
P = np.load(DATA / "user_profiles.npy").astype("float32")
id2row = json.loads((DATA / "id_to_row.json").read_text())
cold = json.loads((DATA / "cold_start_top5.json").read_text())
user2idx = json.loads((DATA / "user_to_idx.json").read_text())


def _norm(X):
    n = np.linalg.norm(X, axis=1, keepdims=True)
    n[n == 0] = 1
    return X / n


E = _norm(E)
P = _norm(P)
row2id = [None] * len(id2row)
for aid, r in id2row.items():
    row2id[r] = aid
