from src.directives import Directives

VALID_DIRECTIVE_PATH = 'valid_directive.json'
INVALID_DIRECTIVE_PATH = 'invalid_directive.json'


def test_load_returns_true_on_invalid_directives():
    directives = Directives()
    assert directives.load(VALID_DIRECTIVE_PATH)


def test_load_returns_false_on_invalid_directives():
    directives = Directives()
    assert not directives.load(INVALID_DIRECTIVE_PATH)


def test_ext_to_category_returns_associated_category():
    directives = Directives()
    assert directives.load(VALID_DIRECTIVE_PATH)
    assert directives.ext_to_category('png') == 'images'
    assert directives.ext_to_category('jpeg') == 'images'
    assert directives.ext_to_category('gif') == 'images'


def test_is_visitable_folder_returns_true_on_visitable_folder():
    directives = Directives()
    assert directives.load(VALID_DIRECTIVE_PATH)
    assert directives.is_visitable_folder('myfolder/')


def test_is_visitable_folder_returns_true_on_non_visitable_folder():
    directives = Directives()
    assert directives.load(VALID_DIRECTIVE_PATH)
    assert not directives.is_visitable_folder('invalid_path/')
