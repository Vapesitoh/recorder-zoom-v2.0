from ...config.settings import RecordingSettings
from ..dto import StartRecordingResult
from ..recording_service import RecordingService


class StartRecordingUseCase:
    def __init__(self, recording_service=None):
        self.recording_service = recording_service or RecordingService()

    def execute(self, settings: RecordingSettings) -> StartRecordingResult:
        return self.recording_service.start_recording(settings)
