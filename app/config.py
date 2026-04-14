from dataclasses import dataclass
import os

@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "Intelligent Claims Processing")
    env: str = os.getenv("ENV", "dev")
    auto_approval_max_amount: float = float(os.getenv("AUTO_APPROVAL_MAX_AMOUNT", "1500"))
    fraud_review_threshold: float = float(os.getenv("FRAUD_REVIEW_THRESHOLD", "0.65"))
    high_confidence_threshold: float = float(os.getenv("HIGH_CONFIDENCE_THRESHOLD", "0.80"))
    policy_default_deductible: float = float(os.getenv("POLICY_DEFAULT_DEDUCTIBLE", "500"))

settings = Settings()
