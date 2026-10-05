"""fechautil: utilidades mínimas para fechas en español."""
from __future__ import annotations

import re
from datetime import date

__version__ = "1.0.0"

_MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def parse(texto: str) -> date:
    """Convierte 'AAAA-MM-DD' o 'DD/MM/AAAA' en un objeto date."""
    texto = texto.strip()

    iso = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", texto)
    if iso:
        return date(int(iso[1]), int(iso[2]), int(iso[3]))

    latino = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", texto)
    if latino:
        return date(int(latino[3]), int(latino[2]), int(latino[1]))

    raise ValueError(f"Formato de fecha no reconocido: {texto!r}")


def formato_largo(fecha: date) -> str:
    """Devuelve la fecha como '5 de octubre de 2026'."""
    return f"{fecha.day} de {_MESES[fecha.month - 1]} de {fecha.year}"
