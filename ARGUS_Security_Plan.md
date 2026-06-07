# Project ARGUS — Security Plan
## River Shoals HOA | Defense-in-Depth Framework

Executive summary
-----------------

This security plan documents the defense-in-depth approach for ARGUS. It lists the security layers (from physical controls through legal/compliance), operational responsibilities, incident response, and the pre-go-live checklist for each project phase.

Key principles:
- Minimize attack surface via network segmentation and least privilege access.
- Keep sensitive data on-premises; share footage only via controlled, documented processes.
- Maintain separation of duties between system administration (Howard), operations (GHS), and board governance.

*Last updated: June 2026 | Owner: Howard Rapp*

> **Defense in depth** means no single point of failure protects the community. Security is layered — physical, electronic, procedural, and legal — so that if any one layer is bypassed or fails, other layers remain intact. This document defines those layers for the ARGUS system.

---

## 1. Security Layers Overview

```
  ┌───────────────────────────────────────────────────────────┐
  │                    LAYER 7: LEGAL / COMPLIANCE            │
  │         Attorney review, privacy notices, data policy     │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 6: AUDIT & ACCOUNTABILITY        │
  │      Full access logs, video retention, board oversight   │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 5: INCIDENT RESPONSE             │
  │       Defined escalation paths, GHS first response        │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 4: MONITORING & DETECTION        │
  │    AI motion alerts, smart detection, anomaly response    │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 3: DATA SECURITY                 │
  │   On-premises storage, access restrictions, encryption    │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 2: NETWORK SECURITY              │
  │     VLAN segmentation, firewall rules, no open ports      │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 1: ACCESS CONTROL                │
  │    Credential management, fob lifecycle, least privilege  │
  ├───────────────────────────────────────────────────────────┤
  │                    LAYER 0: PHYSICAL SECURITY             │
  │     Gates, cameras, lighting, locks, visible deterrence   │
  └───────────────────────────────────────────────────────────┘
```

---

## Layer 0: Physical Security

Physical controls are the outermost layer. They deter, delay, and detect unauthorized access before any electronic system is involved.

**Gates:**
- Both vehicle gates are controlled-access. They do not open without a valid credential (fob/NFC) or visitor intercom authorization.
- Gate operators use hardwired loop detectors for exit — residents leaving do not need credentials.
- Gates are the primary perimeter control. Tailgating (following a vehicle through without credentials) is the main physical vulnerability. LPR cameras address this by capturing every plate that enters.

**Cameras:**
- All cameras are visible. Visible cameras are a deterrent. No hidden cameras are installed or planned.
- AI-series cameras provide full coverage of: pool deck (360°), parking lot, clubhouse exterior door, perimeter fence, and both gate entry lanes.
- Footage is retained for approximately 30 days on the UNVR.

**Lighting:**
- AI-Pro and AI-Bullet cameras have built-in IR illumination. They record in full darkness at effective range.
- Existing lighting at the clubhouse and gates is assumed adequate. If incident review reveals blind spots due to poor lighting, this section will be updated.

**Locks:**
- Pool gate: Existing magnetic lock integrated with the Access Hub.
- Clubhouse door: Maglock installed by licensed contractor. Door remains locked at all times and opens only with a valid credential or manual override by authorized staff.
- Gate operators: Existing electric operators, controlled via dry contact relay from Access Hub.

---

## Layer 1: Access Control

Access control defines who can enter what, when, and under what conditions.

**Credential types:**
- **Key fob (UA-Fob):** Issued to all households. One fob per lot as standard; additional fobs available through GHS at board's discretion.
- **NFC (smartphone):** UniFi Access supports mobile credentials via the UniFi Access app. Optional — fob is the primary credential.
- **Visitor intercom (front gate only):** Visitors call in via the AI-Theta-Pro. GHS or a board member answers remotely and grants or denies access.
- **Admin override:** GHS admins can unlock any door or gate remotely through the UniFi Access dashboard.

**Credential lifecycle — key principles:**

| Event | Action | Who |
|---|---|---|
| New resident moves in | Issue fob, activate in UniFi Access | GHS |
| Resident moves out | Immediately deactivate fob in UniFi Access | GHS (same day as notice) |
| Fob reported lost | Immediately deactivate in UniFi Access, issue replacement | GHS |
| Fob not returned at sale | Deactivate — the system is credential-based, physical possession of a deactivated fob grants nothing | GHS |
| Seasonal rental tenant | Create time-limited credential with access schedule | GHS |
| Contractor needing temporary access | Issue time-limited credential tied to work period only | GHS (board approval required) |

**Least privilege by zone:**

| Zone | Who has access |
|---|---|
| Vehicle gates (entry) | All credentialed residents |
| Pool gate | All credentialed residents (seasonal schedule: pool hours only) |
| Clubhouse door | GHS staff, board members, authorized residents (not all residents by default) |
| UniFi dashboard — admin | Howard Rapp, GHS (Sharon and Kevin Bragman) |
| UniFi dashboard — viewer | All board members, Ruth Jansen |

**Access schedules:**
- Pool gate should be configured with access hours matching the posted pool schedule (e.g., 7am–10pm). Access outside hours should require a board override.
- Vehicle gates are 24/7 for credentialed residents.
- Clubhouse door hours can be restricted to business hours by default, with GHS admin override for events.

**Offline behavior at gates:**
The Access Hub at each gate caches all active credentials locally. If LTE connectivity drops, residents can still enter using their fob or NFC. The hub resumes syncing new credentials and access logs when connectivity is restored. No resident is ever locked out due to a network outage.

---

## Layer 2: Network Security

Network segmentation ensures that a compromise of one system cannot propagate to others. See ARGUS_Network_Architecture.md for full VLAN and IP details.

**Core firewall rules:**

| Rule | Description | Rationale |
|---|---|---|
| Cameras → Outbound blocked | Camera VLAN (10) has no direct internet access | Prevents cameras from being used as botnet nodes or exfiltrating footage |
| Cameras → UNVR only | Camera VLAN can only communicate with the UNVR | Footage stays on-premises, cameras are isolated |
| Access Hubs → Cloud HTTPS only | VLAN 20 allows only outbound HTTPS to Ubiquiti's cloud endpoints | Limits attack surface, prevents lateral movement |
| Guest WiFi → Isolated | Pool/guest WiFi VLAN is fully blocked from all security VLANs | Residents on WiFi cannot see or interact with cameras or access control |
| No inbound port forwarding | The UCG-Ultra has no public ports open | Eliminates exposure to internet-based attacks |
| Admin access → VPN only (if remote) | Remote dashboard access via UniFi's encrypted relay, not open ports | No exposed management interface |

**Password policy:**
- UniFi dashboard admin password: minimum 16 characters, unique, stored in ARGUS folder credentials document (not this file).
- All default credentials changed before any device goes online.
- No shared passwords. Each admin user has their own login.

**Firmware policy:**
- UniFi devices auto-update on a controlled schedule. Howard reviews and applies updates within 30 days of release.
- No device runs firmware more than two major versions behind.

---

## Layer 3: Data Security

**Video retention:**
- Standard retention: 30 days at 1080p continuous recording (5 cameras).
- Footage is stored on the UNVR hard drives (on-premises only). Nothing is stored in Ubiquiti's cloud.
- After 30 days, footage is automatically overwritten. Board must request a clip export before the retention window expires if footage is needed for an incident.

**Who can view footage:**
- GHS (admin): Full access to live and recorded footage.
- Board members (viewer): Can view footage; cannot delete or export without Howard's assistance.
- No resident or outside party has any access to camera footage.
- Footage shared with law enforcement requires a board decision and attorney consultation. Do not share footage informally.

**Access logs:**
- Every credential event is logged: who (which fob/credential), what (which door/gate), when (date/time), and outcome (granted/denied).
- Logs are retained for a minimum of 90 days in UniFi Access.
- Logs should be reviewed monthly by GHS as part of routine operations.

**Data handling at the gates (legal requirement):**
- Before Phase 3 gates go live, Luke Burke must review the LPR camera data handling policy. License plate data associated with resident movement patterns may trigger SC privacy considerations.
- A written policy must exist before the system is activated, covering: what data is collected, how long it is retained, who can access it, and under what circumstances it will be shared.
- This is a hard gate — Phase 3 does not go live without attorney sign-off.

**Backups:**
- UniFi controller configuration should be backed up monthly to a file stored in the ARGUS Google Drive folder.
- UNVR footage is not backed up (30-day overwrite is by design). If long-term archival of specific footage is needed, export and store in a designated secure location.

---

## Layer 4: Monitoring and Detection

**AI-powered detection (UniFi Protect):**
- All cameras use UniFi AI for smart detection. Alerts are generated for: person detection, vehicle detection, package detection (where applicable), and motion in defined zones.
- Detection sensitivity is configured per-camera during Phase 1 installation.
- GHS receives push alerts for significant detection events. Nuisance alerts (routine traffic) are filtered by zone configuration.

**Recommended alert configuration:**

| Camera | Alert trigger | Recipient |
|---|---|---|
| Pool deck (AI-360 x2) | Person detected after pool hours | GHS via app |
| Parking lot (AI-Pro) | Vehicle detected after midnight | GHS via app |
| Clubhouse exterior (AI-Pro) | Person at door after business hours | GHS via app |
| Perimeter (AI-Bullet) | Person detected (any time) | GHS via app |
| Front gate LPR | Camera always recording, no alert | N/A |
| Rear gate LPR | Camera always recording, no alert | N/A |

**Gate access alerts:**
- Configure UniFi Access to alert GHS on: denied access attempts (credential not recognized), door held open too long, and repeated failures (possible credential stuffing).

**Weekly review:**
- GHS should review access logs weekly for anomalies: credentials used at unusual hours, unusual frequency of access, any denied attempts.
- Board president receives a brief monthly summary from GHS.

---

## Layer 5: Incident Response

**Escalation path:**

```
  Incident occurs
       │
       ▼
  GHS (first response) — Sharon / Kevin Bragman
  │  support@greenvillehoa.com | 864-213-2156
  │
  ├─▶ Can resolve (routine access issue, footage request)?
  │      └─▶ Handle and document in access log
  │
  ├─▶ Requires board decision?
  │      └─▶ Contact Howard Rapp: howarddalerapp@gmail.com
  │
  ├─▶ Potential criminal matter?
  │      └─▶ Contact Howard Rapp immediately
  │          Howard contacts Luke Burke: lburke@gvlattorney.com
  │          Do NOT share footage with anyone until attorney advises
  │
  └─▶ System down / technical failure?
         └─▶ Contact Howard Rapp: howarddalerapp@gmail.com
             (Howard is system owner and sole technical resource)
```

**Incident documentation:**
Every incident involving the ARGUS system should be documented. At minimum, record: date/time, what was observed, what action was taken, and by whom. GHS maintains this log in the CINC system. A copy of any significant incident goes to Howard.

**Common incidents and responses:**

| Incident | Immediate response |
|---|---|
| Pool break-in or vandalism | GHS reviews footage, exports clip, notifies Howard. Howard contacts police if appropriate, Luke Burke if legal questions arise. |
| Gate not opening for credentialed resident | GHS checks UniFi Access for the credential status. If deactivated in error, reactivate. If system issue, check LTE status. Escalate to Howard if unresolved. |
| Gate stuck open | GHS attempts remote close via dashboard. If fails, dispatch to site. Gate operator manual override exists (see Phase 3 as-built notes). |
| Unauthorized person in pool area | Review footage. If ongoing, notify police. If trespassing pattern, consider issuing trespass notice (consult Luke Burke). |
| Lost/stolen fob | Resident contacts GHS. GHS deactivates immediately in UniFi Access, issues replacement fob. Zero-delay deactivation is critical. |
| System compromise suspected | Howard to be notified immediately. Change all admin passwords. Review access logs for anomalous activity. Consult Luke Burke if data exposure is possible. |
| LTE outage at gate | Gates continue to function for credentialed residents (offline mode). Visitor intercom is unavailable. Howard monitors and contacts carrier. |

---

## Layer 6: Audit and Accountability

**Board oversight:**
- Howard, as system owner, retains Super Admin access. No other person has Super Admin.
- GHS has Admin access for day-to-day operations but cannot delete footage or modify system configuration without Howard's knowledge.
- Board members have Viewer access only. They can review footage and logs but cannot make changes.

**Annual review:**
Once per year, Howard reviews: all admin accounts and their access levels, fob inventory vs. current resident roster, firmware versions, system health, and the security plan itself for any needed updates.

**Change control:**
Any change to system configuration (VLAN rules, firewall policy, access schedules, user permissions) must be documented in the Decisions Log. Undocumented changes by GHS are not authorized.

**Separation of duties:**
- GHS manages residents and credentials (operational layer).
- Howard manages system configuration and security policy (technical layer).
- Board approves policy changes and reviews incidents (governance layer).
- Luke Burke advises on legal questions before policies are implemented.

---

## Layer 7: Legal and Compliance

**Privacy notices:**
Before the system goes live, physical notices must be posted at all camera locations and gate entry points. Required language varies but should include: that the area is under video surveillance, that footage is retained for 30 days, and a contact for questions (GHS contact information).

**Required before Phase 3 go-live:**
- Luke Burke to review LPR data handling policy (license plate capture = resident movement data).
- Written data retention and handling policy must exist.
- Board must formally vote to adopt the policy.

**Footage sharing policy:**
Footage may only be shared with: law enforcement pursuant to a lawful request, parties involved in an incident with board approval, or as required by a court order. Footage is never shared informally with residents, neighbors, or other third parties. All sharing decisions require board approval and are documented.

**Insurance notice:**
The ARGUS system is a security improvement that may affect the HOA's liability profile. Howard should notify Ables Insurance that the system has been installed once Phase 1 is complete, and ask whether it affects the E&O/D&O policy or qualifies for any premium adjustment.

---

## Security Checklist — Pre-Go-Live (Each Phase)

### Phase 1 Checklist
- [ ] All default passwords changed on all devices
- [ ] VLAN configuration verified — cameras isolated from other VLANs
- [ ] No public-facing ports open on UCG-Ultra
- [ ] UNVR recording verified for all 5 cameras
- [ ] Retention period confirmed at ~30 days
- [ ] GHS admin accounts created and tested
- [ ] Board viewer accounts created and tested
- [ ] Controller configuration backup saved to ARGUS Google Drive
- [ ] Privacy notices posted at clubhouse and pool

### Phase 2 Checklist
- [ ] All fobs registered in UniFi Access with resident names
- [ ] Pool gate access schedule set to pool hours
- [ ] Clubhouse door access restricted to authorized personnel
- [ ] Access log review process communicated to GHS
- [ ] Incident response procedure shared with GHS
- [ ] Maglock contractor work reviewed — fire egress verified

### Phase 3 Checklist
- [ ] Luke Burke sign-off on LPR data handling policy — **DO NOT SKIP**
- [ ] Board vote on data handling policy documented in Decisions Log
- [ ] Privacy notices posted at both gate entry points
- [ ] LTE connectivity confirmed stable at both gates
- [ ] Offline failover tested at both gates (pull LTE SIM, confirm fob still works)
- [ ] LPR cameras confirmed capturing plates at entry distance
- [ ] Visitor intercom tested — GHS confirmed receiving calls
- [ ] CPS system confirmed offline / terminated before declaring ARGUS live
- [ ] Ables Insurance notified of ARGUS completion

---

*Project ARGUS | River Shoals HOA | Confidential Board Document*
*Last updated: June 2026*
