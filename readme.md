# 📰 News Recommendation MVP

This repository contains a **content-based news recommendation system**, developed as part of an AI engineering project.
The goal is to deliver a **fully functional MVP** combining:

- an **Azure Function API** (for serving recommendations), and
- a **Streamlit front-end** (for interactive demo).

---

## 🚀 Overview

The recommender suggests articles based on **cosine similarity** between:

- user profiles (weighted mean of embeddings of previously read articles), and
- article embeddings (vector representations derived from content).

When no user history is available, the system falls back to a **popularity/recentness list**.

---

## 🧱 Repository Structure

| Path / Folder                                                                      | Description                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`exploration_notebooks/`** _(e.g. `explo.ipynb`, `first.ipynb`, `second.ipynb`)_ | Jupyter notebooks used for **data exploration**, **PCA analysis**, and **artifact creation** (embeddings, user profiles, mappings).                                                                                                                                                                                             |
| **`artifacts/`**                                                                   | Folder containing all **precomputed artifacts** used by the API: <br>• `embeddings_clean.npy` – article embeddings <br>• `user_profiles.npy` – user profile vectors <br>• `id_to_row.json` – mapping article_id → index <br>• `user_to_idx.json` – mapping user_id → index <br>• `cold_start_top5.json` – fallback article list |
| **`function_app.py`**                                                              | Azure Function entrypoint exposing the `/recommend` endpoint (GET/POST).                                                                                                                                                                                                                                                        |
| **`recommender.py`**                                                               | Core recommendation logic: computes cosine similarity between user and article embeddings; handles cold-start.                                                                                                                                                                                                                  |
| **`shared.py`**                                                                    | Loads artifacts from the `artifacts/` folder, normalizes vectors, and creates index maps.                                                                                                                                                                                                                                       |
| **`streamlit_app/app.py`**                                                         | Streamlit interface for the demo — connects to the Azure Function API using an environment variable key.                                                                                                                                                                                                                        |
| **`requirements.txt`**                                                             | Python dependencies for both the Azure Function and the Streamlit app.                                                                                                                                                                                                                                                          |
| **`.github/workflows/deploy.yml`**                                                 | Optional CI/CD configuration for Azure deployment.                                                                                                                                                                                                                                                                              |

---

## 🔐 Security & Deployment

- Azure Function configured with `AuthLevel=Function`.
- The access key is stored in `AZ_RECO_SECRET` (environment variable) and passed from Streamlit when calling the API.
- The demo runs on a **low-cost App Service plan (F1/B1)**.
- Optional monitoring via **Azure Application Insights**.

---

## 🧩 Roadmap

1. **Functional MVP** – cosine similarity recommender (current version).
2. **Persistence & robustness** – move embeddings to a persistent vector index (FAISS / Azure Cognitive Search).
3. **Dynamic ingestion** – automate article updates and profile recomputation.
4. **Monitoring & scalability** – add logging, usage metrics, and stress tests.
5. **Post-demo improvements** – explore sequence-based (NAR) or hybrid re-ranking models.

---
