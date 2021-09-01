from ..strings import clean

def test_clean_spaces_line_jump():
  assert clean('\n\nhello world  \n') == 'hello world'

def test_clean_and_replace():
  assert clean('\n\nhello world% \n', {'%': ''}) == 'hello world'