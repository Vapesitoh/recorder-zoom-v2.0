from unittest.mock import MagicMock
from focusrecorder.main import RenderThread


def test_render_thread_full_mode_emits_paths(qtbot):
    recorder = MagicMock()
    recorder.is_recording = True

    service = MagicMock()
    service.stop_recording.return_value = {
        "full_path": "C:/tmp/res.mp4",
        "tiktok_path": ""
    }

    thread = RenderThread(service, recorder, export_mode="full")

    finished_payload = []
    thread.finished.connect(lambda full, tiktok: finished_payload.append((full, tiktok)))

    thread.run()

    assert finished_payload == [("C:/tmp/res.mp4", "")]


def test_render_thread_both_mode_emits_both_paths(qtbot):
    recorder = MagicMock()
    recorder.is_recording = True

    service = MagicMock()
    service.stop_recording.return_value = {
        "full_path": "C:/tmp/res.mp4",
        "tiktok_path": "C:/tmp/res_tiktok.mp4"
    }

    thread = RenderThread(service, recorder, export_mode="both")

    finished_payload = []
    thread.finished.connect(lambda full, tiktok: finished_payload.append((full, tiktok)))

    thread.run()

    assert finished_payload == [("C:/tmp/res.mp4", "C:/tmp/res_tiktok.mp4")]

