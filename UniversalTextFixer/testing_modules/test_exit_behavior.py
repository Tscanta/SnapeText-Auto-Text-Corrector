import threading

from src.hotkeys import shutdown_app


def test_shutdown_app_sets_event_and_calls_callback():
    stop_event = threading.Event()
    called = []

    shutdown_app(stop_event, lambda: called.append("stopped"))

    assert stop_event.is_set()
    assert called == ["stopped"]
