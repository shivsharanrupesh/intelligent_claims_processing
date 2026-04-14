from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_process_claim():
    payload = {
        "claim_id": "CLM-1001",
        "policy_id": "POL-2001",
        "claim_type": "auto",
        "claim_subtype": "auto_glass",
        "customer_id": "CUS-7788",
        "incident_date": "2026-03-28",
        "reported_date": "2026-03-29",
        "claim_amount": 950.0,
        "currency": "CAD",
        "description": "Windshield cracked by road debris while driving on highway.",
        "attachments": [
            {
                "document_id": "DOC-1",
                "file_name": "invoice.pdf",
                "document_type": "invoice",
                "content": "Repair invoice from ABC Auto Glass, amount 950 CAD, service date 2026-03-28"
            },
            {
                "document_id": "DOC-2",
                "file_name": "claim_form.txt",
                "document_type": "claim_form",
                "content": "Customer states windshield damage occurred on highway."
            }
        ]
    }
    response = client.post("/claims/process", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["claim_id"] == "CLM-1001"
    assert data["policy_validation"]["active"] is True
    assert data["adjudication"]["recommendation"] in ["approve", "review", "reject"]
