# fechautil

Librería mínima para fechas en español. Existe como **laboratorio** para
[Pipeline Doctor](https://github.com/maikadevops-labs/pipeline-doctor): es la
dependencia que "funciona ayer y hoy ya no" en el paciente 1 de la demo.

```python
import fechautil

fecha = fechautil.parse("2026-10-05")
print(fechautil.formato_largo(fecha))  # 5 de octubre de 2026
```

## Instalación

```bash
pip install "fechautil @ git+https://github.com/maikadevops-labs/fechautil.git"
```

## Pruebas

```bash
pip install pytest
pip install -e .
pytest -q
```

## Licencia

MIT
