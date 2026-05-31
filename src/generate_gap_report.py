from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

ASSESSMENT_FILE = DATA_DIR / "essential_eight_assessment.csv"
EVIDENCE_FILE = DATA_DIR / "evidence_requirements.csv"

OUTPUT_COMBINED_FILE = REPORTS_DIR / "essential_eight_gap_register.csv"
OUTPUT_REPORT_FILE = REPORTS_DIR / "essential_eight_executive_report.md"


PRIORITY_SCORE = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Critical": 4,
}

STATUS_SCORE = {
    "Closed": 0,
    "In Progress": 1,
    "Open": 2,
}

EVIDENCE_SCORE = {
    "Strong": 1,
    "Medium": 2,
    "Weak": 3,
}


def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")
    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame, required_columns: list[str], file_name: str) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"{file_name} is missing required columns: {', '.join(missing)}")


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    assessment = load_csv(ASSESSMENT_FILE)
    evidence = load_csv(EVIDENCE_FILE)

    validate_columns(
        assessment,
        [
            "control_id",
            "essential_eight_strategy",
            "current_maturity",
            "target_maturity",
            "current_state",
            "gap_summary",
            "business_risk",
            "owner",
            "remediation_action",
            "priority",
            "status",
            "target_date",
        ],
        "essential_eight_assessment.csv",
    )

    validate_columns(
        evidence,
        [
            "control_id",
            "evidence_area",
            "evidence_required",
            "evidence_status",
            "evidence_quality",
            "review_notes",
        ],
        "evidence_requirements.csv",
    )

    return assessment, evidence


def build_gap_register(assessment: pd.DataFrame, evidence: pd.DataFrame) -> pd.DataFrame:
    combined = assessment.merge(evidence, on="control_id", how="left")

    combined["maturity_gap"] = combined["target_maturity"] - combined["current_maturity"]

    combined["priority_score"] = combined["priority"].map(PRIORITY_SCORE).fillna(1).astype(int)
    combined["status_score"] = combined["status"].map(STATUS_SCORE).fillna(1).astype(int)
    combined["evidence_score"] = combined["evidence_quality"].map(EVIDENCE_SCORE).fillna(2).astype(int)

    combined["gap_risk_score"] = (
        combined["maturity_gap"]
        + combined["priority_score"]
        + combined["status_score"]
        + combined["evidence_score"]
    )

    combined["governance_attention_required"] = combined.apply(
        lambda row: "Yes"
        if row["maturity_gap"] > 0
        and (row["priority"] in ["High", "Critical"] or row["evidence_status"] == "Missing")
        else "No",
        axis=1,
    )

    return combined.sort_values(by="gap_risk_score", ascending=False)


def markdown_table(df: pd.DataFrame, columns: list[str]) -> str:
    if df.empty:
        return "No records found."
    return df[columns].to_markdown(index=False)


def generate_report(gap_register: pd.DataFrame) -> str:
    total_controls = gap_register["control_id"].nunique()
    controls_below_target = gap_register[gap_register["maturity_gap"] > 0]["control_id"].nunique()
    critical_items = gap_register[gap_register["priority"] == "Critical"]["control_id"].nunique()
    high_items = gap_register[gap_register["priority"] == "High"]["control_id"].nunique()
    missing_evidence = gap_register[gap_register["evidence_status"] == "Missing"]["control_id"].nunique()
    governance_attention = gap_register[
        gap_register["governance_attention_required"] == "Yes"
    ]["control_id"].nunique()

    priority_summary = (
        gap_register.groupby("priority")["control_id"]
        .nunique()
        .reset_index(name="control_count")
        .sort_values(by="control_count", ascending=False)
    )

    status_summary = (
        gap_register.groupby("status")["control_id"]
        .nunique()
        .reset_index(name="control_count")
        .sort_values(by="control_count", ascending=False)
    )

    attention_items = gap_register[
        gap_register["governance_attention_required"] == "Yes"
    ].copy()

    report = f"""# Essential Eight Gap Assessment Executive Report

## Overview

This report summarises a simulated Essential Eight maturity gap assessment.

The project demonstrates how an Australian cyber GRC workflow can assess current maturity, compare it with a target maturity level, identify evidence gaps and prioritise remediation actions.

The Essential Eight is a baseline set of mitigation strategies recommended by the Australian Cyber Security Centre to make it harder for adversaries to compromise systems.

## Key Metrics

| Metric | Value |
|---|---:|
| Total Essential Eight controls assessed | {total_controls} |
| Controls below target maturity | {controls_below_target} |
| Critical priority items | {critical_items} |
| High priority items | {high_items} |
| Controls with missing evidence | {missing_evidence} |
| Controls requiring governance attention | {governance_attention} |

## Priority Summary

{markdown_table(priority_summary, ["priority", "control_count"])}

## Remediation Status Summary

{markdown_table(status_summary, ["status", "control_count"])}

## Governance Attention Items

{markdown_table(
        attention_items,
        [
            "control_id",
            "essential_eight_strategy",
            "current_maturity",
            "target_maturity",
            "maturity_gap",
            "priority",
            "status",
            "evidence_status",
            "owner",
            "target_date",
        ],
    )}

## GRC Interpretation

The highest-priority items are controls that remain below the target maturity level and have either high business risk, critical remediation priority or missing evidence.

These gaps may create audit-readiness issues, reduce confidence in security control effectiveness and increase exposure to common cyber threats.

## Recommended Actions

1. Prioritise controls with Critical and High priority ratings.
2. Address missing evidence before assessment or audit review.
3. Confirm accountable owners for each remediation action.
4. Track maturity uplift from current level to target level.
5. Validate closure evidence before marking items as complete.
6. Reassess Essential Eight maturity after remediation.

## Disclaimer

This project uses simulated Essential Eight assessment data for portfolio and learning purposes. It does not represent an official compliance assessment and does not contain real client, employer or confidential security data.
"""
    return report


def save_outputs(gap_register: pd.DataFrame, report: str) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    gap_register.to_csv(OUTPUT_COMBINED_FILE, index=False)
    OUTPUT_REPORT_FILE.write_text(report, encoding="utf-8")

    print("Essential Eight gap assessment report generated successfully.")
    print(f"- {OUTPUT_COMBINED_FILE}")
    print(f"- {OUTPUT_REPORT_FILE}")


def main() -> None:
    assessment, evidence = load_data()
    gap_register = build_gap_register(assessment, evidence)
    report = generate_report(gap_register)
    save_outputs(gap_register, report)


if __name__ == "__main__":
    main()
