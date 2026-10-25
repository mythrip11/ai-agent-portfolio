# Healthcare AI Agents

> 3 n8n workflow agents for patient discharge management, insurance prior authorization, and clinical trial recruitment. Each one was built, run, and exported from a local n8n instance and tested end to end with fictional data.

![status](https://img.shields.io/badge/status-tested%20with%20fictional%20data-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)
![built with](https://img.shields.io/badge/built%20with-n8n%20%2B%20Claude-orange)

---

## ✨ Agents

### HC-1: Patient Discharge & Care Continuity
**Trigger:** Webhook POST → fired by an EHR on discharge

> **Problem:** Hospitals discharge large numbers of patients every day, and high-risk cases can slip through without timely follow-up, which raises the chance of readmission.
> **Built:** A webhook agent that normalizes the discharge payload, has Claude assess readmission risk with a structured output, and routes the case by risk level.
> **Outcome:** High-risk patients trigger an urgent email to the physician, medium-risk patients get a follow-up reminder email, and low-risk discharges are logged with a routine care plan.

![HC-1 workflow in n8n](../../screenshots/HC-1.png)
*Webhook trigger, Claude risk assessment, risk-level router, then physician alerts and patient follow-up by Gmail.*

```
EHR Discharge Event
      ↓
Normalize Payload
      ↓
Claude Risk Assessment
      ↓
    Router
   /  |  \
High  Med  Low
 ↓     ↓    ↓
Alert  Follow-up  Log
Physician  Email  Care Plan
(Gmail)   (Gmail)
```

✅ Risk-stratifies every discharge as it arrives
✅ Emails the physician for high-risk patients
✅ Sends a follow-up email for medium-risk patients

**Where this pattern applies:**
- Hospital systems: automate post-discharge follow-up for cardiac patients
- Health networks: flag CHF and COPD patients for same-day nurse callback
- Telehealth platforms: trigger virtual follow-up scheduling on discharge

**n8n:** https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/healthcare/HC-1_patient-discharge-care-continuity.json

---

### HC-2: Insurance Prior Authorization Automation
**Trigger:** Webhook POST → from an EHR or provider portal

> **Problem:** Providers spend a lot of time assembling and submitting prior authorization requests by hand, which delays patient procedures.
> **Built:** A webhook agent that checks coverage (mock eligibility step), has Claude evaluate the clinical notes against medical-necessity criteria, and submits to the payer (mock step) when the criteria are met.
> **Outcome:** Requests that meet the criteria are submitted and confirmed by email. Requests with gaps get an email listing exactly which documents are missing, and inactive coverage gets its own notice.

![HC-2 workflow in n8n](../../screenshots/HC-2.png)
*Webhook trigger, mock eligibility check, Claude medical-necessity review, then payer submission or Gmail notices.*

```
Auth Request Webhook
      ↓
Check Insurance Eligibility (mock)
      ↓
  Coverage Active?
   Yes         No
    ↓           ↓
Claude Medical   Notify Provider
Necessity Review (coverage inactive)
      ↓
  Criteria Met?
   Yes      No
    ↓        ↓
Submit    Notify Provider
to Payer  (missing docs)
(mock)
```

✅ Evaluates clinical notes against medical-necessity criteria
✅ Submits automatically when criteria are met
✅ Returns a missing-documentation checklist to the provider

**Where this pattern applies:**
- Payer-facing teams: pre-screen high-volume imaging and orthopedic requests
- Provider offices: reduce the manual back-and-forth on routine outpatient procedures
- EHR-integrated clinics: trigger requests directly from intake forms

**n8n:** https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/healthcare/HC-2_insurance-prior-authorization.json

---

### HC-3: Clinical Trial Recruitment & Screening
**Trigger:** Schedule → runs daily at 8:00 AM

> **Problem:** Research teams often screen patient charts by hand to find trial candidates, which is slow and can miss eligible patients.
> **Built:** A daily agent that pulls a patient list (mock EHR), splits it into one item per patient, and has Claude screen each one against trial inclusion and exclusion criteria (a fictional diabetes trial).
> **Outcome:** Eligible patients get a personalized outreach email and are logged as candidates, and ineligible patients are logged with the reason.

![HC-3 workflow in n8n](../../screenshots/HC-3.png)
*Daily schedule, mock EHR candidates, Claude trial-eligibility screening, then Gmail outreach and logging.*

```
Daily Scheduler
      ↓
Fetch Patient Candidates (mock EHR)
      ↓
Split Patient Candidates
      ↓
Claude Eligibility Screening
      ↓
  Eligible?
  Yes       No
   ↓         ↓
Send        Log
Outreach    Ineligible
Email (Gmail)
   ↓
Log Candidate
```

✅ Screens the full patient list on every run
✅ Sends personalized outreach to eligible patients
✅ Logs every result (eligible and ineligible) with the reasoning

**Where this pattern applies:**
- Research teams: automate recruitment screening across partner clinics
- Clinical trial platforms: feed screening output into a trial management system
- Academic medical centers: run nightly screens across several concurrent trials

**n8n:** https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/healthcare/HC-3_clinical-trial-recruitment.json

---

## 🚀 Quick Start

### Prerequisites
- An n8n instance (self-hosted, for example `localhost:5678`, or n8n Cloud)
- An Anthropic API key (Claude). You can also swap the model node for another chat model.
- Gmail OAuth2 credentials

### Setup (all three workflows)
1. In n8n, go to **Workflows → Import from File** and choose the JSON file.
2. Attach your own **Anthropic** and **Gmail OAuth2** credentials to the model and Gmail nodes.
3. Change the recipient address in the Gmail nodes (and any `contact_email` values in mock-data nodes) to your own.
4. Click **Execute workflow**. Use fictional data only.

### HC-1 test request
Click **Execute workflow** in n8n first so the test webhook is listening, then send:

```bash
curl -X POST http://localhost:5678/webhook-test/patient-discharge -H "Content-Type: application/json" -d '{"patient_id":"P-1001","age":78,"diagnosis":"Congestive heart failure","comorbidities":["COPD","diabetes"],"length_of_stay_days":9,"prior_admissions_12mo":3,"discharge_disposition":"home","medications_count":14}'
```

### HC-2 test request
Click **Execute workflow**, then send a fictional request to `http://localhost:5678/webhook-test/prior-auth-request`.

### HC-3
The mock EHR node holds 5 fictional patients and the Claude agent screens them against fictional INNOVATE-DM2 criteria. Click **Execute workflow** to run it. If the "Log Eligible Candidate to CRM" node is greyed out after import, select it and press `D` to enable it.

### Credentials

| Agent | Credentials |
|-------|-------------|
| HC-1  | Anthropic · Gmail |
| HC-2  | Anthropic · Gmail |
| HC-3  | Anthropic · Gmail |

The EHR, payer, and CRM steps are mock Code nodes with fictional data. To connect real systems, replace them with HTTP Request nodes.

---

## 🧑‍💻 Author
**Mythri Potluri** · GitHub: [@mythrip11](https://github.com/mythrip11)

## 📄 License
MIT

[← Back to the portfolio](../../README.md)
