# Project ARGUS — Security Plan
## River Shoals HOA | Defense-in-Depth Framework

*Last updated: June 2026 | Owner: Howard Rapp*

> **Defense in depth** means no single point of failure protects the community. Security is layered — physical, electronic, procedural, and legal — so that if any one layer is bypassed or fails, others remain intact.

---

## 1. The Eight Layers of Defense

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#475569'}}}%%
graph BT
    L0["🔒 LAYER 0 — PHYSICAL SECURITY\nGates · Cameras · Lighting · Locks\nVisible deterrence and perimeter control"]
    L1["🪪 LAYER 1 — ACCESS CONTROL\nFob lifecycle · Least privilege · Schedules\nCredentialed entry only — no tailgating"]
    L2["🌐 LAYER 2 — NETWORK SECURITY\nVLAN segmentation · Firewall rules\nCameras isolated · No open ports"]
    L3["💾 LAYER 3 — DATA SECURITY\nOn-premises UNVR only · 30-day retention\nAccess logs 90 days · Footage policy"]
    L4["🔍 LAYER 4 — MONITORING & DETECTION\nAI motion alerts · Smart detection zones\nAnomaly response · After-hours alerts"]
    L5["🚨 LAYER 5 — INCIDENT RESPONSE\nEscalation paths · GHS first response\nHoward technical · Luke Burke legal"]
    L6["📋 LAYER 6 — AUDIT & ACCOUNTABILITY\nFull access logs · Board oversight\nAnnual review · Separation of duties"]
    L7["⚖️ LAYER 7 — LEGAL & COMPLIANCE\nAttorney review · Privacy notices\nLPR data policy · Insurance notification"]

    L0 --> L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7

    style L0 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style L1 fill:#7c2d12,stroke:#f97316,color:#fed7aa
    style L2 fill:#713f12,stroke:#eab308,color:#fef08a
    style L3 fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style L4 fill:#0c4a6e,stroke:#0ea5e9,color:#bae6fd
    style L5 fill:#1e1b4b,stroke:#6366f1,color:#c7d2fe
    style L6 fill:#4a1d96,stroke:#a855f7,color:#e9d5ff
    style L7 fill:#500724,stroke:#ec4899,color:#fbcfe8
```

---

## 2. Layer 0: Physical Security

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#ef4444'}}}%%
graph LR
    subgraph GATES["⚙️ GATES — Primary Perimeter"]
        G1["Front Gate\nW. Georgia Rd entry\nCredential-controlled"]
        G2["Rear Gate\nSecondary entry\nCredential-controlled"]
        G3["Loop Detectors\nHardwired exit\nNo credential needed to exit"]
    end

    subgraph CAMERAS["📷 CAMERAS — Detection & Deterrence"]
        C1["AI-360 × 2\nPool deck\n360° fisheye · no blind spots"]
        C2["AI-Pro × 2\nParking + door\nFace + plate capture"]
        C3["AI-Bullet × 1\nPerimeter fence\nLong-range IR"]
        C4["AI-Pro LPR × 2\nBoth gates\nEvery plate recorded"]
    end

    subgraph LOCKS["🔒 LOCKS — Controlled Entry"]
        L1["Pool gate\nElectronic strike\nAccess Hub controlled"]
        L2["Clubhouse door\nMaglock\nContractor installed\nFire egress safe"]
    end

    THREAT["👤 Unauthorized\nPerson / Vehicle"] -->|"Deterred by visible cameras"| CAMERAS
    THREAT -->|"Stopped at"| GATES
    THREAT -->|"Cannot enter without credential"| LOCKS

    style GATES fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style CAMERAS fill:#065f46,stroke:#10b981,color:#a7f3d0
    style LOCKS fill:#92400e,stroke:#f59e0b,color:#fde68a
    style THREAT fill:#1f2937,stroke:#6b7280,color:#d1d5db
    style G1 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style G2 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style G3 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style C1 fill:#0d3321,stroke:#10b981,color:#86efac
    style C2 fill:#0d3321,stroke:#10b981,color:#86efac
    style C3 fill:#0d3321,stroke:#10b981,color:#86efac
    style C4 fill:#0d3321,stroke:#10b981,color:#86efac
    style L1 fill:#431407,stroke:#f59e0b,color:#fcd34d
    style L2 fill:#431407,stroke:#f59e0b,color:#fcd34d
```

---

## 3. Layer 1: Access Control — Credential Lifecycle

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#f59e0b'}}}%%
flowchart TD
    START(["🏠 Resident Moves In"]) --> ISSUE["GHS issues fob\nRegisters in UniFi Access\nAssigns zones: gates + pool"]
    ISSUE --> ACTIVE["✅ Fob Active\nGates · Pool · Schedule-based"]

    ACTIVE --> Q1{"Event?"}

    Q1 -->|"Fob lost / stolen"| DEACT1["🚨 GHS deactivates\nIMMEDIATELY in UniFi\nPhysical fob worthless"]
    Q1 -->|"Resident moves out"| DEACT2["GHS deactivates\nSame day as notice"]
    Q1 -->|"Seasonal rental"| TEMP["Time-limited credential\nAccess schedule set\nAuto-expires"]
    Q1 -->|"Contractor access"| CONT["Named user profile\nTime-limited window\nBoard approval required"]
    Q1 -->|"Fob not returned at sale"| DEACT3["Deactivate immediately\nPhysical possession\ngrants nothing"]

    DEACT1 --> REISSUE["Issue replacement fob\nNew credential · New number"]
    DEACT2 --> END1(["Account deleted"])
    DEACT3 --> END2(["Account deleted"])
    REISSUE --> ACTIVE
    TEMP --> EXPIRE(["Credential auto-expires"])
    CONT --> EXPIRE

    style START fill:#065f46,stroke:#10b981,color:#fff
    style ISSUE fill:#0e7490,stroke:#06b6d4,color:#fff
    style ACTIVE fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style Q1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style DEACT1 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style DEACT2 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style DEACT3 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style TEMP fill:#92400e,stroke:#f59e0b,color:#fde68a
    style CONT fill:#4a1d96,stroke:#8b5cf6,color:#e9d5ff
    style REISSUE fill:#065f46,stroke:#10b981,color:#fff
    style END1 fill:#374151,stroke:#6b7280,color:#d1d5db
    style END2 fill:#374151,stroke:#6b7280,color:#d1d5db
    style EXPIRE fill:#374151,stroke:#6b7280,color:#d1d5db
```

**Least privilege by zone:**

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph LR
    subgraph ZONES["ACCESS ZONES"]
        Z1["🚗 Vehicle Gates\n24/7 all residents"]
        Z2["🏊 Pool Gate\nPool hours only\nAll residents"]
        Z3["🚪 Clubhouse Door\nGHS + board +\nauthorized residents only"]
        Z4["🖥️ UniFi Dashboard\nAdmin: Howard + GHS\nViewer: all board"]
    end

    RES["👥 All Residents"] -->|"✅ Full access"| Z1
    RES -->|"✅ Scheduled"| Z2
    RES -->|"❌ Not by default"| Z3
    GHS2["🏢 GHS Staff"] --> Z1 & Z2 & Z3 & Z4
    BOARD["📋 Board Members"] -->|"Viewer only"| Z4

    style ZONES fill:#0f172a,stroke:#475569,color:#e2e8f0
    style Z1 fill:#065f46,stroke:#10b981,color:#fff
    style Z2 fill:#065f46,stroke:#10b981,color:#fff
    style Z3 fill:#92400e,stroke:#f59e0b,color:#fff
    style Z4 fill:#4c1d95,stroke:#a78bfa,color:#fff
    style RES fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style GHS2 fill:#0e7490,stroke:#06b6d4,color:#fff
    style BOARD fill:#1e1b4b,stroke:#6366f1,color:#fff
```

---

## 4. Layer 2: Network Security — Firewall Rules

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#4b5563'}}}%%
flowchart LR
    CAMERA["📷 Camera\nVLAN 10"] -->|"✅ ALLOWED\nRecord footage"| UNVR4["💾 UNVR"]
    CAMERA -->|"🚫 BLOCKED\nNo internet"| INTERNET["🌐 Internet"]
    CAMERA -->|"🚫 BLOCKED\nCan't reach"| ACHUB["🔑 Access Hub"]
    CAMERA -->|"🚫 BLOCKED\nCan't reach"| WIFI["📶 WiFi clients"]

    ACHUB -->|"✅ ALLOWED\nManagement only"| UBCLOUD["☁️ Ubiquiti Cloud\nHTTPS only"]
    ACHUB -->|"🚫 BLOCKED\nNo browsing"| INTERNET
    ACHUB -->|"🚫 BLOCKED"| CAMERA

    GUEST["📱 Guest WiFi\nVLAN 30"] -->|"✅ ALLOWED"| INTERNET
    GUEST -->|"🚫 BLOCKED\nFully isolated"| CAMERA
    GUEST -->|"🚫 BLOCKED\nFully isolated"| ACHUB

    ADMIN["🖥️ Admin\nVLAN 1"] -->|"✅ ALLOWED"| UNVR4
    ADMIN -->|"✅ ALLOWED"| ACHUB
    ADMIN -->|"✅ ALLOWED"| INTERNET

    style CAMERA fill:#065f46,stroke:#10b981,color:#fff
    style UNVR4 fill:#4c1d95,stroke:#a78bfa,color:#fff
    style ACHUB fill:#92400e,stroke:#f59e0b,color:#fff
    style INTERNET fill:#1e40af,stroke:#3b82f6,color:#fff
    style UBCLOUD fill:#2d1a4a,stroke:#8b5cf6,color:#fff
    style GUEST fill:#0e7490,stroke:#06b6d4,color:#fff
    style ADMIN fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style WIFI fill:#0e7490,stroke:#06b6d4,color:#fff
```

---

## 5. Layer 3: Data Security

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#a78bfa'}}}%%
graph TD
    subgraph STORAGE["💾 ON-PREMISES STORAGE ONLY"]
        UNVR5["UNVR — Video footage\n~30 day retention\nAuto-overwrite after 30 days\n2× 4TB HDD"]
        LOGS["UniFi Access — Event logs\n90 day retention\nEvery fob tap recorded"]
    end

    subgraph WHO["👁️ WHO CAN ACCESS"]
        A1["GHS Admin\nFull access — live + recorded"]
        A2["Board Members\nViewer — cannot delete or export"]
        A3["Howard\nSuper Admin — all access"]
        NO["❌ Residents\n❌ Outside parties\n❌ Law enforcement\n   (without board vote + Luke Burke)"]
    end

    subgraph LEGAL["⚖️ SHARING POLICY"]
        S1["Law enforcement\nRequires lawful request\nBoard decision + Luke Burke"]
        S2["Incident parties\nRequires board approval\nDocumented in decisions log"]
        S3["Court order\nComply as legally required\nNotify Luke Burke first"]
        NEVER["🚫 Never share informally\nNever share with neighbors\nNever share without board vote"]
    end

    STORAGE --> WHO
    WHO --> LEGAL

    style STORAGE fill:#4c1d95,stroke:#a78bfa,color:#e9d5ff
    style WHO fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style LEGAL fill:#1e1b4b,stroke:#6366f1,color:#c7d2fe
    style UNVR5 fill:#2e1065,stroke:#a78bfa,color:#fff
    style LOGS fill:#2e1065,stroke:#a78bfa,color:#fff
    style A1 fill:#065f46,stroke:#10b981,color:#fff
    style A2 fill:#065f46,stroke:#10b981,color:#fff
    style A3 fill:#065f46,stroke:#10b981,color:#fff
    style NO fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style S1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style S2 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style S3 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style NEVER fill:#7f1d1d,stroke:#ef4444,color:#fecaca
```

---

## 6. Layer 4: Monitoring — Smart Alert Configuration

| Camera | Alert Trigger | Hours | Recipient |
|---|---|---|---|
| AI-360 Pool North | Person detected | After pool hours | GHS via app |
| AI-360 Pool South | Person detected | After pool hours | GHS via app |
| AI-Pro Parking | Vehicle detected | After midnight | GHS via app |
| AI-Pro Clubhouse Door | Person at door | After business hours | GHS via app |
| AI-Bullet Perimeter | Person detected | Any time | GHS via app |
| AI-Pro Front Gate LPR | Always recording | Always | No alert — review on demand |
| AI-Pro Rear Gate LPR | Always recording | Always | No alert — review on demand |

**Gate access alerts — configure in UniFi Access:**

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0c2a1a', 'lineColor': '#10b981'}}}%%
graph LR
    EVENTS["🔑 Access Events"] --> Q{"Event type?"}
    Q -->|"Normal entry"| LOG["📋 Logged only\nNo alert"]
    Q -->|"Denied — unknown credential"| ALERT1["🚨 Alert GHS\nPossible unauthorized attempt"]
    Q -->|"Door held open > threshold"| ALERT2["🚨 Alert GHS\nPossible propped door"]
    Q -->|"3+ failures same credential"| ALERT3["🚨 Alert GHS\nPossible malfunction or fob issue"]

    style EVENTS fill:#065f46,stroke:#10b981,color:#fff
    style Q fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style LOG fill:#374151,stroke:#6b7280,color:#d1d5db
    style ALERT1 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style ALERT2 fill:#7c2d12,stroke:#f97316,color:#fed7aa
    style ALERT3 fill:#92400e,stroke:#f59e0b,color:#fde68a
```

---

## 7. Layer 5: Incident Response — Escalation Path

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6366f1'}}}%%
flowchart TD
    INC(["🚨 Incident Occurs"]) --> GHS3

    subgraph TIER1["TIER 1 — GHS First Response"]
        GHS3["GHS — Sharon / Kevin\nsupport@greenvillehoa.com\n864-213-2156"]
    end

    GHS3 --> Q2{"Can GHS\nresolve?"}
    Q2 -->|"✅ Yes — routine"| RESOLVE["Handle and document\nNote in access log"]
    Q2 -->|"Board decision needed"| HOWARD["📞 Contact Howard Rapp\nhowarddalerapp@gmail.com"]
    Q2 -->|"🚔 Criminal matter"| POLICE["Call 911 immediately\nThen contact Howard"]
    Q2 -->|"🔧 Technical failure"| HOWARD

    HOWARD --> Q3{"Legal\nquestion?"}
    Q3 -->|"No"| HRESOLVE["Howard resolves\nDocuments in ARGUS log"]
    Q3 -->|"Yes / footage sharing"| LUKE["⚖️ Luke Burke\nlburke@gvlattorney.com"]
    POLICE --> LUKE

    LUKE --> LEGAL_ACT["Legal action\nas advised"]

    subgraph DOC["📋 ALWAYS DOCUMENT"]
        D1["Date + time\nWhat was observed\nAction taken\nBy whom"]
    end

    RESOLVE --> DOC
    HRESOLVE --> DOC
    LEGAL_ACT --> DOC

    style INC fill:#7f1d1d,stroke:#ef4444,color:#fff
    style TIER1 fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style GHS3 fill:#065f46,stroke:#10b981,color:#fff
    style Q2 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style RESOLVE fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style HOWARD fill:#92400e,stroke:#f59e0b,color:#fde68a
    style POLICE fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style Q3 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style HRESOLVE fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style LUKE fill:#4c1d95,stroke:#a78bfa,color:#e9d5ff
    style LEGAL_ACT fill:#1e1b4b,stroke:#6366f1,color:#c7d2fe
    style DOC fill:#1e3a5f,stroke:#60a5fa,color:#bfdbfe
```

**Common incident quick reference:**

| Incident | Immediate Response |
|---|---|
| Pool break-in / vandalism | GHS exports footage, notifies Howard. Howard contacts police if appropriate, Luke Burke if legal questions. |
| Gate stuck open | GHS attempts remote lock via dashboard. If fails, dispatch on-site. Contact Howard. |
| Unauthorized person in pool | Review footage. If pattern, trespass notice via Luke Burke. |
| Lost or stolen fob | GHS deactivates immediately in UniFi Access. Zero delay. |
| LTE outage at gate | Gates continue operating (offline mode). Visitor intercom unavailable. Howard investigates. |
| System compromise suspected | Change all admin passwords immediately. Review access logs. Notify Howard. Consult Luke Burke if data exposure possible. |

---

## 8. Layers 6 and 7: Audit, Accountability, and Legal

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#a855f7'}}}%%
graph LR
    subgraph DUTIES["SEPARATION OF DUTIES"]
        OP["🏢 GHS\nOperational layer\nResidents + credentials\nDay-to-day ops"]
        TECH["👤 Howard\nTechnical layer\nSystem config + security policy\nNo GHS config changes without approval"]
        GOV["📋 Board\nGovernance layer\nPolicy approval\nIncident review"]
        LEGAL2["⚖️ Luke Burke\nLegal layer\nData policy review\nLPR sign-off\nFootage sharing guidance"]
    end

    OP <-->|"Operations reports"| GOV
    TECH <-->|"Technical reports"| GOV
    TECH -->|"Policy questions"| LEGAL2
    GOV -->|"Directs"| OP
    GOV -->|"Directs"| TECH

    subgraph REQUIRED["⚠️ HARD REQUIREMENTS"]
        R1["Luke Burke review of LPR\ndata handling policy\nREQUIRED before Phase 3 go-live"]
        R2["Privacy notices posted\nat all camera locations\nbefore any system is live"]
        R3["Board vote to adopt\ndata handling policy\ndocumented in decisions log"]
        R4["Ables Insurance notified\nafter Phase 1 completion\n864-987-9900"]
    end

    LEGAL2 --> REQUIRED

    style DUTIES fill:#0f172a,stroke:#475569,color:#e2e8f0
    style OP fill:#065f46,stroke:#10b981,color:#fff
    style TECH fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style GOV fill:#4c1d95,stroke:#a78bfa,color:#fff
    style LEGAL2 fill:#500724,stroke:#ec4899,color:#fff
    style REQUIRED fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style R1 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style R2 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style R3 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style R4 fill:#450a0a,stroke:#ef4444,color:#fca5a5
```

---

## 9. Phase-by-Phase Security Checklists

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#10b981'}}}%%
graph LR
    subgraph P1C["✅ PHASE 1 CHECKLIST"]
        P1A["All default passwords changed\nbefore any device goes online"]
        P1B["VLAN isolation verified\ncameras can't reach other VLANs"]
        P1C2["No public-facing ports open\non UCG-Ultra"]
        P1D["UNVR recording verified\nall 5 cameras live"]
        P1E["GHS admin accounts created\nboard viewer accounts created"]
        P1F["Controller config backed up\nto ARGUS Google Drive"]
        P1G["Privacy notices posted\nclubhouse and pool locations"]
    end

    subgraph P2C["✅ PHASE 2 CHECKLIST"]
        P2A["All fobs registered\nwith resident names in UniFi Access"]
        P2B["Pool gate hours set\nto match posted pool schedule"]
        P2C2["Clubhouse door restricted\nto authorized personnel only"]
        P2D["GHS trained on\naccess log review process"]
        P2E["Incident response procedure\nshared with GHS in writing"]
        P2F["Maglock contractor work reviewed\nfire egress verified"]
    end

    subgraph P3C["⚠️ PHASE 3 CHECKLIST"]
        P3A["🔴 Luke Burke sign-off\non LPR data handling\nHARD BLOCK — DO NOT SKIP"]
        P3B["Board vote on data policy\ndocumented in decisions log"]
        P3C2["Privacy notices at\nboth gate entry points"]
        P3D["LTE stable 48h+ at each gate\nbefore cutover"]
        P3E["Offline failover tested\nLTE SIM pulled · fob still works"]
        P3F["LPR cameras capturing plates\nat entry distance"]
        P3G["Visitor intercom tested\nGHS confirmed receiving calls"]
        P3H["CPS system confirmed offline\nbefore declaring ARGUS live"]
        P3I["Ables Insurance notified\n864-987-9900"]
    end

    style P1C fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style P2C fill:#0c1e3a,stroke:#3b82f6,color:#bfdbfe
    style P3C fill:#2a0a0a,stroke:#ef4444,color:#fecaca
    style P3A fill:#450a0a,stroke:#ef4444,color:#fca5a5
```

---

*Project ARGUS | River Shoals HOA | Confidential Board Document*
*Last updated: June 2026*
