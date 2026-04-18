from ...recorder import FocusRecorder
from ..dto import StopRecordingResult
from ..recording_service import RecordingService


class StopRecordingUseCase:
    def __init__(self, recording_service=None):
        self.recording_service = recording_service or RecordingService()

    def execute(
        self,
        recorder: FocusRecorder,
        *,
        callback_progress=None,
        export_mode="full",
    ) -> StopRecordingResult:
        return self.recording_service.stop_recording(
            recorder,
            callback_progress=callback_progress,
            export_mode=export_mode,
        )

