# Transportation AI Agents

> 3 n8n workflow agents for fleet maintenance prediction, dynamic route optimization, and freight exception management. Each one was built, run, and exported from a local n8n instance and tested end to end with fictional data.

![status](https://img.shields.io/badge/status-tested%20with%20fictional%20data-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)
![built with](https://img.shields.io/badge/built%20with-n8n%20%2B%20Claude-orange)

---

## ✨ Agents

### TR-4: Fleet Predictive Maintenance
**Trigger:** Schedule → runs every hour

> **Problem:** Fleet maintenance is often reactive, so breakdowns, towing, and missed deliveries happen before anyone looks at the warning signs in the telematics data.
> **Built:** An hourly agent that reads telematics for each vehicle (mock data in the demo), has Claude analyze sensor readings and diagnostic trouble codes, and returns a structured verdict with urgency, the likely failing component, and a recommended action.
> **Outcome:** At-risk vehicles get a mock service appointment, with the date based on urgency, and the fleet manager is emailed the details. Healthy vehicles are logged.

![TR-4 workflow in n8n](../../screenshots/TR-4.png)
*Hourly schedule, mock fleet telematics, Claude maintenance prediction, then a service appointment and Gmail alert.*

```
Hourly Scheduler
      ↓
Fetch Fleet Telemetry (mock)
      ↓
Split into One Vehicle per Item
      ↓
Claude Analyzes Sensors + DTC Codes
      ↓
  Maintenance Needed?
   Yes           No
    ↓             ↓
Schedule      Log Healthy
Service       Status
(mock)
    ↓
Gmail Alert to
Fleet Manager
```

✅ Flags at-risk vehicles from sensor data and fault codes
✅ Books a service appointment (mock) with urgency-based timing
✅ Emails the fleet manager the issue, urgency, and recommended action

**Where this pattern applies:**
- Commercial truck fleets: act on engine and brake warnings before a breakdown
- Last-mile delivery fleets: monitor van health across many vehicles
- Transit operators: prioritize maintenance by urgency

**n8n:** https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/transportation/TR-4_fleet-predictive-maintenance.json

---

### TR-5: Dynamic Route Optimization & Exception
**Trigger:** Schedule → runs every 15 minutes

> **Problem:** When weather or traffic incidents hit, dispatchers reroute drivers by hand and customers often hear nothing until a delivery is already late.
> **Built:** A 15-minute agent that checks each active delivery against traffic and weather conditions (mock data in the demo) and has Claude decide whether the delay is significant. Express and time-sensitive cargo has a lower threshold.
> **Outcome:** For significant delays the agent picks an alternate route and a new ETA, updates dispatch (mock), and emails both the driver and the customer. On-time deliveries are logged.

![TR-5 workflow in n8n](../../screenshots/TR-5.png)
*15-minute schedule, mock deliveries and traffic/weather, Claude delay assessment, then reroute and Gmail notices.*

```
Every 15 Minutes
      ↓
Fetch Active Deliveries (mock)
      ↓
Split into One Delivery per Item
      ↓
Fetch Traffic + Weather (mock)
      ↓
Claude Assesses Delay + Reroute
      ↓
  Significant Delay?
   Yes           No
    ↓             ↓
Update Route   Log On-Time
+ ETA (mock)   Status
    ↓
Gmail Driver
    ↓
Gmail Customer
```

✅ Checks every active delivery on each run
✅ Recommends an alternate route and new ETA for significant delays
✅ Notifies both the driver and the customer by email

**Where this pattern applies:**
- Parcel and freight carriers: reroute around corridor-wide weather events
- Same-day delivery services: correct ETAs before customers ask
- LTL carriers: cut the customer service load during weather delays

**n8n:** https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/transportation/TR-5_dynamic-route-optimization.json

---

### TR-6: Freight Exception & Carrier Resolution
**Trigger:** Schedule → runs every hour

> **Problem:** Freight teams triage a steady stream of shipment exceptions by hand, and high-value or time-critical cargo can be escalated too late.
> **Built:** An hourly agent that reads in-transit shipments with exceptions (mock TMS data in the demo) and has Claude classify each as critical, standard, or low, taking cargo value, delay, and SLA deadline into account.
> **Outcome:** Critical exceptions open a case (mock CRM) and email the account manager and the customer. Standard exceptions open a case and email the customer. Low-severity exceptions are logged.

![TR-6 workflow in n8n](../../screenshots/TR-6.png)
*Hourly schedule, mock shipments, Claude severity classification, then a three-way router (critical, standard, low).*

```
Hourly Scheduler
      ↓
Fetch Shipments with Exceptions (mock)
      ↓
Split into One Shipment per Item
      ↓
Claude Classifies Exception Severity
      ↓
      Router
   /    |    \
Critical Std  Low
   ↓     ↓    ↓
Create  Create  Log
Case    Case
   ↓     ↓
Gmail   Gmail
Account Customer
Manager
   ↓
Gmail
Customer
```

✅ Classifies every exception by severity with a written rationale
✅ Escalates critical shipments to the account manager by email
✅ Creates cases (mock CRM) and notifies customers

**Where this pattern applies:**
- Freight brokers: triage weather and carrier delay exceptions
- LTL carriers: escalate high-value exceptions to key account managers
- Shippers: notify customers about critical B2B delivery problems

**n8n:** https://github.com/mythrip11/ai-agent-portfolio/blob/main/workflows/transportation/TR-6_freight-exception-management.json

---

## 🚀 Quick Start

### Prerequisites
- An n8n instance (self-hosted, for example `localhost:5678`, or n8n Cloud)
- An Anthropic API key (Claude)
- Gmail OAuth2 credentials

### Setup (all three workflows)
1. In n8n, go to **Workflows → Import from File** and choose the JSON file.
2. Attach your own **Anthropic** and **Gmail OAuth2** credentials to the model and Gmail nodes.
3. Change the recipient address in the Gmail nodes to your own.
4. Click **Execute workflow**. Use fictional data only.

### What each workflow contains
- **TR-4** (`TR-4_fleet-predictive-maintenance.json`): hourly schedule, a mock telematics node with 5 fictional vehicles, a Claude agent with structured output, a mock service-appointment node, and a Gmail alert.
- **TR-5** (`TR-5_dynamic-route-optimization.json`): 15-minute schedule, mock dispatch (4 fictional deliveries) and mock traffic/weather nodes, a Claude agent, a mock route/ETA update, and Gmail notices to the driver and the customer.
- **TR-6** (`TR-6_freight-exception-management.json`): hourly schedule, a mock TMS node with 5 fictional shipments, a Claude agent, a Switch router, mock CRM cases, and Gmail notices.

### Credentials

| Agent | Credentials |
|-------|-------------|
| TR-4  | Anthropic · Gmail |
| TR-5  | Anthropic · Gmail |
| TR-6  | Anthropic · Gmail |

The telematics, dispatch, traffic, TMS, and CRM steps are mock Code nodes with fictional data. To connect real systems, replace them with HTTP Request nodes.

---

## 🧑‍💻 Author
**Mythri Potluri** · GitHub: [@mythrip11](https://github.com/mythrip11)

## 📄 License
MIT

[← Back to the portfolio](../../README.md)
