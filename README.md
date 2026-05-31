# Essential Eight Gap Assessment Tool

An Australia-focused cybersecurity GRC project that assesses Essential Eight maturity gaps, remediation priorities, evidence requirements and executive-ready reporting.

This project demonstrates how cyber security control assessment data can be translated into a practical governance workflow for identifying maturity gaps, evidence weaknesses, remediation priorities and audit-readiness issues.

## Project Summary

The **Essential Eight** is a set of baseline cyber security mitigation strategies recommended by the Australian Cyber Security Centre to help organisations reduce the risk of cyber compromise.

This project uses simulated data to demonstrate how an organisation can assess its Essential Eight maturity position and produce governance-ready outputs for security, risk, compliance and executive stakeholders.

The workflow connects:

```text
Essential Eight Assessment → Evidence Review → Gap Analysis → Remediation Priority → Executive Report
```

## Why This Project Matters

For cybersecurity GRC, information security and security assurance roles in Australia, the Essential Eight is highly relevant because it provides a practical baseline for improving cyber resilience.

A maturity assessment is only useful when it clearly shows:

* Current maturity level
* Target maturity level
* Control gaps
* Evidence gaps
* Responsible owners
* Remediation priorities
* Target dates
* Governance attention items
* Executive-level risk implications

This project demonstrates how those elements can be structured, assessed and reported using a simple Python-based workflow.

## Key Features

* Essential Eight maturity assessment dataset
* Current vs target maturity comparison
* Maturity gap calculation
* Evidence requirements register
* Evidence quality review
* Remediation priority scoring
* Governance attention flagging
* Python-generated gap register
* Executive-ready Markdown report
* Audit-readiness focused reporting

## Repository Structure

```text
essential-eight-gap-assessment-tool/
│
├── data/
│   ├── essential_eight_assessment.csv
│   └── evidence_requirements.csv
│
├── src/
│   └── generate_gap_report.py
│
├── reports/
│   ├── essential_eight_gap_register.csv
│   └── essential_eight_executive_report.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Input Files

### `data/essential_eight_assessment.csv`

Contains simulated maturity assessment data for the eight Essential Eight mitigation strategies:

* Application Control
* Patch Applications
* Configure Microsoft Office Macro Settings
* User Application Hardening
* Restrict Administrative Privileges
* Patch Operating Systems
* Multi-Factor Authentication
* Regular Backups

Each record includes:

* Control ID
* Essential Eight strategy
* Current maturity
* Target maturity
* Current state
* Gap summary
* Business risk
* Control owner
* Remediation action
* Priority
* Status
* Target date

### `data/evidence_requirements.csv`

Tracks evidence expectations for each strategy.

Each record includes:

* Control ID
* Evidence area
* Evidence required
* Evidence status
* Evidence quality
* Review notes

This helps show whether a control is not only implemented, but also supported by reviewable evidence.

## Generated Outputs

Running the Python script generates two portfolio-ready outputs.

### `reports/essential_eight_gap_register.csv`

A structured gap register that combines maturity assessment data with evidence requirements.

It includes:

* Current maturity
* Target maturity
* Maturity gap
* Priority score
* Evidence score
* Gap risk score
* Governance attention flag

### `reports/essential_eight_executive_report.md`

An executive-style report that summarises:

* Total controls assessed
* Controls below target maturity
* Critical and high priority items
* Missing evidence items
* Governance attention items
* Remediation status
* Recommended actions

## How the Assessment Logic Works

The script calculates the maturity gap using:

```text
Maturity Gap = Target Maturity - Current Maturity
```

It then assigns a simple gap risk score using maturity gap, remediation priority, status and evidence quality.

The project also flags governance attention items where a control is below the target maturity level and has either high/critical priority or missing evidence.

Example logic:

```text
Below Target Maturity + High Priority = Governance Attention Required
Below Target Maturity + Missing Evidence = Governance Attention Required
```

## Example Workflow

```text
Essential Eight Assessment Data
        ↓
Evidence Requirements Register
        ↓
Python Gap Analysis Script
        ↓
Combined Gap Register
        ↓
Executive Summary Report
```

## How to Run

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run the report generator:

```bash
py src/generate_gap_report.py
```

Check generated reports:

```bash
dir reports
```

Expected outputs:

```text
essential_eight_gap_register.csv
essential_eight_executive_report.md
```

## Example Governance Questions Answered

This project helps answer questions such as:

* Which Essential Eight strategies are below target maturity?
* Which controls require urgent governance attention?
* Where is evidence missing or weak?
* Which remediation actions are still open?
* Who owns each remediation action?
* Which gaps create the strongest audit-readiness concern?
* What should be prioritised for maturity uplift?

## Skills Demonstrated

This project demonstrates practical capability in:

* Cybersecurity GRC
* Essential Eight maturity assessment
* Security control gap analysis
* Evidence requirement tracking
* Remediation prioritisation
* Audit-readiness reporting
* Governance attention flagging
* Risk-based security reporting
* Python reporting automation
* Executive security communication
* Australia-focused cyber security governance

## Career Relevance

This project aligns with roles such as:

* Cybersecurity GRC Analyst
* Cybersecurity Analyst
* Information Security Analyst
* Security Governance Analyst
* Risk and Compliance Analyst
* Security Assurance Analyst
* Cloud Security Governance Analyst
* Data Privacy and Security Analyst

## Practical Value

This project shows how a recognised Australian cyber security framework can be translated into a repeatable governance workflow.

It demonstrates the ability to:

* Interpret control expectations
* Structure assessment data
* Identify maturity gaps
* Link evidence to control status
* Prioritise remediation
* Communicate findings clearly to stakeholders
* Produce audit-ready reporting outputs

## Future Improvements

Planned improvements include:

* Add Streamlit dashboard
* Add maturity heatmap
* Add remediation SLA tracking
* Add overdue remediation flagging
* Add evidence expiry dates
* Add ISO 27001 and NIST CSF mapping
* Add Power BI-ready output
* Add screenshots of the generated report
* Add sample executive dashboard visuals
* Add exportable management action plan

## Disclaimer

This project uses simulated Essential Eight assessment data for portfolio and learning purposes. It is not an official Essential Eight assessment and does not contain real client, employer, security, privacy, audit or confidential organisational data.

## Author

**Parisa Shojaei**

Cybersecurity GRC · Cloud Security · Privacy Governance · Risk Analytics · AI Assurance
Python · SQL · AWS · Jira
