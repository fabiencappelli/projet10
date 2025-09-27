import azure.functions as func
from azure.functions import HttpRequest, HttpResponse
from recommender import recommend_items

app = func.FunctionApp()


@app.route(
    route="recommend", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS
)
def recommend(req: HttpRequest) -> HttpResponse:
    uid = req.params.get("user_id") or (req.get_json(silent=True) or {}).get("user_id")
    k = req.params.get("k", "5")
    ok, payload, code = recommend_items(uid, k)
    return HttpResponse(payload, status_code=code, mimetype="application/json")
