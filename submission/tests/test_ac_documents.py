from src.docs.applicability import applicable_documents


def test_ac010_k998_k999_quarantined():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    for doc_id in ("K-998", "K-999"):
        assert docs[doc_id]["instruction_applicable"] is False
        assert docs[doc_id]["quarantined"] is True


def test_ac011_k006_yes_k007_no():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    assert docs["K-006"]["instruction_applicable"] is True
    assert docs["K-007"]["instruction_applicable"] is False


def test_ac012_k026_draft_not_instruction():
    docs = {d["doc_id"]: d for d in applicable_documents()}
    assert docs["K-026"]["instruction_applicable"] is False
    assert docs["K-026"]["status"] == "draft"
