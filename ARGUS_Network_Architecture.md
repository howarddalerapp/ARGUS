# Project ARGUS — Network Architecture
## River Shoals HOA | Infrastructure Design Reference

*Last updated: June 2026 | Owner: Howard Rapp*

---

## 1. Site Overview

River Shoals HOA has three distinct physical locations that make up the ARGUS security infrastructure.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1e3a5f', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#3b82f6', 'lineColor': '#60a5fa', 'secondaryColor': '#0f2744', 'tertiaryColor': '#162032'}}}%%
graph LR
    subgraph CLUBHOUSE["🏛️  CLUBHOUSE  —  Main Hub"]
        direction TB
        C1[WOW Fiber\nBroadband WAN]
        C2[Network Controller\nAll equipment here]
        C3[5 Cameras\nFull HD Recording]
        C4[Pool + Door\nAccess Control]
    end

    subgraph FGATE["🚗  FRONT GATE  —  W. Georgia Rd"]
        direction TB
        F1[LTE Pro\nCellular WAN]
        F2[Access Hub\nOffline Capable]
        F3[AI-Theta-Pro\nVisitor Intercom]
        F4[LPR Camera\nPlate Recognition]
    end

    subgraph RGATE["🚗  REAR GATE  —  Secondary Entry"]
        direction TB
        R1[LTE Pro\nCellular WAN]
        R2[Access Hub\nOffline Capable]
        R3[LPR Camera\nPlate Recognition]
    end

    subgraph CLOUD["☁️  UBIQUITI CLOUD  —  Remote Management"]
        UC[unifi.ui.com\nHTTPS Only]
    end

    CLUBHOUSE <-->|"HTTPS / STUN\nEncrypted tunnel"| CLOUD
    FGATE <-->|"HTTPS / STUN\nCellular"| CLOUD
    RGATE <-->|"HTTPS / STUN\nCellular"| CLOUD

    style CLUBHOUSE fill:#1a3a5c,stroke:#3b82f6,color:#e2e8f0
    style FGATE fill:#1a3a2c,stroke:#10b981,color:#e2e8f0
    style RGATE fill:#1a2a3a,stroke:#06b6d4,color:#e2e8f0
    style CLOUD fill:#2d1a4a,stroke:#8b5cf6,color:#e2e8f0
```

| Site | Distance | Connectivity | Power |
|---|---|---|---|
| Clubhouse | Central hub | WOW fiber broadband | Existing AC |
| Front Gate (W. Georgia Rd) | ~1 mile from clubhouse | LTE Pro cellular | Existing AC |
| Rear Gate | ~1 mile from clubhouse | LTE Pro cellular | Existing AC |

---

## 2. Clubhouse Network — Physical Topology

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f2744', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#3b82f6', 'lineColor': '#60a5fa', 'background': '#0a1628'}}}%%
graph TD
    WOW["🌐 WOW FIBER\nBroadband WAN"]
    UCG["🖥️ UCG-Ultra or CGMax\nGateway · Controller · Firewall\n192.168.1.1"]
    SW["⚡ USW-Lite-8-POE\nManaged PoE Switch\n192.168.1.20"]
    UNVR["💾 UNVR\nCamera Recorder\n2 × 4TB HDD · ~30 day retention\n192.168.1.10"]
    CAM360A["📷 AI-360 · Pool Deck North\n192.168.10.11"]
    CAM360B["📷 AI-360 · Pool Deck South\n192.168.10.12"]
    CAMPRO1["📷 AI-Pro · Parking Lot\n192.168.10.13"]
    CAMPRO2["📷 AI-Pro · Clubhouse Door\n192.168.10.14"]
    CAMBULLET["📷 AI-Bullet · Perimeter Fence\n192.168.10.15"]
    AP1["📶 U6 Mesh · Pool Area\n192.168.1.31"]
    AP2["📶 U6 Mesh · Patio\n192.168.1.32"]
    AP3["📶 U6 Extender\n192.168.1.33"]
    HUB1["🔑 Access Hub · Pool Gate\n192.168.20.11"]
    HUB2["🔑 Access Hub · Clubhouse Door\n192.168.20.12"]
    READER1["👆 Reader Pro · Pool Entry"]
    READER2["👆 Reader Lite · Pool Exit"]
    READER3["👆 Reader Pro · Clubhouse Door"]
    MAGLOCK["🔒 Maglock\nContractor Install"]

    WOW -->|WAN| UCG
    UCG -->|LAN trunk| SW
    SW -->|PoE| UNVR
    SW -->|PoE VLAN 10| CAM360A
    SW -->|PoE VLAN 10| CAM360B
    SW -->|PoE VLAN 10| CAMPRO1
    SW -->|PoE VLAN 10| CAMPRO2
    SW -->|PoE VLAN 10| CAMBULLET
    SW -->|PoE VLAN 40/30| AP1
    SW -->|PoE VLAN 40/30| AP2
    SW -->|PoE VLAN 40/30| AP3
    SW -->|PoE VLAN 20| HUB1
    SW -->|PoE VLAN 20| HUB2
    HUB1 --- READER1
    HUB1 --- READER2
    HUB2 --- READER3
    HUB2 --- MAGLOCK
    UNVR <-->|Records footage| CAM360A
    UNVR <-->|Records footage| CAM360B
    UNVR <-->|Records footage| CAMPRO1
    UNVR <-->|Records footage| CAMPRO2
    UNVR <-->|Records footage| CAMBULLET

    style WOW fill:#1e40af,stroke:#3b82f6,color:#fff
    style UCG fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style SW fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style UNVR fill:#7c3aed,stroke:#a78bfa,color:#fff
    style CAM360A fill:#065f46,stroke:#10b981,color:#fff
    style CAM360B fill:#065f46,stroke:#10b981,color:#fff
    style CAMPRO1 fill:#065f46,stroke:#10b981,color:#fff
    style CAMPRO2 fill:#065f46,stroke:#10b981,color:#fff
    style CAMBULLET fill:#065f46,stroke:#10b981,color:#fff
    style AP1 fill:#0e7490,stroke:#06b6d4,color:#fff
    style AP2 fill:#0e7490,stroke:#06b6d4,color:#fff
    style AP3 fill:#0e7490,stroke:#06b6d4,color:#fff
    style HUB1 fill:#92400e,stroke:#f59e0b,color:#fff
    style HUB2 fill:#92400e,stroke:#f59e0b,color:#fff
    style READER1 fill:#78350f,stroke:#fbbf24,color:#fff
    style READER2 fill:#78350f,stroke:#fbbf24,color:#fff
    style READER3 fill:#78350f,stroke:#fbbf24,color:#fff
    style MAGLOCK fill:#7f1d1d,stroke:#ef4444,color:#fff
```

> **CGMax note:** If CGMax is chosen over UCG-Ultra + UNVR, the two top boxes collapse into one device. All downstream connections remain identical.

---

## 3. Gate Network — Physical Topology

Both gates use an identical architecture. This diagram applies to both the front and rear gate.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f2744', 'lineColor': '#10b981'}}}%%
graph TD
    CELL["📡 CELLULAR NETWORK\nT-Mobile · AT&T · Verizon"]
    LTE["📶 LTE Pro\nCellular Gateway + WiFi\nGate cabinet mounted\n192.168.20.31 / .32"]
    HUB["🔑 Access Hub · UA-Hub\nLocal credential cache\nWorks OFFLINE if LTE drops\n192.168.20.21 / .22"]
    CAM["📷 AI-Pro Camera\nLicense Plate Recognition\nIR night vision\n8-10ft mount height\n192.168.10.21 / .22"]
    READER["👆 Reader Pro\nFob + NFC entry\nGate entry post"]
    INTERCOM["🔔 AI-Theta-Pro\nVideo Intercom\nFRONT GATE ONLY"]
    GATE["⚙️ Gate Operator\nExisting hardware\nDry contact from Hub\nLoop detector exit"]

    CELL -->|"Cellular WAN"| LTE
    LTE -->|"PoE / LAN"| HUB
    LTE -->|"PoE / LAN"| CAM
    HUB -->|"Wired relay"| GATE
    HUB --- READER
    HUB --- INTERCOM

    subgraph OFFLINE["🔒 OFFLINE CAPABILITY"]
        OA["Fob auth from local cache\nNo internet required\nResidents never locked out"]
    end
    HUB -.->|"Fails safely to"| OFFLINE

    style CELL fill:#1e40af,stroke:#3b82f6,color:#fff
    style LTE fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style HUB fill:#92400e,stroke:#f59e0b,color:#fff
    style CAM fill:#065f46,stroke:#10b981,color:#fff
    style READER fill:#78350f,stroke:#fbbf24,color:#fff
    style INTERCOM fill:#4a1d96,stroke:#8b5cf6,color:#fff
    style GATE fill:#374151,stroke:#9ca3af,color:#fff
    style OFFLINE fill:#1a2a1a,stroke:#10b981,color:#86efac
```

**Front gate only:** AI-Theta-Pro video intercom installed. Rear gate has Reader Pro and LPR camera only — no intercom, residents and service vehicles with fobs only.

---

## 4. Full System Logical Topology — All Three Sites

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#111827', 'lineColor': '#6b7280'}}}%%
graph TB
    subgraph INTERNET["☁️  INTERNET & UBIQUITI CLOUD"]
        WOW2["WOW Fiber"]
        LTE_CELL["Cellular Networks"]
        CLOUD2["Ubiquiti Cloud\nunifi.ui.com\nHTTPS only · No footage stored"]
    end

    subgraph CLUBHOUSE2["🏛️  CLUBHOUSE"]
        UCG2["UCG-Ultra / CGMax\nGateway + Controller"]
        SW2["PoE Switch"]
        UNVR2["UNVR\nOn-premises recording"]
        CAMS2["5 Cameras\nAI-360 × 2\nAI-Pro × 2\nAI-Bullet × 1"]
        APS2["WiFi APs × 3"]
        HUBS2["Access Hubs × 2\nPool + Door"]
    end

    subgraph FGATE2["🚗  FRONT GATE"]
        LTEF["LTE Pro"]
        HUBF["Access Hub\nw/ Credential Cache"]
        INTERCOMF["AI-Theta-Pro\nIntercom"]
        CAMF["AI-Pro LPR\nCamera"]
        READF["Reader Pro"]
    end

    subgraph RGATE2["🚗  REAR GATE"]
        LTER["LTE Pro"]
        HUBR["Access Hub\nw/ Credential Cache"]
        CAMR["AI-Pro LPR\nCamera"]
        READR["Reader Pro"]
    end

    WOW2 -->|WAN| UCG2
    UCG2 --> SW2
    SW2 --> UNVR2
    SW2 --> CAMS2
    SW2 --> APS2
    SW2 --> HUBS2
    UNVR2 <--> CAMS2

    LTE_CELL --> LTEF
    LTE_CELL --> LTER
    LTEF --> HUBF
    LTEF --> CAMF
    HUBF --- INTERCOMF
    HUBF --- READF
    LTER --> HUBR
    LTER --> CAMR
    HUBR ---READR

    CLOUD2 <-->|"HTTPS management"| UCG2
    CLOUD2 <-->|"HTTPS management"| LTEF
    CLOUD2 <-->|"HTTPS management"| LTER

    style INTERNET fill:#1e1b4b,stroke:#818cf8,color:#e0e7ff
    style CLUBHOUSE2 fill:#0c2340,stroke:#3b82f6,color:#bfdbfe
    style FGATE2 fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style RGATE2 fill:#0c1e2a,stroke:#06b6d4,color:#a5f3fc
    style UCG2 fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style SW2 fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style UNVR2 fill:#4c1d95,stroke:#a78bfa,color:#fff
    style CAMS2 fill:#065f46,stroke:#10b981,color:#fff
    style APS2 fill:#0e7490,stroke:#06b6d4,color:#fff
    style HUBS2 fill:#92400e,stroke:#f59e0b,color:#fff
    style LTEF fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style LTER fill:#1e3a5f,stroke:#60a5fa,color:#fff
    style HUBF fill:#92400e,stroke:#f59e0b,color:#fff
    style HUBR fill:#92400e,stroke:#f59e0b,color:#fff
    style INTERCOMF fill:#4a1d96,stroke:#8b5cf6,color:#fff
    style CAMF fill:#065f46,stroke:#10b981,color:#fff
    style CAMR fill:#065f46,stroke:#10b981,color:#fff
    style READF fill:#78350f,stroke:#fbbf24,color:#fff
    styleREADR fill:#78350f,stroke:#fbbf24,color:#fff
    style CLOUD2 fill:#2d1a4a,stroke:#8b5cf6,color:#e9d5ff
    style WOW2 fill:#1e40af,stroke:#3b82f6,color:#fff
    style LTE_CELL fill:#1e40af,stroke:#3b82f6,color:#fff
```

---

## 5. VLAN Segmentation Design

Each device category is isolated on its own network segment. A compromised camera cannot reach the access control system. Guest WiFi cannot reach anything security-related.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#111827', 'lineColor': '#4b5563'}}}%%
graph LR
    GW["🖥️ Gateway\nUCG-Ultra / CGMax"]

    subgraph V1["VLAN 1 — Management  192.168.1.0/24"]
        M1["Controller · Switch · UNVR · APs"]
    end

    subgraph V10["VLAN 10 — Cameras  192.168.10.0/24"]
        M10["All cameras — clubhouse + gates\n🚫 No internet access\n✅ UNVR only"]
    end

    subgraph V20["VLAN 20 — Access Control  192.168.20.0/24"]
        M20["All Access Hubs · LTE Pros\n🚫 No local network access\n✅ Ubiquiti cloud HTTPS only"]
    end

    subgraph V30["VLAN 30 — Guest WiFi  192.168.30.0/24"]
        M30["Resident devices at pool\n✅ Internet access\n🚫 Blocked from all security VLANs"]
    end

    subgraph V40["VLAN 40 — Staff WiFi  192.168.40.0/24"]
        M40["GHS + board devices\n✅ Internet access\n✅ Admin dashboard only"]
    end

    GW <-->|"Trunk"| V1
    GW <-->|"Routed\nFirewall enforced"| V10
    GW <-->|"Routed\nFirewall enforced"| V20
    GW <-->|"Routed\nFirewall enforced"| V30
    GW <-->|"Routed\nFirewall enforced"| V40

    V10 x--x|"BLOCKED"| V20
    V10 x--x|"BLOCKED"| V30
    V20 x--x|"BLOCKED"| V30
    V30 x--x|"BLOCKED"| V40

    style GW fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style V1 fill:#1a2a1a,stroke:#10b981,color:#a7f3d0
    style V10 fill:#1a1a2e,stroke:#6366f1,color:#c7d2fe
    style V20 fill:#2a1a0a,stroke:#f59e0b,color:#fde68a
    style V30 fill:#0a1a2a,stroke:#06b6d4,color:#a5f3fc
    style V40 fill:#1a0a2a,stroke:#8b5cf6,color:#e9d5ff
    style M1 fill:#0d1f0d,stroke:#10b981,color:#86efac
    style M10 fill:#0d0d1f,stroke:#6366f1,color:#a5b4fc
    style M20 fill:#1f120d,stroke:#f59e0b,color:#fcd34d
    style M30 fill:#0d121f,stroke:#06b6d4,color:#67e8f9
    style M40 fill:#120d1f,stroke:#8b5cf6,color:#c4b5fd
```

---

## 6. Camera Coverage Map — Clubhouse and Pool

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#475569'}}}%%
graph TD
    subgraph SITE["🏛️ CLUBHOUSE SITE — Camera Coverage Zones"]
        subgraph PARKING["🚗 PARKING LOT ZONE"]
            P1["📷 AI-Pro · SW Corner\nInbound vehicle plates\nDay + IR night vision\n192.168.10.13"]
        end
        subgraph DOOR["🚪 CLUBHOUSE ENTRY ZONE"]
            P2["📷 AI-Pro · NE Corner Exterior\nFace + person detection\nAccess Hub Reader co-located\n192.168.10.14"]
        end
        subgraph POOL["🏊 POOL DECK ZONE — Full 360° Coverage"]
            P3["📷 AI-360 · Deck North\nFull 360° fisheye\nNo blind spots\n192.168.10.11"]
            P4["📷 AI-360 · Deck South\nFull 360° fisheye\nNo blind spots\n192.168.10.12"]
        end
        subgraph PERIM["🔒 PERIMETER ZONE"]
            P5["📷 AI-Bullet · West Fence\nLong sightline coverage\nIR range 100+ ft\n192.168.10.15"]
        end
    end

    UNVR3["💾 UNVR — Records all 5 feeds\n~30 day retention · On-premises only"]

    P1 -->|"VLAN 10"| UNVR3
    P2 -->|"VLAN 10"| UNVR3
    P3 -->|"VLAN 10"| UNVR3
    P4 -->|"VLAN 10"| UNVR3
    P5 -->|"VLAN 10"| UNVR3

    style SITE fill:#0f172a,stroke:#475569,color:#e2e8f0
    style PARKING fill:#1a2a1a,stroke:#10b981,color:#a7f3d0
    style DOOR fill:#1a1a2e,stroke:#6366f1,color:#c7d2fe
    style POOL fill:#0e2a3a,stroke:#06b6d4,color:#a5f3fc
    style PERIM fill:#2a1a0a,stroke:#f59e0b,color:#fde68a
    style P1 fill:#065f46,stroke:#10b981,color:#fff
    style P2 fill:#3730a3,stroke:#6366f1,color:#fff
    style P3 fill:#0e7490,stroke:#06b6d4,color:#fff
    style P4 fill:#0e7490,stroke:#06b6d4,color:#fff
    style P5 fill:#92400e,stroke:#f59e0b,color:#fff
    style UNVR3 fill:#4c1d95,stroke:#a78bfa,color:#fff
```

---

## 7. Camera Coverage Map — Gates

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#10b981'}}}%%
graph LR
    subgraph FG["🚗 FRONT GATE — W. Georgia Rd"]
        FR["🚘 Inbound\nvehicles"]
        FLPR["📷 AI-Pro LPR\nMounted 8-10ft height\n15-25ft back from gate\n15-20° downward angle\nIR night capture\n192.168.10.21"]
        FPOST["📍 Entry Post\n👆 Reader Pro\n🔔 AI-Theta-Pro Intercom"]
        FOPER["⚙️ Gate Operator\nExisting hardware\nUA-Hub dry contact"]
        FR --> FLPR --> FPOST --> FOPER
    end

    subgraph RG["🚗 REAR GATE — Secondary Entry"]
        RR["🚘 Inbound\nvehicles"]
        RLPR["📷 AI-Pro LPR\nMounted 8-10ft height\n15-25ft back from gate\n192.168.10.22"]
        RPOST["📍 Entry Post\n👆 Reader Pro\n⛔ No intercom\nResidents + service only"]
        ROPER["⚙️ Gate Operator\nExisting hardware\nUA-Hub dry contact"]
        RR --> RLPR --> RPOST --> ROPER
    end

    style FG fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style RG fill:#0c1e2a,stroke:#06b6d4,color:#a5f3fc
    style FLPR fill:#065f46,stroke:#10b981,color:#fff
    style RLPR fill:#065f46,stroke:#10b981,color:#fff
    style FPOST fill:#78350f,stroke:#fbbf24,color:#fff
    style RPOST fill:#78350f,stroke:#fbbf24,color:#fff
    style FOPER fill:#374151,stroke:#9ca3af,color:#fff
    style ROPER fill:#374151,stroke:#9ca3af,color:#fff
```

---

## 8. IP Addressing Plan

| Device | VLAN | Assigned IP | Type |
|---|---|---|---|
| UCG-Ultra / CGMax | 1 | 192.168.1.1 | Static |
| UNVR | 1 | 192.168.1.10 | Static |
| PoE Switch | 1 | 192.168.1.20 | Static |
| U6 Mesh AP (pool) | 1 | 192.168.1.31 | DHCP Reserved |
| U6 Mesh AP (patio) | 1 | 192.168.1.32 | DHCP Reserved |
| U6 Extender | 1 | 192.168.1.33 | DHCP Reserved |
| Camera — AI-360 Pool North | 10 | 192.168.10.11 | DHCP Reserved |
| Camera — AI-360 Pool South | 10 | 192.168.10.12 | DHCP Reserved |
| Camera — AI-Pro Parking | 10 | 192.168.10.13 | DHCP Reserved |
| Camera — AI-Pro Door | 10 | 192.168.10.14 | DHCP Reserved |
| Camera — AI-Bullet Perimeter | 10 | 192.168.10.15 | DHCP Reserved |
| Camera — AI-Pro Front Gate LPR | 10 | 192.168.10.21 | DHCP Reserved |
| Camera — AI-Pro Rear Gate LPR | 10 | 192.168.10.22 | DHCP Reserved |
| Access Hub — Pool | 20 | 192.168.20.11 | DHCP Reserved |
| Access Hub — Clubhouse Door | 20 | 192.168.20.12 | DHCP Reserved |
| Access Hub — Front Gate | 20 | 192.168.20.21 | DHCP Reserved |
| Access Hub — Rear Gate | 20 | 192.168.20.22 | DHCP Reserved |
| LTE Pro — Front Gate | 20 | 192.168.20.31 | DHCP Reserved |
| LTE Pro — Rear Gate | 20 | 192.168.20.32 | DHCP Reserved |

> Reserve all IPs in the DHCP server during Phase 1 setup — before any device is powered on.

---

## 9. Architecture Decision: UCG-Ultra + UNVR vs. Cloud Gateway Max

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#475569'}}}%%
graph LR
    subgraph OPT1["Option A — UCG-Ultra + UNVR"]
        A1["🖥️ UCG-Ultra\n$129\nNetworking only"]
        A2["💾 UNVR\n$299\nCamera recording\n2× HDD bays"]
        A1 --- A2
        A3["Total: $428\n✅ Modular — fails independently\n✅ HDD expandable\n✅ Howard runs this at home\n⚠️ Two devices to rack"]
    end

    subgraph OPT2["Option B — Cloud Gateway Max"]
        B1["🖥️ CGMax\n$199\nNetworking + NVMe recording\nSingle device"]
        B2["Total: $199\n✅ $229 cheaper\n✅ One device — simpler\n⚠️ Single point of failure\n⚠️ Fixed NVMe storage"]
    end

    DECIDE{"⚡ Howard\nto decide\nbefore order"}

    OPT1 --> DECIDE
    OPT2 --> DECIDE

    style OPT1 fill:#0c2a1a,stroke:#10b981,color:#a7f3d0
    style OPT2 fill:#0c1e3a,stroke:#3b82f6,color:#bfdbfe
    style A1 fill:#065f46,stroke:#10b981,color:#fff
    style A2 fill:#4c1d95,stroke:#a78bfa,color:#fff
    style A3 fill:#0d1f0d,stroke:#10b981,color:#86efac
    style B1 fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style B2 fill:#0d1220,stroke:#3b82f6,color:#93c5fd
    style DECIDE fill:#7c2d12,stroke:#f97316,color:#fff
```

---

## 10. UniFi Application Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'lineColor': '#6b7280'}}}%%
graph TD
    LOGIN["🔐 unifi.ui.com\nSingle login for all three apps"]

    subgraph NET["🌐 UniFi Network"]
        N1["Manages switches, WiFi,\nVLANs, firewall, LTE Pros"]
        N2["Users: Howard setup\nGHS monitoring"]
    end

    subgraph PROT["📷 UniFi Protect"]
        P1["Manages all cameras\nlive view, recording,\nmotion detection, AI alerts"]
        P2["Users: Howard setup\nGHS daily ops\nBoard viewer"]
    end

    subgraph ACC["🔑 UniFi Access"]
        A1["Manages access control\nfobs, doors, gates,\nschedules, access logs"]
        A2["Users: Howard setup\nGHS daily ops"]
    end

    LOGIN --> NET
    LOGIN --> PROT
    LOGIN --> ACC

    style LOGIN fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style NET fill:#065f46,stroke:#10b981,color:#a7f3d0
    style PROT fill:#4c1d95,stroke:#a78bfa,color:#e9d5ff
    style ACC fill:#92400e,stroke:#f59e0b,color:#fde68a
    style N1 fill:#0d1f14,stroke:#10b981,color:#86efac
    style N2 fill:#0d1f14,stroke:#10b981,color:#86efac
    style P1 fill:#1a0a2a,stroke:#8b5cf6,color:#c4b5fd
    style P2 fill:#1a0a2a,stroke:#8b5cf6,color:#c4b5fd
    style A1 fill:#1f120d,stroke:#f59e0b,color:#fcd34d
    style A2 fill:#1f120d,stroke:#f59e0b,color:#fcd34d
```

---

*Project ARGUS | River Shoals HOA | Confidential Board Document*
*Last updated: June 2026*
