from datetime import date

import pytest

import fechautil


def test_parse_iso():
    assert fechautil.parse("2026-10-05") == date(2026, 10, 5)


def test_parse_latino():
    assert fechautil.parse("5/10/2026") == date(2026, 10, 5)


def test_parse_invalido():
    with pytest.raises(ValueError):
        fechautil.parse("mañana")


def test_formato_largo():
    assert fechautil.formato_largo(date(2026, 10, 5)) == "5 de octubre de 2026"
