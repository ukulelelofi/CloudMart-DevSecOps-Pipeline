# CloudMart-DevSecOps-Pipeline

DevSecOps Capstone Project demonstrating a secure CI/CD pipeline using GitHub Actions with automated testing, security scanning, governance, and compliance.

---

## 🚀 DevSecOps Pipeline Architecture

```mermaid
flowchart TD

A[Developer Push / Pull Request] --> B[GitHub Repository]

B --> C[GitHub Actions]

C --> D[Checkout Repository]

D --> E[Build Stage]

E --> F[Install Dependencies]

F --> G[Run Unit Tests - Pytest]

G --> H[Secret Scan - Gitleaks]

H --> I[SAST - CodeQL]

I --> J[Vulnerability Scan - Trivy]

J --> K[Generate Audit Evidence]

K --> L[Upload Audit Evidence Artifact]

L --> M[Release Gate Validation]

M --> N[Ready for UAT / Production Approval]
```

---

## Security Controls

- ✅ GitHub Actions CI Pipeline
- ✅ Pytest Unit Testing
- ✅ Gitleaks Secret Detection
- ✅ CodeQL Static Application Security Testing (SAST)
- ✅ Trivy Vulnerability Scanning
- ✅ Audit Evidence Generation
- ✅ Artifact Upload
- ✅ Release Gate Validation

---

## Governance & Compliance

This pipeline demonstrates enterprise DevSecOps practices by ensuring:

- Security
