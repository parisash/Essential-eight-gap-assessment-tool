# Essential Eight Gap Assessment Executive Report

## Overview

This report summarises a simulated Essential Eight maturity gap assessment.

The project demonstrates how an Australian cyber GRC workflow can assess current maturity, compare it with a target maturity level, identify evidence gaps and prioritise remediation actions.

The Essential Eight is a baseline set of mitigation strategies recommended by the Australian Cyber Security Centre to make it harder for adversaries to compromise systems.

## Key Metrics

| Metric | Value |
|---|---:|
| Total Essential Eight controls assessed | 8 |
| Controls below target maturity | 8 |
| Critical priority items | 1 |
| High priority items | 5 |
| Controls with missing evidence | 2 |
| Controls requiring governance attention | 6 |

## Priority Summary

| priority   |   control_count |
|:-----------|----------------:|
| High       |               5 |
| Medium     |               2 |
| Critical   |               1 |

## Remediation Status Summary

| status      |   control_count |
|:------------|----------------:|
| In Progress |               4 |
| Open        |               4 |

## Governance Attention Items

| control_id   | essential_eight_strategy           |   current_maturity |   target_maturity |   maturity_gap | priority   | status      | evidence_status   | owner                    | target_date   |
|:-------------|:-----------------------------------|-------------------:|------------------:|---------------:|:-----------|:------------|:------------------|:-------------------------|:--------------|
| E8-007       | Multi-Factor Authentication        |                  2 |                 3 |              1 | Critical   | Open        | Missing           | Identity and Access Team | 2026-07-08    |
| E8-002       | Patch Applications                 |                  1 |                 2 |              1 | High       | Open        | Missing           | Application Support Team | 2026-07-10    |
| E8-006       | Patch Operating Systems            |                  2 |                 3 |              1 | High       | Open        | Partial           | Infrastructure Team      | 2026-07-18    |
| E8-001       | Application Control                |                  1 |                 2 |              1 | High       | In Progress | Partial           | Endpoint Security Team   | 2026-07-15    |
| E8-005       | Restrict Administrative Privileges |                  1 |                 2 |              1 | High       | In Progress | Partial           | Identity and Access Team | 2026-07-12    |
| E8-008       | Regular Backups                    |                  1 |                 2 |              1 | High       | In Progress | Partial           | Infrastructure Team      | 2026-07-22    |

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
