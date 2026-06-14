# Spam Classifier API

## Construir imagen

```bash
docker build -t spam-api .
```

## Ejecutar

```bash
docker run --rm -p 8000:8000 spam-api
```

## Ejemplo

Entrada:

```json
{
  "text": "Win a free iPhone"
}
```

Salida:

```json
{
  "prediction": "spam"
}
```

## Puntos extra implementados

* [x] `.gitignore` configurado y sin secretos.
* [x] `.dockerignore` configurado.
* [x] Dockerfile con imagen base `python:3.12-slim`.
* [x] Tests automatizados con `pytest`.
* [x] Linting con `ruff`.
* [x] Imagen publicada en GHCR.
es posible ver la image con docker pull ghcr.io/yeimyhs/spam-api:latest
docker run --rm -p 8000:8000 ghcr.io/yeimyhs/spam-api:latest
* [ ] CI con GitHub Actions.
* [ ] Otras prácticas avanzadas (metrics, MLflow, Kubernetes).

### Tecnologías utilizadas

* FastAPI
* Docker
* scikit-learn
* pytest
* ruff
