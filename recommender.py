import json, numpy as np
import shared as S


def _k_int(v):
    try:
        return max(1, int(v))
    except:
        return 5


def recommend_items(uid, k="5"):
    if not uid:
        return False, '{"error":"user_id required"}', 400
    k = _k_int(k)
    uidx = S.user2idx.get(str(uid))
    if uidx is None:
        return True, json.dumps({"items": S.cold[:k]}), 200
    scores = S.P[uidx] @ (S.ET if hasattr(S, "ET") else S.E.T)
    k = min(k, scores.size)
    top = np.argpartition(-scores, k - 1)[:k]
    top = top[np.argsort(-scores[top])]
    items = [S.row2id[i] for i in top]
    return True, json.dumps({"items": items}), 200
