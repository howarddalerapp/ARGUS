# Project ARGUS
## River Shoals HOA — Security Infrastructure Modernization

> **Project name:** In Greek myth, Argus Panoptes was a giant with a hundred eyes — the ever-watchful guardian who never slept. The name fits a project whose purpose is community-wide visibility and access control across the clubhouse, pool, and both gates — all owned and managed by the board itself.

---

## Document Index

| Document | Purpose |
|---|---|
| **ARGUS_Project_Plan.md** (this file) | Executive summary, phases, schedule, ROI |
| **ARGUS_Tracker.md** | Budget line items, equipment list, open items, decisions log |
| **ARGUS_Network_Architecture.md** | Network diagrams, VLAN design, IP plan, camera placement |
| **ARGUS_Security_Plan.md** | Defense-in-depth security framework, policies, compliance |
| **ARGUS_Operations_Guide.md** | Plain-language how-to for GHS and board members |
| **ARGUS_Transition_Plan.md** | Zero-downtime CPS to ARGUS cutover plan |

---

## 1. Three-Site Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph LR
    subgraph CLUB["🏛️ CLUBHOUSE — Simpsonville SC"]
        CL1["Network controller\n5 cameras · 3 WiFi APs\nNVR recording\nPool + door access control\nWOW fiber WAN"]
    end

    subgraph FG["🚗 FRONT GATE\nW. Georgia Rd · ~1 mile"]
        FG1["LTE Pro cellular\nAccess Hub + LPR camera\nVideo intercom\nReader Pro\nOffline capable"]
    end

    subgraph RG["🚗 REAR GATE\nSecondary entry · ~1 mile"]
        RG1["LTE Pro cellular\nAccess Hub + LPR camera\nReader Pro\nOffline capable\nNo intercom"]
    end

    subgraph CLOUD3["☁️ UBIQUITI CLOUD\nManagement only · No footage"]
        UC3["unifi.ui.com"]
    end

    CLUB <-->|"WOW fiber\nBroadband WAN"| CLOUD3
    FG <-->|"LTE cellular"| CLOUD3
    RG <-->|"LTE cellular"| CLOUD3

    style CLUB fill:#0c2340,stroke:#3b82f6,color:#bfdbfe
    style FG fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style RG fill:#1e1b4b,stroke:#6366f1,color:#c7d2fe
    style CLOUD3 fill:#2d1a4a,stroke:#8b5cf6,color:#e9d5ff
    style CL1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style FG1 fill:#065f46,stroke:#10b981,color:#fff
    style RG1 fill:#3730a3,stroke:#6366f1,color:#fff
    style UC3 fill:#4a1d96,stroke:#8b5cf6,color:#fff
```

---

## 2. Project Summary

| Field | Detail |
|---|---|
| Community | River Shoals HOA, Simpsonville SC — 280+ lots |
| Objective | Replace CPS vendor-managed security with board-owned Ubiquiti UniFi |
| Equipment Budget | ~$8,305 before SC sales tax (~$8,886 with tax at 7%) |
| Ongoing Operating Cost | ~$50-70/month for 2× LTE SIM plans at gates |
| Installation Lead | Howard Rapp — operates identical UniFi system at personal residence |
| Outside Labor | One licensed contractor for clubhouse door maglock only |
| WOW Fiber | Available at clubhouse at no install cost — coordinate with Rico Pruitt via GHS |
| Hands-on Start | Early August 2026 (deferred until after July travel) |
| Attorney Hard Block | Luke Burke review of LPR data handling policy required before Phase 3 |

---

## 3. Three Phases

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph LR
    subgraph PH1["PHASE 1 — Clubhouse Foundation\n~$3,565 · ~17 hrs self-install"]
        P1["📷 5 cameras\n💾 NVR / CGMax\n⚡ PoE switch\n📶 3 WiFi APs\n🌐 WOW fiber termination\n🖥️ Network controller setup"]
    end

    subgraph PH2["PHASE 2 — Pool + Door Access\n~$2,372 · ~9 hrs + 1 contractor"]
        P2["🔑 Pool gate RFID replacement\n🚪 Clubhouse door access control\n🔒 Maglock — licensed contractor\n🪪 Resident fob issuance ~100 initial"]
    end

    subgraph PH3["PHASE 3 — Vehicle Gates\n~$2,368 · ~13 hrs self-install"]
        P3["📡 LTE Pro × 2 at both gates\n🔑 Gate access control × 2\n🔔 Video intercom — front gate\n📷 LPR cameras × 2\n⚖️ Luke Burke sign-off required"]
    end

    PH1 -->|"Aug 1-14"| PH2
    PH2 -->|"Aug 15-31"| PH3

    style PH1 fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style PH2 fill:#0c2340,stroke:#3b82f6,color:#bfdbfe
    style PH3 fill:#2a1200,stroke:#f97316,color:#fed7aa
    style P1 fill:#0d3321,stroke:#10b981,color:#fff
    style P2 fill:#0d1f3a,stroke:#3b82f6,color:#fff
    style P3 fill:#1f0d00,stroke:#f97316,color:#fff
```

---

## 4. Full Project Schedule

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
gantt
    title Project ARGUS — Full Installation Schedule
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Pre-Installation
        Board vote + equipment order     :active, pre1, 2026-06-01, 2026-06-15
        Architecture decision CGMax vs UCG :crit, pre2, 2026-06-01, 2026-06-10
        WOW fiber scheduling with Rico   :pre3, 2026-06-01, 2026-06-20
        SIM procurement — 2x LTE        :pre4, 2026-06-10, 2026-06-30
        Equipment arrives                :milestone, eq, 2026-06-30, 1d

    section BLOCKED — Howard Traveling
        July travel period               :crit, travel, 2026-07-01, 2026-07-31

    section Phase 1 — Clubhouse
        Controller + switch + UNVR setup :p1a, 2026-08-01, 2026-08-05
        5 cameras install + test         :p1b, 2026-08-05, 2026-08-10
        3 WiFi APs install               :p1c, 2026-08-08, 2026-08-12
        WOW fiber termination            :p1d, 2026-08-10, 2026-08-14
        Camera system cutover from CPS   :milestone, m1, 2026-08-14, 1d

    section Phase 2 — Pool + Door
        Fob ordering + pre-registration  :p2a, 2026-08-01, 2026-08-20
        Maglock contractor               :p2b, 2026-08-15, 2026-08-22
        Pool + door access hub install   :p2c, 2026-08-20, 2026-08-28
        Fob distribution to residents    :p2d, 2026-08-15, 2026-08-28
        Pool + door cutover              :milestone, m2, 2026-08-28, 1d

    section Phase 3 — Gates
        Luke Burke LPR policy review     :crit, lb, 2026-08-01, 2026-08-31
        LTE Pros install + test          :p3a, 2026-09-01, 2026-09-06
        Gate hubs + readers install      :p3b, 2026-09-06, 2026-09-10
        Front gate cutover               :milestone, m3, 2026-09-10, 1d
        Rear gate cutover                :milestone, m4, 2026-09-14, 1d

    section Closeout
        CPS termination                  :close1, 2026-09-20, 2026-10-01
        As-built documentation           :close2, 2026-09-20, 2026-09-30
        Insurance notification           :milestone, ins, 2026-09-30, 1d
        Final board report               :close3, 2026-10-01, 2026-10-07
```

---

## 5. ROI Analysis

### Known CPS Costs from Email Records

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'xyChart': {'backgroundColor': '#0f172a', 'plotColorPalette': '#ef4444'}}}}%%
xychart-beta
    title "Confirmed CPS Invoices (from email records)"
    x-axis ["Invoice 66366\n~2024\nGate repairs", "Call box\nMar 2025\nFront gate", "Surge protectors\nFeb 2025\nEstimate 19374", "Invoice 95670\nDec 2025\nGate repairs"]
    y-axis "Amount ($)" 0 --> 50000
    bar [45000, 6500, 1962, 4000]
```

| Date | Invoice | Amount | Description |
|---|---|---|---|
| ~2024 | Invoice 66366 | **$45,000** | Gate repairs — loop work (2024/2025) |
| Feb 2025 | Estimate 19374 | **$1,962** | Surge protectors |
| Mar 2025 | Board approval | **$6,500** | Front gate call box replacement |
| Dec 2025 | Invoice 95670 | **$4,000** | Gate repairs |
| Mar 2025 | Keypad invoice | **TBD** | Front gate keypad |
| Various | Camera work | **TBD** | $750/camera replacement rate |

**Confirmed minimum from email records: $57,462 over ~24 months**

> GHS has been asked to pull complete CPS invoice history from CINC to establish the full annual figure.

### ARGUS vs CPS — Break-Even Analysis

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'xyChart': {'backgroundColor': '#0f172a', 'plotColorPalette': '#10b981,#ef4444'}}}}%%
xychart-beta
    title "Cumulative Cost: CPS vs ARGUS (at $30K/yr CPS estimate)"
    x-axis ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
    y-axis "Cumulative Cost ($)" 0 --> 160000
    bar [30000, 60000, 90000, 120000, 150000]
    line [9806, 10726, 11646, 12566, 13486]
```

| Annual CPS Savings Estimate | Break-Even Point |
|---|---|
| $20,000/year | ~5.4 months |
| $30,000/year | ~3.6 months |
| $40,000/year | ~2.7 months |

**ARGUS annual operating cost:** ~$920/year (LTE SIMs + consumables)
**ARGUS one-time equipment:** ~$8,886 with SC tax

The $45,000 single gate repair invoice alone exceeds the entire ARGUS equipment budget.

---

## 6. System Access and Roles

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph TD
    subgraph ROLES["🔐 ARGUS SYSTEM ACCESS ROLES"]
        SA["👤 Howard Rapp\nSuper Admin\nSystem owner · Installer\nSole technical resource\nAll three UniFi apps\nAll configuration"]

        AD["🏢 GHS — Sharon + Kevin Bragman\nAdmin\nsupport@greenvillehoa.com\nkbragman@greenvillehoa.com\nDay-to-day ops\nFob management\nIncident first response"]

        VW["📋 Board — Viewer\nAllison Hanline\nDave Arnold\nRuth Jansen\nMaynard Bates\nM. Broskie\nView cameras + access logs\nCannot make changes"]

        LEGAL3["⚖️ Luke Burke\nExternal\nlburke@gvlattorney.com\nLPR data policy sign-off\nNo system access"]
    end

    SA --> AD
    SA --> VW
    SA -.->|"Consults before Phase 3"| LEGAL3

    style ROLES fill:#0f172a,stroke:#475569,color:#e2e8f0
    style SA fill:#7c2d12,stroke:#f97316,color:#fff
    style AD fill:#065f46,stroke:#10b981,color:#fff
    style VW fill:#1e1b4b,stroke:#6366f1,color:#fff
    style LEGAL3 fill:#4c1d95,stroke:#a78bfa,color:#fff
```

---

## 7. Critical Prerequisites — Nothing Moves Without These

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#ef4444'}}}%%
graph LR
    subgraph HARD["🔴 HARD BLOCKS — Cannot Proceed Without"]
        H1["Board vote approving\nfull budget\n~$8,886 equipment\n+ ~$720/yr LTE"]
        H2["Architecture decision:\nUCG-Ultra + UNVR\nvs. Cloud Gateway Max"]
        H3["🔴 Luke Burke sign-off\non LPR data handling policy\nPHASE 3 BLOCKED until done"]
    end

    subgraph PEND["🟡 PENDING — Must Complete Pre-Install"]
        P1["WOW fiber scheduling\nwith Rico Pruitt via GHS"]
        P2["2× LTE SIMs procured\nbefore Phase 3"]
        P3["Maglock contractor\nidentified and scheduled\nfor Phase 2"]
        P4["Full CPS invoice history\nfrom GHS — for ROI finalization"]
    end

    style HARD fill:#450a0a,stroke:#ef4444,color:#fecaca
    style PEND fill:#431407,stroke:#f59e0b,color:#fde68a
    style H1 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style H2 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style H3 fill:#450a0a,stroke:#ef4444,color:#fca5a5
    style P1 fill:#92400e,stroke:#f59e0b,color:#fff
    style P2 fill:#92400e,stroke:#f59e0b,color:#fff
    style P3 fill:#92400e,stroke:#f59e0b,color:#fff
    style P4 fill:#92400e,stroke:#f59e0b,color:#fff
```

---

## 8. Key Contacts

| Role | Name | Contact |
|---|---|---|
| System Owner / Installer | Howard Rapp | howarddalerapp@gmail.com |
| WOW Fiber | Rico Pruitt (via GHS) | support@greenvillehoa.com |
| HOA Attorney | Luke Burke | lburke@gvlattorney.com |
| Property Management | Sharon / Kevin Bragman | support@greenvillehoa.com · kbragman@greenvillehoa.com |
| Insurance | Ables Insurance | 864-987-9900 |
| CPS (current vendor) | AR department | AR@cpsgreenville.com |

---

*Project ARGUS | River Shoals HOA | Confidential Board Document*
*Last updated: June 2026*
