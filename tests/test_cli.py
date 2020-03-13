from dosym import cli

def test_parser():
    p = cli.create_parser(optional=[])
    assert p.debug == False
    assert p.force == False
    assert p.files == []
    assert p.generate_config == False
    assert p.version == False

def test_debug_mode():
    class DebugEnabled:
        debug = True

    class DebugDisabled:
        debug = False

    enabled = cli.check_debug_mode(DebugEnabled)
    disabled = cli.check_debug_mode(DebugDisabled)
    assert enabled == True
    assert disabled == False


