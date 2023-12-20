from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_data_file: Path
    source_info_file: Path
    local_data_name: str

@dataclass(frozen=True)
class DataVisualizationConfig:
    root_dir: Path
    data_file_path: Path
    info_file_path: Path

@dataclass(frozen=True)
class PromptGenerationConfig:
    root_dir: Path
    data_path: Path
    visualization_path: Path
    data_information_file: Path