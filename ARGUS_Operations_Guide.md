# Project ARGUS — Operations Guide
## River Shoals HOA | How-To Guide for GHS and Board Members

*Last updated: June 2026 | Written for non-technical users*

> **Before you start:** Everything in this guide is done through the **UniFi dashboard** at `unifi.ui.com`. You do not need to touch any hardware for day-to-day operations. If you encounter something not covered here, stop and contact Howard Rapp before making changes.

---

## Quick Reference

| What I need to do | Section |
|---|---|
| Watch live cameras | Section 2 |
| Review recorded footage after an incident | Section 3 |
| Add a new resident's fob | Section 4 |
| Deactivate a lost or surrendered fob | Section 5 |
| Let a visitor in through the front gate | Section 6 |
| Unlock a door or gate remotely | Section 7 |
| Troubleshoot a resident who can't get in | Section 8 |
| Something is broken | Section 9 |
| Who to call for what | Section 10 |
| Monthly routine tasks | Section 11 |
| What each device is | Section 12 |

---

## System Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#60a5fa'}}}%%
graph TD
    subgraph DASHBOARD["🖥️ unifi.ui.com — Your Control Center"]
        subgraph PROTECT["📷 UniFi Protect"]
            PR1["Live camera feeds"]
            PR2["Recorded footage + timeline"]
            PR3["Motion event clips"]
            PR4["Export footage for incidents"]
        end
        subgraph ACCESS["🔑 UniFi Access"]
            AC1["Add / deactivate fobs"]
            AC2["Access logs — who entered when"]
            AC3["Remote door / gate unlock"]
            AC4["Visitor intercom calls"]
        end
        subgraph NETWORK["🌐 UniFi Network"]
            NET1["WiFi management\nHoward only — do not touch"]
        end
    end

    GHS_USER["🏢 GHS\nAdmin access"] -->|"Daily operations"| PROTECT & ACCESS
    BOARD_USER["📋 Board Members\nViewer access"] -->|"Review only"| PROTECT & ACCESS
    HOWARD_USER["👤 Howard Rapp\nSuper Admin"] -->|"All three apps"| DASHBOARD

    style DASHBOARD fill:#0f172a,stroke:#3b82f6,color:#bfdbfe
    style PROTECT fill:#2e1065,stroke:#a78bfa,color:#e9d5ff
    style ACCESS fill:#431407,stroke:#f59e0b,color:#fde68a
    style NETWORK fill:#0c2340,stroke:#3b82f6,color:#bfdbfe
    style GHS_USER fill:#065f46,stroke:#10b981,color:#fff
    style BOARD_USER fill:#1e1b4b,stroke:#6366f1,color:#fff
    style HOWARD_USER fill:#7c2d12,stroke:#f97316,color:#fff
```

---

## Section 1 — Logging In

**Web address:** `https://unifi.ui.com`

Your login is your email address plus the password Howard set up for your account.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#10b981'}}}%%
flowchart LR
    GO["Open browser\nGo to unifi.ui.com"] --> LOGIN2["Enter email + password"]
    LOGIN2 --> Q{"Login OK?"}
    Q -->|"✅ Yes"| DASH["Dashboard loads\nSelect Protect or Access\nfrom left sidebar"]
    Q -->|"❌ Forgot password"| RESET["Click Forgot Password\nCheck your email\nFollow reset link"]
    Q -->|"❌ Still can't login"| HOWARD2["Contact Howard Rapp\nhowarddalerapp@gmail.com"]

    style GO fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style LOGIN2 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style Q fill:#0e7490,stroke:#06b6d4,color:#fff
    style DASH fill:#065f46,stroke:#10b981,color:#fff
    style RESET fill:#92400e,stroke:#f59e0b,color:#fff
    style HOWARD2 fill:#7f1d1d,stroke:#ef4444,color:#fff
```

> GHS (Sharon and Kevin) have **Admin** access — view cameras, manage fobs, unlock doors.
> Board members have **Viewer** access — view cameras and access logs only, no changes.

---

## Section 2 — Watching Live Cameras

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#a78bfa'}}}%%
flowchart LR
    S1["1. Log in to\nunifi.ui.com"] --> S2["2. Click Protect\n📷 camera icon\nin left sidebar"]
    S2 --> S3["3. Camera grid\nappears — all feeds\nare live and real-time"]
    S3 --> S4{"What do\nyou need?"}
    S4 -->|"Full screen one camera"| S5["Click any camera\nto expand it"]
    S4 -->|"Back to grid"| S6["Click grid icon\ntop right corner"]
    S4 -->|"Zoom in"| S7["Scroll mouse wheel\nor pinch on tablet"]
    S4 -->|"Camera showing grey"| S8["Camera may be offline\nNote camera name\nContact Howard"]

    style S1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style S2 fill:#2e1065,stroke:#a78bfa,color:#fff
    style S3 fill:#065f46,stroke:#10b981,color:#fff
    style S4 fill:#0e7490,stroke:#06b6d4,color:#fff
    style S5 fill:#065f46,stroke:#10b981,color:#fff
    style S6 fill:#065f46,stroke:#10b981,color:#fff
    style S7 fill:#065f46,stroke:#10b981,color:#fff
    style S8 fill:#7f1d1d,stroke:#ef4444,color:#fff
```

---

## Section 3 — Reviewing Recorded Footage

> ⚠️ **Critical:** Footage is kept for approximately **30 days only**. Export any footage needed for incidents before the window closes — it cannot be recovered once overwritten.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#a78bfa'}}}%%
flowchart TD
    R1["1. Log in → Protect\nClick the camera to review"] --> R2["2. Timeline bar appears\nat bottom of screen\nCovers last 30 days"]
    R2 --> R3["3. Click on the timeline\nto jump to any time\nUse playback controls"]
    R3 --> Q4{"How to find\nthe moment fast?"}
    Q4 -->|"Know approximate time"| R4["Click timeline at\nthe right time"]
    Q4 -->|"Looking for motion events"| R5["Click Events tab\n⚡ lightning bolt icon\nShows all detected motion\nClick any event to jump to it"]
    R3 --> EXPORT{"Need to save\nthe footage?"}
    EXPORT -->|"Yes — for an incident"| EX1["Click Export button\n⬇️ download arrow icon\nSet start + end time\nClick Export → saves as MP4"]
    EX1 --> EX2{"Legal matter?"}
    EX2 -->|"Yes"| EX3["Do NOT share with anyone\nuntil Howard and Luke Burke advise"]
    EX2 -->|"No"| EX4["Save file securely\nNote date · time · camera name"]

    style R1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style R2 fill:#2e1065,stroke:#a78bfa,color:#fff
    style R3 fill:#2e1065,stroke:#a78bfa,color:#fff
    style Q4 fill:#0e7490,stroke:#06b6d4,color:#fff
    style R4 fill:#065f46,stroke:#10b981,color:#fff
    style R5 fill:#065f46,stroke:#10b981,color:#fff
    style EXPORT fill:#0e7490,stroke:#06b6d4,color:#fff
    style EX1 fill:#92400e,stroke:#f59e0b,color:#fff
    style EX2 fill:#0e7490,stroke:#06b6d4,color:#fff
    style EX3 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style EX4 fill:#065f46,stroke:#10b981,color:#fff
```

---

## Section 4 — Adding a New Resident's Fob

**You need first:** Resident name, lot address, and the fob number (printed on the back of the fob, usually 8-10 digits).

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#f59e0b'}}}%%
flowchart TD
    A1["1. Log in → Access\n🔑 key icon in sidebar"] --> A2["2. Click Users\nin the top menu"]
    A2 --> A3["3. Click + button\ntop right corner\nAdd User"]
    A3 --> A4["4. Fill in:\nFirst name · Last name\nEmail optional but useful"]
    A4 --> A5["5. Under Credentials\nclick Add Credential\nSelect NFC / Fob"]
    A5 --> A6{"How to enter\nfob number?"}
    A6 -->|"Type it manually"| A7["Type the fob number\nfrom label on back of fob"]
    A6 -->|"Scan the fob"| A8["Click Scan\nHold fob to any Reader\nNumber auto-fills"]
    A7 --> A9["6. Under Access Policies\nselect zones:"]
    A8 --> A9
    A9 --> A10["✅ Vehicle Gate — front + rear\n✅ Pool Gate\n❌ Clubhouse Door — not by default"]
    A10 --> A11["7. Click Save\nFob is active immediately"]
    A11 --> A12["Test: Ask resident to\ntry fob at pool or gate\nCheck Access Log to confirm"]

    style A1 fill:#92400e,stroke:#f59e0b,color:#fff
    style A2 fill:#92400e,stroke:#f59e0b,color:#fff
    style A3 fill:#92400e,stroke:#f59e0b,color:#fff
    style A4 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style A5 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style A6 fill:#0e7490,stroke:#06b6d4,color:#fff
    style A7 fill:#065f46,stroke:#10b981,color:#fff
    style A8 fill:#065f46,stroke:#10b981,color:#fff
    style A9 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style A10 fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style A11 fill:#065f46,stroke:#10b981,color:#fff
    style A12 fill:#065f46,stroke:#10b981,color:#fff
```

---

## Section 5 — Deactivating a Fob

> ⚠️ **Do this immediately** when a resident moves out, reports a fob lost or stolen, or a fob is not returned. A deactivated fob grants zero access even if someone still has the physical fob.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#ef4444'}}}%%
flowchart TD
    D1["1. Log in → Access → Users"] --> D2["2. Search for the resident\nby name or address"]
    D2 --> D3["3. Click their name\nto open their profile"]
    D3 --> D4["4. Under Credentials\nfind their fob"]
    D4 --> D5{"Temporary or\npermanent?"}
    D5 -->|"Temporary — resident still active"| D6["Toggle the fob OFF\ngrey means disabled\nClick Save"]
    D5 -->|"Permanent — resident leaving"| D7["Click Suspend User\nor Delete the profile entirely"]
    D6 --> D8["✅ Fob is dead immediately\nPhysical fob is useless"]
    D7 --> D8
    D8 --> D9["Document the change:\nDate · reason · who requested\nIn access management log"]

    style D1 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style D2 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style D3 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style D4 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style D5 fill:#0e7490,stroke:#06b6d4,color:#fff
    style D6 fill:#92400e,stroke:#f59e0b,color:#fff
    style D7 fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style D8 fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style D9 fill:#1e3a5f,stroke:#3b82f6,color:#fff
```

---

## Section 6 — Letting a Visitor in Through the Front Gate

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#8b5cf6'}}}%%
flowchart LR
    VIS["👤 Visitor arrives\nat front gate\nPresses intercom button"] --> RING["📱 Call rings to\nGHS app on phone\nor computer notification"]
    RING --> GHS_ANS{"GHS available?"}
    GHS_ANS -->|"✅ Yes"| ANS["Open UniFi Access app\nTap Answer\nLive video of visitor appears\nTwo-way audio active"]
    GHS_ANS -->|"❌ No answer"| VIS2["Call also rings to\nHoward if configured\nVisitor must contact resident directly"]
    ANS --> DECIDE{"Grant access?"}
    DECIDE -->|"✅ Yes"| UNLOCK2["Tap Unlock Gate\nGate opens ~15 seconds"]
    DECIDE -->|"❌ No"| DECLINE["Tap Decline or hang up\nGate stays closed"]
    UNLOCK2 --> DONE2["✅ Visitor enters\nGate closes automatically"]

    style VIS fill:#4a1d96,stroke:#8b5cf6,color:#fff
    style RING fill:#4a1d96,stroke:#8b5cf6,color:#fff
    style GHS_ANS fill:#0e7490,stroke:#06b6d4,color:#fff
    style ANS fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style VIS2 fill:#374151,stroke:#6b7280,color:#fff
    style DECIDE fill:#0e7490,stroke:#06b6d4,color:#fff
    style UNLOCK2 fill:#065f46,stroke:#10b981,color:#fff
    style DECLINE fill:#7f1d1d,stroke:#ef4444,color:#fff
    style DONE2 fill:#14532d,stroke:#22c55e,color:#bbf7d0
```

> The rear gate has no intercom. Rear gate is for credentialed residents and service vehicles with fobs only.

---

## Section 7 — Unlocking a Door or Gate Remotely

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#06b6d4'}}}%%
flowchart TD
    U1["1. Log in → Access → Devices\nList of all doors and gates appears"] --> U2["2. Click the device\nyou want to unlock:\nPool Gate · Clubhouse Door\nFront Gate · Rear Gate"]
    U2 --> U3{"What type\nof unlock?"}
    U3 -->|"Immediate — let someone in now"| U4["Click Unlock 🔓\nDoor opens immediately\nRe-locks after 10-15 seconds automatically"]
    U3 -->|"Timed window — event or maintenance"| U5["Click Schedule or Hold Open\nSet start time · end time · date\nSave — gate re-locks at end automatically"]
    U4 --> U6["✅ Done\nNo resident needs to be present"]
    U5 --> U7["✅ Gate stays unlocked\nduring the window only"]

    style U1 fill:#0e7490,stroke:#06b6d4,color:#fff
    style U2 fill:#0e7490,stroke:#06b6d4,color:#fff
    style U3 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style U4 fill:#065f46,stroke:#10b981,color:#fff
    style U5 fill:#92400e,stroke:#f59e0b,color:#fff
    style U6 fill:#14532d,stroke:#22c55e,color:#bbf7d0
    style U7 fill:#14532d,stroke:#22c55e,color:#bbf7d0
```

---

## Section 8 — Resident Can't Get In (Troubleshooting)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#f59e0b'}}}%%
flowchart TD
    PROB(["📞 Resident reports\ncan't get in"]) --> S1["Step 1: Check credential\nAccess → Users → Find resident\nIs fob toggled ON?"]
    S1 --> Q1{"Fob status?"}
    Q1 -->|"Disabled — toggle is grey"| FIX1["Re-enable fob\nClick toggle → ON → Save\nTest immediately"]
    Q1 -->|"Active — toggle is green"| S2["Step 2: Check if using\nfob correctly\nMust hold within 1-2 inches\nNFC phone needs Access app open"]
    S2 --> S3["Step 3: Check Access Log\nAccess → Access Log\nSearch resident name or credential ID"]
    S3 --> Q2{"What does\nlog show?"}
    Q2 -->|"Denied — credential seen"| FIX2["Wrong zone or outside schedule\nCheck access policy\nFix zone assignment"]
    Q2 -->|"Not appearing at all"| FIX3["Reader never saw fob\nWrong fob · not registered\nor reader hardware issue"]
    Q2 -->|"Not sure"| S4["Step 4: Test reader yourself\nTry your own admin fob\nat that specific reader"]
    FIX3 --> S4
    S4 --> Q3{"Your fob\nworks?"}
    Q3 -->|"✅ Yes"| FIX4["Resident fob issue\nRe-register their fob\nor issue a replacement"]
    Q3 -->|"❌ No"| FIX5["Reader or hub is down\nCheck Devices in Access\nContact Howard"]
    PROB --> TEMP["Meanwhile:\nUse remote unlock\nSection 7 to let them in now"]

    style PROB fill:#7c2d12,stroke:#f97316,color:#fff
    style S1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style Q1 fill:#0e7490,stroke:#06b6d4,color:#fff
    style FIX1 fill:#065f46,stroke:#10b981,color:#fff
    style S2 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style S3 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style Q2 fill:#0e7490,stroke:#06b6d4,color:#fff
    style FIX2 fill:#92400e,stroke:#f59e0b,color:#fff
    style FIX3 fill:#92400e,stroke:#f59e0b,color:#fff
    style S4 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style Q3 fill:#0e7490,stroke:#06b6d4,color:#fff
    style FIX4 fill:#065f46,stroke:#10b981,color:#fff
    style FIX5 fill:#7f1d1d,stroke:#ef4444,color:#fff
    style TEMP fill:#14532d,stroke:#22c55e,color:#bbf7d0
```

---

## Section 9 — Something Is Broken

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#ef4444'}}}%%
flowchart TD
    ISSUE(["⚠️ Something wrong"]) --> Q{"What is\nthe problem?"}

    Q -->|"Camera shows grey/offline"| CA["Check Protect → Devices\nIs camera status Offline?\nNote camera name\nContact Howard — do not reset hardware"]

    Q -->|"Gate stuck open"| GA["Access → Devices → Gate\nIs device Connected?\nTry remote lock via dashboard\nIf fails → gate operator manual override exists\nContact Howard immediately"]

    Q -->|"Gate won't open for anyone"| GA2["Check Access → Devices\nIs hub Offline?\nLTE may be down — offline mode active\nResident fobs still work\nVisitor intercom unavailable\nContact Howard"]

    Q -->|"Can't login to dashboard"| DA["Try different browser or device\nCheck your internet connection\nCheck status.ui.com for Ubiquiti outage\nIf still down → Contact Howard"]

    Q -->|"Accidentally changed something"| ACC["STOP — do not try to fix it\nNote exactly what you changed\nContact Howard immediately"]

    CA --> HOWARD3["📞 Howard Rapp\nhowarddalerapp@gmail.com"]
    GA --> HOWARD3
    GA2 --> HOWARD3
    DA --> HOWARD3
    ACC --> HOWARD3

    style ISSUE fill:#7f1d1d,stroke:#ef4444,color:#fff
    style Q fill:#0e7490,stroke:#06b6d4,color:#fff
    style CA fill:#92400e,stroke:#f59e0b,color:#fff
    style GA fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style GA2 fill:#7c2d12,stroke:#f97316,color:#fed7aa
    style DA fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style ACC fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style HOWARD3 fill:#065f46,stroke:#10b981,color:#fff
```

---

## Section 10 — Who to Call for What

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph LR
    subgraph TIER1B["TIER 1 — GHS handles directly"]
        T1A["New resident fob"]
        T1B["Resident moving out — deactivate"]
        T1C["Footage request for incident"]
        T1D["Gate stuck — attempt remote fix"]
        T1E["Resident can't get in"]
    end

    subgraph TIER2B["TIER 2 — Escalate to Howard"]
        T2A["Camera offline"]
        T2B["Gate issue GHS can't resolve"]
        T2C["System technical failure"]
        T2D["Legal question about footage"]
        T2E["LTE outage at gate"]
    end

    subgraph TIER3B["TIER 3 — Howard escalates to Luke"]
        T3A["Sharing footage with\nlaw enforcement"]
        T3B["Suspected criminal matter"]
        T3C["Any legal question"]
    end

    subgraph EMERGENCY["🚔 EMERGENCY"]
        E1["Suspected crime in progress\nCall 911 first\nThen notify Howard"]
    end

    subgraph INSURANCE["🏦 INSURANCE"]
        I1["Policy questions\nAbles Insurance\n864-987-9900"]
    end

    style TIER1B fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style TIER2B fill:#0c1e3a,stroke:#3b82f6,color:#bfdbfe
    style TIER3B fill:#1e1b4b,stroke:#8b5cf6,color:#e9d5ff
    style EMERGENCY fill:#7f1d1d,stroke:#ef4444,color:#fecaca
    style INSURANCE fill:#0e4429,stroke:#16a34a,color:#bbf7d0
```

| Contact | Role | How to reach |
|---|---|---|
| Howard Rapp | System owner / technical | howarddalerapp@gmail.com |
| GHS | Operations | support@greenvillehoa.com · 864-213-2156 |
| Luke Burke | HOA attorney | lburke@gvlattorney.com |
| Ables Insurance | E&O/D&O policy | 864-987-9900 |

---

## Section 11 — Monthly Routine (GHS)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#06b6d4'}}}%%
graph LR
    subgraph WEEKLY["📅 WEEKLY"]
        W1["Scan access logs\nfor anomalies:\nDenied entries\nUnusual times\nRepeated failures"]
        W2["Check all cameras\nshow Connected status\nin UniFi Protect"]
        W3["Check all Access Hubs\nshow Connected status\nin UniFi Access"]
    end

    subgraph MONTHLY["📅 MONTHLY"]
        M1["Full access log review\nFlag anything unusual\nfor board"]
        M2["Fob roster check\nMatch against current residents\nDeactivate any stale fobs"]
        M3["Confirm UNVR recording\nCheck last timestamp\nfor each camera"]
        M4["Brief status note\nto Howard:\nunusual · resolved issues\nequipment concerns"]
    end

    subgraph INCIDENT["🚨 AFTER ANY INCIDENT"]
        I1["Export footage\nIMMEDIATELY\n30-day window"]
        I2["Document incident:\nDate · what observed\naction taken"]
        I3["Notify Howard\nif significant"]
    end

    style WEEKLY fill:#0c2340,stroke:#3b82f6,color:#bfdbfe
    style MONTHLY fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style INCIDENT fill:#7f1d1d,stroke:#ef4444,color:#fecaca
```

---

## Section 12 — What Each Device Does (Plain Language)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph TD
    subgraph NETWORK2["🌐 NETWORKING DEVICES — Clubhouse closet"]
        UCG3["🖥️ UCG-Ultra or CGMax\nThe brain of the network\nConnects everything to internet\nRoutes traffic between devices"]
        SW3["⚡ PoE Switch\nPower strip + traffic director\nSends power AND data\nover Ethernet to cameras and hubs"]
    end

    subgraph RECORDING["💾 RECORDING — Clubhouse closet"]
        UNVR6["💾 UNVR\nThe camera recorder\nAll video stored here\nIf UNVR is down: cameras still show\nlive but nothing is being saved"]
    end

    subgraph CAMERAS2["📷 CAMERAS — Various locations"]
        AI360["AI-360 Camera\nSees in ALL directions at once\n360° fisheye · No blind spots\nUsed on pool deck"]
        AIPRO["AI-Pro Camera\nHigh-res directional\nCaptures faces and license plates\nUsed at parking lot · door · gates"]
        AIBULLET["AI-Bullet Camera\nLong-range directional\nIR range 100+ feet\nUsed on perimeter fence"]
    end

    subgraph ACCESS2["🔑 ACCESS DEVICES — Gates + doors"]
        ACHUB2["Access Hub\nSmall box controlling a door or gate\nTalks to readers · tells lock to open\nHas credential cache — works offline"]
        READPRO["Reader Pro\nBlack panel where you tap fob\nReads fob · sends to Access Hub"]
        READLITE["Reader Lite\nSmaller Reader Pro\nUsed on exit side of pool gate"]
        LTE2["LTE Pro\nCellular modem at each gate\nGives gate its own internet\nNo wires needed between sites"]
        INTERCOM2["AI-Theta-Pro\nVideo intercom at front gate\nVisitor presses button\nGHS answers · sees visitor · opens gate"]
    end

    style NETWORK2 fill:#0c2340,stroke:#3b82f6,color:#bfdbfe
    style RECORDING fill:#2e1065,stroke:#a78bfa,color:#e9d5ff
    style CAMERAS2 fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style ACCESS2 fill:#431407,stroke:#f59e0b,color:#fde68a
    style UCG3 fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style SW3 fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style UNVR6 fill:#4c1d95,stroke:#a78bfa,color:#fff
    style AI360 fill:#065f46,stroke:#10b981,color:#fff
    style AIPRO fill:#065f46,stroke:#10b981,color:#fff
    style AIBULLET fill:#065f46,stroke:#10b981,color:#fff
    style ACHUB2 fill:#92400e,stroke:#f59e0b,color:#fff
    style READPRO fill:#78350f,stroke:#fbbf24,color:#fff
    style READLITE fill:#78350f,stroke:#fbbf24,color:#fff
    style LTE2 fill:#1e40af,stroke:#3b82f6,color:#fff
    style INTERCOM2 fill:#4a1d96,stroke:#8b5cf6,color:#fff
```

---

*Project ARGUS | River Shoals HOA*
*Questions: GHS at support@greenvillehoa.com or Howard Rapp at howarddalerapp@gmail.com*
*Last updated: June 2026*
