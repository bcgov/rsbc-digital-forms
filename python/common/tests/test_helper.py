import pytest
from python.common.helper import str_to_integer


class TestStrToInteger:
    """Test cases for str_to_integer function"""

    def test_str_to_integer_valid_positive_number(self):
        """Test str_to_integer with valid positive number string"""
        result = str_to_integer("123")
        assert result == 123

    def test_str_to_integer_valid_negative_number(self):
        """Test str_to_integer with valid negative number string"""
        result = str_to_integer("-456")
        assert result == -456

    def test_str_to_integer_valid_zero(self):
        """Test str_to_integer with zero string"""
        result = str_to_integer("0")
        assert result == 0

    def test_str_to_integer_valid_large_number(self):
        """Test str_to_integer with large number string"""
        result = str_to_integer("999999999")
        assert result == 999999999

    def test_str_to_integer_none_value(self):
        """Test str_to_integer with None value"""
        result = str_to_integer(None)
        assert result is None

    def test_str_to_integer_empty_string(self):
        """Test str_to_integer with empty string"""
        result = str_to_integer("")
        assert result is None

    def test_str_to_integer_whitespace_string(self):
        """Test str_to_integer with whitespace string"""
        result = str_to_integer("   ")
        assert result is None

    def test_str_to_integer_invalid_alphabetic_string(self):
        """Test str_to_integer with alphabetic string"""
        result = str_to_integer("abc")
        assert result is None

    def test_str_to_integer_invalid_alphanumeric_string(self):
        """Test str_to_integer with alphanumeric string"""
        result = str_to_integer("123abc")
        assert result is None

    def test_str_to_integer_invalid_special_characters(self):
        """Test str_to_integer with special characters"""
        result = str_to_integer("!@#$%")
        assert result is None

    def test_str_to_integer_decimal_number(self):
        """Test str_to_integer with decimal number string"""
        result = str_to_integer("123.45")
        assert result is None

    def test_str_to_integer_float_string(self):
        """Test str_to_integer with float string"""
        result = str_to_integer("123.0")
        assert result is None

    def test_str_to_integer_number_with_spaces(self):
        """Test str_to_integer with number containing spaces"""
        result = str_to_integer("1 2 3")
        assert result is None

    def test_str_to_integer_leading_zeros(self):
        """Test str_to_integer with leading zeros"""
        result = str_to_integer("000123")
        assert result == 123

    def test_str_to_integer_negative_zero(self):
        """Test str_to_integer with negative zero"""
        result = str_to_integer("-0")
        assert result == 0

    def test_str_to_integer_plus_sign_positive(self):
        """Test str_to_integer with explicit plus sign"""
        result = str_to_integer("+123")
        assert result == 123

    def test_str_to_integer_scientific_notation(self):
        """Test str_to_integer with scientific notation"""
        result = str_to_integer("1e3")
        assert result is None

    def test_str_to_integer_hexadecimal(self):
        """Test str_to_integer with hexadecimal string"""
        result = str_to_integer("0xFF")
        assert result is None

    def test_str_to_integer_octal(self):
        """Test str_to_integer with octal string"""
        result = str_to_integer("0o123")
        assert result is None

    def test_str_to_integer_binary(self):
        """Test str_to_integer with binary string"""
        result = str_to_integer("0b101")
        assert result is None

    def test_str_to_integer_leading_whitespace(self):
        """Test str_to_integer with leading whitespace"""
        result = str_to_integer("  123")
        assert result == 123

    def test_str_to_integer_trailing_whitespace(self):
        """Test str_to_integer with trailing whitespace"""
        result = str_to_integer("123  ")
        assert result == 123

    def test_str_to_integer_mixed_case_invalid(self):
        """Test str_to_integer with mixed case letters"""
        result = str_to_integer("AbC123")
        assert result is None

    def test_str_to_integer_unicode_numbers(self):
        """Test str_to_integer with unicode number characters"""
        result = str_to_integer("①②③")
        assert result is None

    def test_str_to_integer_roman_numerals(self):
        """Test str_to_integer with roman numerals"""
        result = str_to_integer("XII")
        assert result is None

    def test_str_to_integer_infinity(self):
        """Test str_to_integer with infinity string"""
        result = str_to_integer("inf")
        assert result is None

    def test_str_to_integer_nan(self):
        """Test str_to_integer with NaN string"""
        result = str_to_integer("nan")
        assert result is None

    def test_str_to_integer_very_large_number(self):
        """Test str_to_integer with very large number that fits in int"""
        large_number = "9" * 15  # 15 nines
        result = str_to_integer(large_number)
        assert result == int(large_number)

    def test_str_to_integer_negative_large_number(self):
        """Test str_to_integer with very large negative number"""
        large_negative = "-" + "9" * 15
        result = str_to_integer(large_negative)
        assert result == int(large_negative)

    @pytest.mark.parametrize("test_input,expected", [
        ("0", 0),
        ("1", 1),
        ("-1", -1),
        ("100", 100),
        ("-100", -100),
        ("999", 999),
        ("+42", 42),
        ("007", 7),
        (None, None),
        ("", None),
        ("abc", None),
        ("12.3", None),
        ("12 3", None),
        (" 123", 123),
        ("123 ", 123),
    ])
    def test_str_to_integer_parametrized(self, test_input, expected):
        """Parametrized test for str_to_integer function"""
        result = str_to_integer(test_input)
        assert result == expected

    def test_str_to_integer_type_validation(self):
        """Test that str_to_integer returns correct types"""
        # Valid conversion should return int
        result = str_to_integer("123")
        assert isinstance(result, int)
        assert result == 123
        
        # Invalid conversion should return None
        result = str_to_integer("abc")
        assert result is None
        
        # None input should return None
        result = str_to_integer(None)
        assert result is None