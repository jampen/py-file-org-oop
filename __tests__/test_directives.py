from src.directives import Directives

VALID_DIRECTIVE_PATH = 'valid_directive.json'
INVALID_DIRECTIVE_PATH = 'invalid_directive.json'


def test_load_returns_true_on_invalid_directives():
    directives = Directives()
    assert directives.load(VALID_DIRECTIVE_PATH) == True


def test_load_returns_false_on_invalid_directives():
    directives = Directives()
    assert directives.load(INVALID_DIRECTIVE_PATH) == False


def test_ext_to_category_returns_associated_category():
    directives = Directives()
    assert directives.load(VALID_DIRECTIVE_PATH)
    assert directives.ext_to_category('png') == 'images'
    assert directives.ext_to_category('jpeg') == 'images'
    assert directives.ext_to_category('gif') == 'images'
