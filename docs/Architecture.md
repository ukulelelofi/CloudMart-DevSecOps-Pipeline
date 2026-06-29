</> Markdown

# CloudMart Solutions - DevSecOps Architecture

## Project Overview

CloudMart Solutions is a growing digital commerce company that wants to improve software delivery by integrating security throughout the CI/CD pipeline.

The proposed DevSecOps architecture aims to provide:

- Faster software delivery
- Earlier security detection
- Automated compliance
- Continuous monitoring
- Audit-ready evidence

---

# Current Challenges

The current environment has several issues:

- Security checks happen too late.
- Secrets (API Keys) have been committed into source control.
- Vulnerability reports are difficult to prioritize.
- DAST testing occurs after release candidates are prepared.
- Infrastructure changes are partly manual.
- Audit evidence is difficult to collect.

---

# Proposed Architecture

Developer

↓

GitHub Repository

↓

GitHub Actions (CI/CD)

↓

Build Application

↓

Unit Testing

↓

Secret Scanning

↓

Static Application Security Testing (SAST)

↓

Software Composition Analysis (Dependency Scan)

↓

Container Image Scan

↓

Infrastructure as Code Scan

↓

Deploy to Staging

↓

Dynamic Application Security Testing (DAST)

↓

Manual Security Approval

↓

Deploy to Production

↓

Monitoring & Continuous Feedback

---

# Benefits

This architecture provides:

- Shift-Left Security
- Faster developer feedback
- Automated security validation
- Continuous compliance
- Better audit evidence
- Reduced deployment risk
- Faster and more reliable software delivery
