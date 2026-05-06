import pytest

from pyparsing import QuotedString


def test_quote_char_leading_trailing_spaces_stripped():
    """Accidental spaces around quote_char should be cleaned up"""
    qs = QuotedString("  ;  ")
    assert qs.quote_char == ";"


def test_quote_char_leading_trailing_tabs_stripped():
    """Accidental tabs around quote_char should be cleaned up"""
    qs = QuotedString("\t;\t")
    assert qs.quote_char == ";"


def test_quote_char_newline_preserved():
    """Intentional newline in quote_char should not be stripped"""
    qs = QuotedString("\n;", multiline=True)
    assert qs.quote_char == "\n;"


def test_end_quote_char_leading_trailing_spaces_stripped():
    """Accidental spaces around end_quote_char should be cleaned up"""
    qs = QuotedString("{", end_quote_char="  }  ")
    assert qs.end_quote_char == "}"


def test_end_quote_char_newline_preserved():
    """Intentional newline in end_quote_char should not be stripped"""
    qs = QuotedString(";", end_quote_char=";\n")
    assert qs.end_quote_char == ";\n"


def test_whitespace_only_quote_char_raises():
    """A quote_char of only spaces/tabs should still raise ValueError"""
    with pytest.raises(ValueError, match="quote_char cannot be the empty string"):
        QuotedString("   ")


def test_whitespace_only_end_quote_char_raises():
    """An end_quote_char of only spaces/tabs should still raise ValueError"""
    with pytest.raises(ValueError, match="end_quote_char cannot be the empty string"):
        QuotedString("{", end_quote_char="   ")