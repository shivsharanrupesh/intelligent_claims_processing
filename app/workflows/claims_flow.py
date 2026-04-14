from app.models.schemas import ClaimRequest, ProcessedClaimResponse
from app.agents.crew import ClaimsCrew
from app.services.storage_service import StorageService

class ClaimsProcessingFlow:
    # Controller/orchestration layer.

    def __init__(self) -> None:
        self.storage = StorageService()
        self.crew = ClaimsCrew()

    def process(self, claim: ClaimRequest) -> ProcessedClaimResponse:
        self.storage.persist_claim(claim)
        results = self.crew.run(claim)

        adjudication = results["adjudication_result"]
        fraud = results["fraud_result"]
        policy = results["policy_result"]
        ocr_results = results["ocr_results"]

        audit_summary = (
            f"Claim {claim.claim_id} processed. "
            f"Recommendation={adjudication.recommendation}; "
            f"FraudScore={fraud.score:.2f}; "
            f"CoverageApplicable={policy.coverage_applicable}; "
            f"HumanReview={adjudication.human_review_required}"
        )

        return ProcessedClaimResponse(
            claim_id=claim.claim_id,
            policy_validation=policy,
            fraud_assessment=fraud,
            adjudication=adjudication,
            ocr_results=ocr_results,
            audit_summary=audit_summary,
        )
