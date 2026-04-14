from app.models.schemas import ClaimRequest
from app.services.ocr_service import OCRService
from app.services.classification_service import ClassificationService
from app.services.policy_service import PolicyService
from app.services.fraud_service import FraudService
from app.services.adjudication_service import AdjudicationService

class ClaimsTools:
    def __init__(self) -> None:
        self.ocr_service = OCRService()
        self.classification_service = ClassificationService()
        self.policy_service = PolicyService()
        self.fraud_service = FraudService()
        self.adjudication_service = AdjudicationService()

    def intake_tool(self, claim: ClaimRequest) -> dict:
        return {
            "claim_id": claim.claim_id,
            "policy_id": claim.policy_id,
            "attachments_count": len(claim.attachments),
            "claim_amount": claim.claim_amount,
            "status": "validated"
        }

    def ocr_tool(self, claim: ClaimRequest):
        return self.ocr_service.extract(claim.attachments)

    def classify_tool(self, claim: ClaimRequest):
        return self.classification_service.classify(claim)

    def policy_tool(self, claim: ClaimRequest):
        return self.policy_service.validate(claim)

    def fraud_tool(self, claim: ClaimRequest, ocr_results):
        return self.fraud_service.assess(claim, ocr_results)

    def adjudication_tool(self, claim: ClaimRequest, policy_result, fraud_result):
        return self.adjudication_service.recommend(claim, policy_result, fraud_result)
