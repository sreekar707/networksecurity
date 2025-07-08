from dataclasses import dataclass
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
    
class DataValidationArtifact:
    validation_status:bool
    validation_train_file_path:str
    validation_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str