import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / 'sa.py'
spec = importlib.util.spec_from_file_location('sa', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_initial_menu_options_exist():
    assert hasattr(module, 'telaInicial')
    assert hasattr(module, 'telaPedido')
    assert hasattr(module, 'cardapioPao')
    assert hasattr(module, 'cardapioCarne')
    assert hasattr(module, 'cardapioSalada')
