# Project ARGUS — Tracker
## River Shoals HOA | Security Infrastructure Modernization

*Last updated: June 2026*

---

## Budget

### Phase 1 — Clubhouse Foundation

Scope: WOW fiber internet, network backbone, clubhouse and pool WiFi, and 5 replacement cameras covering clubhouse interior, exterior, pool deck, and parking lot. Establishes the core infrastructure all later phases depend on.

> Architecture note: The UCG-Ultra handles networking only and cannot run UniFi Protect (cameras). The UNVR is required as a separate camera recorder. Alternative: replace both with a Cloud Gateway Max ($199) which includes built-in NVMe storage for Protect, saving ~$229. Howard to decide before ordering.

| Item | Model | Qty | Unit Cost | Extended | Notes |
|---|---|---|---|---|---|
| WOW Fiber provisioning | — | 1 | $0 | $0 | No cost per community agreement with Rico Pruitt |
| Cloud Gateway Ultra | UCG-Ultra | 1 | $129 | $129 | Network controller (networking only — see note above) |
| Network Video Recorder | UNVR | 1 | $299 | $299 | Camera storage, runs UniFi Protect |
| Storage drives 4TB | WD Purple 4TB | 2 | $99 | $198 | ~30 days retention at 5 cameras 1080p |
| PoE Switch | USW-Lite-8-POE | 1 | $109 | $109 | Powers cameras and APs |
| Camera — AI 360 (pool deck) | UVC-AI-360 | 2 | $349 | $698 | 360° fisheye, no blind spots at pool |
| Camera — AI Pro (entry/parking) | UVC-AI-Pro | 2 | $349 | $698 | Directional, captures faces/plates at entry |
| Camera — AI Bullet (perimeter) | UVC-AI-Bullet | 1 | $199 | $199 | Long sightline along perimeter fence |
| WiFi AP — U6 Mesh | U6-Mesh | 2 | $179 | $358 | Outdoor pool/patio coverage |
| WiFi AP — U6 Extender | U6-Extender | 1 | $129 | $129 | Extends coverage to far side of pool area |
| Cable, conduit, mounts, enclosures | — | 1 | $250 | $250 | Consumables estimate |
| WOW fiber provision contingency | — | 1 | $200 | $200 | If commercial drop requires a run; $0 if WOW activates free |

**Phase 1 Subtotal: ~$3,267 (WOW free) / ~$3,467 (WOW contingency)**
**Board should approve $3,565 to maintain contingency room.**

---

### Phase 2 — Pool and Clubhouse Door Access

Scope: Replace existing pool RFID system with UniFi Access. Add access control to the clubhouse door. Issue resident key fobs. One outside contractor needed for clubhouse door maglock hardware only.

| Item | Model | Qty | Unit Cost | Extended | Notes |
|---|---|---|---|---|---|
| Access Hub (pool gate) | UA-Hub | 1 | $149 | $149 | Controls pool gate lock |
| Access Reader Pro (pool entry) | UA-Reader-Pro | 1 | $179 | $179 | Resident fob/NFC tap to enter |
| Access Reader Lite (pool exit) | UA-Reader-Lite | 1 | $79 | $79 | Exit reader, pool side |
| Access Hub (clubhouse door) | UA-Hub | 1 | $149 | $149 | Controls clubhouse door lock |
| Access Reader Pro (clubhouse) | UA-Reader-Pro | 1 | $179 | $179 | Resident fob/NFC tap to enter |
| Key fob stock (~100 fobs) | UA-Fob | 10 pk | $89 | $890 | First issuance batch (~280 lots total; second batch needed later) |
| Wiring, power supply, misc hardware | — | 1 | $247 | $247 | Conduit, low-voltage cabling, junction boxes |
| Maglock/strike installation (outside contractor) | — | 1 | $500 | $500 | Clubhouse door only — fire egress wiring required |

**Phase 2 Subtotal: ~$2,372**

> This is the only outside labor in the full project. The maglock/strike on the clubhouse door requires proper fire egress wiring that warrants a licensed installer.

---

### Phase 3 — Front and Rear Gate Access

Scope: Bring both community gates onto UniFi Access using LTE Pro cellular connectivity at each gate. Add video intercom for visitor entry at the front gate. Add LPR cameras at both gates. Both gates already have operators, loop detectors, and AC power — work involves wiring Access Hubs to existing gate operator dry contacts.

#### Connectivity: LTE Pro at Both Gates

Both gates use a Ubiquiti LTE Pro unit for network connectivity. At ~1 mile from the clubhouse, wired Ethernet is not viable and wireless bridge range is insufficient. LTE provides independent, reliable connectivity at each gate with no dependency on the clubhouse network.

**Offline / failover behavior:** The Access Hub stores resident credentials locally on-device. If the LTE connection drops for any reason, resident fob and NFC authentication continues to work normally using the cached credential list. Residents are not locked out during an outage. What does not work during an outage: visitor intercom calls (require active connection to reach GHS or board) and new credential syncs. Loop detector exit (residents leaving) is hardwired and unaffected by network status.

**LTE SIM cards:** Each LTE Pro requires a data SIM from any carrier (T-Mobile, AT&T, or Verizon). These are not purchased from Ubiquiti — Howard to procure two SIMs on a low-data IoT/data plan. For access control and one camera per gate, 5-10GB/month per SIM is more than sufficient. Estimated ongoing cost: ~$25-35/month per SIM, or ~$50-70/month total. This is an operating expense, not a capital expense, and should be reflected in the HOA operating budget going forward.

| Item | Model | Qty | Unit Cost | Extended | Notes |
|---|---|---|---|---|---|
| Access Hub (front gate) | UA-Hub | 1 | $149 | $149 | Wires to existing front gate operator dry contacts |
| Access Hub (rear gate) | UA-Hub | 1 | $149 | $149 | Wires to existing rear gate operator dry contacts |
| Access Reader Pro (front gate) | UA-Reader-Pro | 1 | $179 | $179 | Resident fob/NFC entry — works offline |
| Access Reader Pro (rear gate) | UA-Reader-Pro | 1 | $179 | $179 | Resident fob/NFC entry — works offline |
| LTE Pro (front gate) | LTE-Pro | 1 | $179 | $179 | Cellular connectivity — gate has existing AC power |
| LTE Pro (rear gate) | LTE-Pro | 1 | $179 | $179 | Cellular connectivity — gate has existing AC power |
| Video Intercom (front gate) | AI-Theta-Pro | 1 | $299 | $299 | Visitor call-in to GHS or board remotely |
| Camera — AI Pro (front gate LPR) | UVC-AI-Pro | 1 | $349 | $349 | License plate capture, inbound |
| Camera — AI Pro (rear gate LPR) | UVC-AI-Pro | 1 | $349 | $349 | License plate capture |
| Cable, conduit, weatherproof hardware | — | 1 | $357 | $357 | Gate wiring, junction boxes, misc |

**Phase 3 Equipment Subtotal: ~$2,368**
**Phase 3 Ongoing: ~$50-70/month (2x LTE SIMs) — operating expense**

---

### Budget Summary

| Phase | Scope | Equipment Subtotal | Labor (Self) |
|---|---|---|---|
| Phase 1 | Clubhouse core: cameras, WiFi, NVR, WOW fiber | ~$3,565 | ~17 hrs |
| Phase 2 | Pool and clubhouse door access control + fobs | ~$2,372 | ~9 hrs + 1 outside contractor |
| Phase 3 | Front and rear gates: LTE, access control, intercom, LPR | ~$2,368 | ~13 hrs |
| **TOTAL** | | **~$8,305** | **~39 hrs self + 1 contractor** |

**SC sales tax (7%): ~$581**
**Total with tax: ~$8,886**

**Ongoing operating cost (LTE SIMs): ~$50-70/month — budget line item required**

---

## Schedule

| Phase | Task | Owner | Start Window | End Window | Status |
|---|---|---|---|---|---|
| Pre | Board approval of ARGUS budget | Howard | June 2026 | June 2026 | Pending |
| Pre | Architecture decision: UCG-Ultra + UNVR vs. Cloud Gateway Max | Howard | June 2026 | June 2026 | Pending |
| Pre | Equipment ordering | Howard | June 2026 | June 2026 | Pending |
| Pre | Procure 2x LTE SIM cards (T-Mobile / AT&T / Verizon IoT plan) | Howard | June 2026 | Pre-Phase 3 | Pending |
| Pre | WOW fiber scheduling with Rico Pruitt | Howard | June 2026 | July 2026 | Pending |
| Pre | CPS contract termination notice | Howard / GHS | June 2026 | TBD | Pending |
| — | **TRAVEL — NO WORK** | — | Jul 1, 2026 | Jul 31, 2026 | BLOCKED |
| 1 | UniFi controller + UNVR + switch installation | Howard | Aug 1 | Aug 5 | Pending |
| 1 | WOW fiber termination at clubhouse | Howard / Rico | Aug 1 | Aug 5 | Pending |
| 1 | Camera mounting and cabling (5 cameras) | Howard | Aug 5 | Aug 10 | Pending |
| 1 | WiFi AP installation and tuning (3 APs) | Howard | Aug 10 | Aug 12 | Pending |
| 1 | Phase 1 testing and acceptance | Howard | Aug 12 | Aug 14 | Pending |
| 2 | Clubhouse door maglock install (outside contractor) | Contractor | Aug 15 | Aug 16 | Pending |
| 2 | Pool access control (hub, readers, wiring) | Howard | Aug 15 | Aug 20 | Pending |
| 2 | Clubhouse door access control (hub, reader) | Howard | Aug 20 | Aug 22 | Pending |
| 2 | Fob issuance to residents (via GHS) | Howard / GHS | Aug 22 | Aug 31 | Pending |
| 2 | Phase 2 testing and acceptance | Howard | Aug 28 | Aug 31 | Pending |
| 3 | LTE Pro installation at front gate | Howard | Sep 1 | Sep 3 | Pending |
| 3 | LTE Pro installation at rear gate | Howard | Sep 1 | Sep 3 | Pending |
| 3 | Gate Access Hub installation and wiring (both gates) | Howard | Sep 3 | Sep 8 | Pending |
| 3 | Access Reader Pro installation (both gates) | Howard | Sep 3 | Sep 8 | Pending |
| 3 | LPR camera installation (both gates) | Howard | Sep 8 | Sep 12 | Pending |
| 3 | Front gate intercom installation | Howard | Sep 10 | Sep 12 | Pending |
| 3 | Credential sync and offline failover test (both gates) | Howard | Sep 12 | Sep 14 | Pending |
| 3 | Luke Burke review (resident/vehicle data) | Howard / Luke | Before go-live | — | Required — do not go live without this |
| 3 | Phase 3 testing and acceptance | Howard | Sep 15 | Sep 20 | Pending |
| All | GHS admin credentials set up in UniFi | Howard | Post Phase 1 | — | Pending |
| All | Board viewer access set up in UniFi | Howard | Post Phase 1 | — | Pending |
| All | CPS contract terminated | Howard / GHS | Post Phase 3 | — | Pending |

---

## Equipment List

| Phase | Item | Model | Qty | Unit Cost | Ordered? | Received? | Planned Location |
|---|---|---|---|---|---|---|---|
| 1 | Cloud Gateway Ultra | UCG-Ultra | 1 | $129 | No | No | Clubhouse AV/network closet |
| 1 | Network Video Recorder | UNVR | 1 | $299 | No | No | Clubhouse AV/network closet |
| 1 | Storage Drive 4TB | WD Purple 4TB | 2 | $99 | No | No | Inside UNVR |
| 1 | PoE Switch | USW-Lite-8-POE | 1 | $109 | No | No | Clubhouse AV/network closet |
| 1 | Camera — AI 360 | UVC-AI-360 | 2 | $349 | No | No | Pool deck (360° coverage) |
| 1 | Camera — AI Pro | UVC-AI-Pro | 2 | $349 | No | No | Parking lot entry, clubhouse exterior |
| 1 | Camera — AI Bullet | UVC-AI-Bullet | 1 | $199 | No | No | Pool perimeter / back fence |
| 1 | WiFi AP — U6 Mesh | U6-Mesh | 2 | $179 | No | No | Pool/patio outdoor coverage |
| 1 | WiFi AP — U6 Extender | U6-Extender | 1 | $129 | No | No | Far side pool area |
| 2 | Access Hub (pool) | UA-Hub | 1 | $149 | No | No | Pool gate enclosure |
| 2 | Access Reader Pro (pool in) | UA-Reader-Pro | 1 | $179 | No | No | Pool gate exterior |
| 2 | Access Reader Lite (pool out) | UA-Reader-Lite | 1 | $79 | No | No | Pool gate interior |
| 2 | Access Hub (clubhouse) | UA-Hub | 1 | $149 | No | No | Clubhouse door |
| 2 | Access Reader Pro (clubhouse) | UA-Reader-Pro | 1 | $179 | No | No | Clubhouse exterior door |
| 2 | Key Fobs (10-pack) | UA-Fob | 10 | $89 | No | No | GHS for resident issuance |
| 3 | Access Hub (front gate) | UA-Hub | 1 | $149 | No | No | Front gate operator cabinet |
| 3 | Access Hub (rear gate) | UA-Hub | 1 | $149 | No | No | Rear gate operator cabinet |
| 3 | Access Reader Pro (front gate) | UA-Reader-Pro | 1 | $179 | No | No | Front gate entry post |
| 3 | Access Reader Pro (rear gate) | UA-Reader-Pro | 1 | $179 | No | No | Rear gate entry post |
| 3 | LTE Pro (front gate) | LTE-Pro | 1 | $179 | No | No | Front gate operator cabinet |
| 3 | LTE Pro (rear gate) | LTE-Pro | 1 | $179 | No | No | Rear gate operator cabinet |
| 3 | Video Intercom (front gate) | AI-Theta-Pro | 1 | $299 | No | No | Front gate entry post |
| 3 | Camera — AI Pro (front gate LPR) | UVC-AI-Pro | 1 | $349 | No | No | Front gate, inbound lane |
| 3 | Camera — AI Pro (rear gate LPR) | UVC-AI-Pro | 1 | $349 | No | No | Rear gate, inbound lane |

---

## Open Items

| # | Item | Owner | Target | Status |
|---|---|---|---|---|
| 1 | Board vote to approve ARGUS budget (~$8,305 + tax) | Howard | June 2026 | Open |
| 2 | Architecture decision: UCG-Ultra + UNVR vs. Cloud Gateway Max | Howard | June 2026 | Open — CGMax saves ~$229 |
| 3 | WOW fiber activation scheduling with Rico Pruitt | Howard | June 2026 | Open |
| 4 | Confirm CPS annual contract cost (request from Sharon) | GHS | June 2026 | Open |
| 5 | CPS contract termination notice period confirmed | Howard / GHS | June 2026 | Open |
| 6 | Procure 2x LTE SIM cards for gate LTE Pro units | Howard | Pre-Phase 3 | Open — T-Mobile, AT&T, or Verizon IoT plan |
| 7 | Add LTE SIM monthly cost (~$50-70/mo) to HOA operating budget | Howard / Ruth | Pre-Phase 3 | Open |
| 8 | Outside contractor identified for clubhouse door maglock | Howard | Pre-Phase 2 | Open |
| 9 | Luke Burke review of resident/vehicle movement data handling | Howard / Luke Burke | Pre-Phase 3 | Required — do not go live without this |
| 10 | GHS admin credentials set up in UniFi | Howard | Post Phase 1 | Pending |
| 11 | Board viewer access set up in UniFi | Howard | Post Phase 1 | Pending |
| 12 | Fob issuance process defined with GHS | Howard / GHS | Pre-Phase 2 | Pending |
| 13 | Second fob batch order (~200 additional fobs for remaining lots) | Howard / GHS | Phase 2 | Pending |
| 14 | Credential sync and offline failover test completed at both gates | Howard | Phase 3 | Pending |
| 15 | CPS contract terminated and final billing reconciled | Howard / GHS | Post Phase 3 | Pending |
| 16 | As-built documentation filed in ARGUS folder | Howard | Post Phase 3 | Pending |

---

## Decisions Log

| Date | Decision / Action | Authority | Status |
|---|---|---|---|
| TBD | Board approval of full ARGUS budget | Board vote | Pending |
| TBD | Architecture: UCG-Ultra + UNVR vs. Cloud Gateway Max | Howard | Pending |
| TBD | Gate connectivity: LTE Pro at both gates (decided) | Howard | Decided June 2026 |
| TBD | WOW fiber service activation authorized | Board / Howard | Pending |
| TBD | GHS to provide current annual CPS cost | Howard / GHS | Pending |
| TBD | Luke Burke consultation on gate data handling | Howard / Luke | Pending |

*Add a row each time the board votes, Luke Burke is consulted, or a vendor commitment is made.*

---

*Project ARGUS | River Shoals HOA | Confidential Board Document*
*Last updated: June 2026*
