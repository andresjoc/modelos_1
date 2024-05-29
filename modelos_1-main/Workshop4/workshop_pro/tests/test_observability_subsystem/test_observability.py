import pytest
from unittest.mock import mock_open, patch
from datetime import datetime
from workshop_pro.observability_subsystem.observability import Observability


class TestObservability:
    @patch(
        "workshop_pro.observability_subsystem.observability.open",
        new_callable=mock_open,
    )
    @patch("workshop_pro.observability_subsystem.observability.datetime")
    def test_write_user_log(self, mock_datetime, mock_file):
        mock_datetime.now.return_value = datetime(2024, 5, 29, 12, 0, 0)
        Observability.write_user_log("test_user", "Test message")

        mock_file.assert_called_once_with("user_log.txt", "a", encoding="utf-8")
        mock_file().write.assert_called_once_with(
            "2024-05-29 12:00:00 - User test_user: Test message\n"
        )

    @patch(
        "workshop_pro.observability_subsystem.observability.open",
        new_callable=mock_open,
    )
    @patch("workshop_pro.observability_subsystem.observability.datetime")
    def test_write_performance_log(self, mock_datetime, mock_file):
        mock_datetime.now.return_value = datetime(2024, 5, 29, 12, 0, 0)
        Observability.write_performance_log("Performance test message")

        mock_file.assert_called_once_with("performance_log.txt", "a", encoding="utf-8")
        mock_file().write.assert_called_once_with(
            "2024-05-29 12:00:00 - Performance test message\n"
        )


if __name__ == "__main__":
    pytest.main()
