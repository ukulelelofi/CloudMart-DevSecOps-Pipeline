#  CloudMart DevSecOps Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-success)
![CodeQL](https://img.shields.io/badge/SAST-CodeQL-blue)
![Trivy](https://img.shields.io/badge/Vulnerability-Trivy-success)
![Gitleaks](https://img.shields.io/badge/Secrets-Gitleaks-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

#  Project Story

CloudMart is a fictional e-commerce platform designed to demonstrate how modern organizations can implement an enterprise-grade DevSecOps CI/CD pipeline using GitHub Actions.

Rather than focusing only on automation, this project demonstrates how secure software can move safely from development to production through automated testing, security validation, governance controls, deployment approvals, compliance evidence and release quality gates.

The project follows a **Shift-Left Security** approach by embedding security throughout the Software Development Life Cycle (SDLC), enabling vulnerabilities and misconfigurations to be detected before deployment.

---

#  Project Objectives

This project was created to demonstrate practical implementation of:

- Continuous Integration (CI)
- Continuous Delivery (CD)
- Secure Software Development Lifecycle (SSDLC)
- Shift-Left Security
- DevSecOps Automation
- Governance & Compliance
- Deployment Traceability
- Audit Evidence Generation
- Release Gate Validation

---

#  Project Overview

Every source code change automatically triggers an enterprise DevSecOps pipeline consisting of:

- Source Code Checkout
- Dependency Installation
- Unit Testing
- Secret Detection
- Static Application Security Testing (SAST)
- Filesystem Vulnerability Scanning
- Docker Image Build
- Container Vulnerability Scanning
- Pull Request Validation
- Manual Deployment Approval
- Deployment Evidence Generation
- Release Gate Validation

---

#  Technologies

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.11 |
| Web Framework | Flask |
| Version Control | Git |
| Repository | GitHub |
| CI/CD Platform | GitHub Actions |
| Unit Testing | Pytest |
| Secret Detection | Gitleaks |
| Static Application Security Testing (SAST) | GitHub CodeQL |
| Vulnerability Scanning | Trivy |
| Containerization | Docker |
| Deployment Control | GitHub Environments |
| Compliance Evidence | GitHub Artifacts |

---

##  CloudMart DevSecOps CI/CD Pipeline

```mermaid
flowchart TD

A[ Developer pushes code to Feature Branch] --> B[Stage 1: Unit Testing<br/>Pytest validates application functionality]

B -- Tests Failed --> BLOCK1[🚫 CI Failed<br/>Fix application code]

B -- Tests Passed --> C[Stage 2: Secret Detection<br/>Gitleaks scans for API keys, passwords and tokens]

C -- Secrets Found --> BLOCK2[🚫 Release Blocked<br/>Remove secret and rotate credentials]

C -- No Secrets --> D[Stage 3: Static Application Security Testing<br/>GitHub CodeQL analyses source code]

D -- High Risk Found --> BLOCK3[🚫 Release Blocked<br/>Fix security vulnerabilities]

D -- Passed --> E[Stage 4: Filesystem Vulnerability Scan<br/>Trivy scans project dependencies]

E -- Critical Vulnerability --> BLOCK4[🚫 Release Blocked<br/>Update vulnerable packages]

E -- Passed --> F[Stage 5: Build Docker Image]

F --> G[Stage 6: Container Image Scan<br/>Trivy scans Docker image]

G -- Critical Vulnerability --> BLOCK5[🚫 Release Blocked<br/>Use secure base image]

G -- Passed --> H[Stage 7: Generate Audit Evidence<br/>Commit SHA, Branch, Timestamp]

H --> I[Stage 8: CI Release Gate]

I --> J[Pull Request Review]

J --> K[Merge into Main Branch]

K --> L[Stage 9: Deploy to Development]

L --> M[Generate Deployment Evidence]

M --> N[Manual Approval<br/>GitHub Environment]

N --> O[Stage 10: Deploy to UAT]

O --> P[Generate Deployment Evidence]

P --> Q[Manual Approval<br/>Release Manager]

Q --> R[Stage 11: Deploy to Production]

R --> S[Production Validation]

S --> T[Generate Production Evidence]

T --> U[ Secure Production Release]

```

#  Governance, Compliance & Audit

```
                Governance & Compliance

                ┌───────────────────────┐
                │ Secure Development     │
                └───────────┬────────────┘
                            │
                            ▼
                 Automated Security Checks
                            │
       ┌──────────────┬──────────────┬──────────────┐
       ▼              ▼              ▼
   Gitleaks        CodeQL          Trivy
       │              │              │
       └──────────────┼──────────────┘
                      ▼
             Audit Evidence Generated
                      │
                      ▼
           Pull Request Review & Approval
                      │
                      ▼
         Controlled Deployment to Production
                      │
                      ▼
              Compliance & Traceability
```

#  Security Controls

| Security Control | Tool |
|------------------|------|
| Unit Testing | Pytest |
| Secret Detection | Gitleaks |
| Static Code Analysis | CodeQL |
| Filesystem Vulnerability Scan | Trivy |
| Container Image Scan | Trivy |
| Docker Build Validation | Docker |
| Release Validation | GitHub Actions |
| Deployment Approval | GitHub Environments |

---
---
#  KPI Dashboard

The following KPIs are used to measure pipeline quality and operational performance.

| KPI | Target |
|------|--------|
| Unit Test Pass Rate | 100% |
| Secrets Detected | 0 |
| Critical Vulnerabilities | 0 |
| High Vulnerabilities | 0 |
| Successful CI Builds | >95% |
| Successful Deployments | >95% |
| Audit Evidence Generated | 100% |
| Production Deployment Success | 100% |

---

---

#  Docker

Build the Docker image

```bash
docker build -t cloudmart .
```

Run the application

```bash
docker run -p 5000:5000 cloudmart
```

Access the application

```
http://localhost:5000
```

---

#  Deployment Strategy

CloudMart follows a controlled deployment strategy.

| Stage | Description |
|---------|-------------|
| CI | Build, Test, Security Validation |
| Pull Request | Code Review |
| Development | Automatic Deployment |
| UAT | Manual Approval |
| Production | Manual Approval |

---

#  Pipeline Status

Current implementation includes:

- ✅ Continuous Integration
- ✅ Continuous Delivery
- ✅ Unit Testing
- ✅ Secret Detection
- ✅ Static Code Analysis
- ✅ Filesystem Vulnerability Scanning
- ✅ Docker Image Build
- ✅ Container Security Scanning
- ✅ Audit Evidence Generation
- ✅ Deployment Evidence Generation
- ✅ Release Gate Validation
- ✅ Manual Deployment Approval

**Current Status**

🟢 Production Ready (Demonstration Environment)

---

#  Future Roadmap

The project will continue evolving with additional DevSecOps capabilities.

- Branch Protection Rules
- Required Pull Request Reviews
- Dependabot
- Software Bill of Materials (SBOM)
- Docker Image Signing (Cosign)
- Terraform Infrastructure as Code
- OWASP ZAP Dynamic Application Security Testing
- SonarQube Code Quality
- Kubernetes Deployment
- Azure Deployment
- Slack / Microsoft Teams Notifications
- Security Dashboard
- Prometheus Monitoring
- Grafana Visualization

---

#  Lessons Learned

This project strengthened my understanding of how DevSecOps extends beyond automation.

By combining CI/CD, security testing, governance, compliance, audit evidence and deployment approvals into a single workflow, I gained practical experience in implementing secure software delivery aligned with enterprise best practices.

---

#  Author

**YLHASH**

Cybersecurity | DevSecOps | Security Engineering

Proud human to six furkids 🐾, coffee enthusiast and always curious about improving security one step at a time.
