from unittest.mock import MagicMock
from workshop_pro.engines_subsystem import Engine, EnginesFacade
from workshop_pro.vehicles_subsystem.engines_flyweight import EngineFlyweight


class TestEngineFlyweight:
    def test_get_engine_existing(self):
        engine_mock = MagicMock(spec=Engine)
        EnginesFacade.get_engine = MagicMock(return_value=engine_mock)

        flyweight = EngineFlyweight()
        engine1 = flyweight.get_engine("gasoline", 2000)
        engine2 = flyweight.get_engine("gasoline", 2000)

        assert engine1 is engine2
        EnginesFacade.get_engine.assert_called_once_with("gasoline", 2000)

    def test_get_engine_new_type(self):
        engine_mock = MagicMock(spec=Engine)
        EnginesFacade.get_engine = MagicMock(return_value=engine_mock)

        flyweight = EngineFlyweight()
        engine1 = flyweight.get_engine("diesel", 2500)
        engine2 = flyweight.get_engine("diesel", 2500)

        assert engine1 is engine2
        EnginesFacade.get_engine.assert_called_once_with("diesel", 2500)

    def test_get_engine_new_price(self):
        engine_mock_1 = MagicMock(spec=Engine)
        engine_mock_1.price = 3000
        engine_mock_2 = MagicMock(spec=Engine)
        engine_mock_2.price = 3500
        EnginesFacade.get_engine = MagicMock(side_effect=[engine_mock_1, engine_mock_2])

        flyweight = EngineFlyweight()
        engine1 = flyweight.get_engine("electric", 3000)
        engine2 = flyweight.get_engine("electric", 3500)

        assert engine1 != engine2
        assert engine1.price == 3000
        assert engine2.price == 3500
        EnginesFacade.get_engine.assert_any_call("electric", 3000)
        EnginesFacade.get_engine.assert_any_call("electric", 3500)
