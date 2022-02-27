from ..strings import clean, get_first_number

def test_clean_spaces_line_jump():
  assert clean('\n\nhello world  \n') == 'hello world'

def test_clean_and_replace():
  assert clean('\n\nhello world% \n', {'%': ''}) == 'hello world'

def test_get_first_number_when_exists():
    assert get_first_number("hello 1 23 world") == '1'

def test_get_first_number_when_empty():
    assert get_first_number("hello world") == ''