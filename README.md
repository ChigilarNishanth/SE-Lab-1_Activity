# SE Lab 1: Requirements Engineering & UML Use-Case Modelling
**Course:** Software Engineering Lab  
**Institution:** PES University - Dept. of CSE  
**Problem Statement #56:** Peer Skill Exchange & Mentorship Network  

---

## 📌 Deliverables Overview
* 📄 **Problem Statement:** [`docs/Problem_Statement.pdf`](docs/Problem_Statement.pdf)
* 📋 **Requirements Specification:** [`docs/Requirements_Specification.md`](docs/Requirements_Specification.md)
* 📐 **Use Case Specification:** [`docs/Use_Case_Specification.md`](docs/Use_Case_Specification.md)
* 📊 **UML Diagram Source:** [`diagrams/use_case_diagram.puml`](diagrams/use_case_diagram.puml)

---

## 📋 1. Requirements Table

### Functional Requirements (FR-001 to FR-005)

| ID | Type / Category | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Credit Ledger | The system shall maintain an automated time-credit ledger for each member, crediting 1 hour to the mentor and debiting 1 hour from the learner upon verified completion of a session. | High | **Pass:** 1 credit transfers from learner to mentor balance upon mutual sign-off.<br>**Fail:** A member with 0 credits is permitted to confirm a session booking. | Establishes the core peer time-banking exchange model without fiat currency. |
| **FR-002** | Discovery & Search | The system shall allow Skill Mentors to publish tagged skill offerings and allow Learner Members to filter listings by skill name, mentor rating, and availability. | High | **Pass:** Search queries return matching mentor profiles and slots within 2 seconds.<br>**Fail:** Inactive or fully booked slots appear in active search results. | Enables members to discover appropriate skills and qualified mentors efficiently. |
| **FR-003** | Scheduling & Booking | The system shall permit Learner Members with ≥ 1 credit to book an open mentor time slot and place the credit into an escrow lock. | High | **Pass:** Selected slot locks in real-time to prevent duplicate bookings across concurrent users.<br>**Fail:** Two learners book the same mentor slot concurrently. | Prevents scheduling overlaps and manages session availability cleanly. |
| **FR-004** | Verification & Validation | The system shall prompt both the Learner Member and Skill Mentor to submit a session completion validation and a 1–5 star rating with feedback within 48 hours. | Medium | **Pass:** Time credit is released from escrow to mentor balance upon dual confirmation.<br>**Fail:** Ledger updates prior to validation confirmation. | Guarantees peer accountability and prevents fraudulent credit claims. |
| **FR-005** | Cancellation & Disputes | The system shall permit session cancellations with 100% credit refund if cancelled >24 hours prior, and allow dispute logging for session no-shows. | Medium | **Pass:** Held credit is restored on valid cancellation; disputes freeze credits for admin resolution.<br>**Fail:** Learner loses credit when a mentor fails to attend. | Protects member time investments against no-shows and technical faults. |

### Non-Functional Requirements (NFR-001 & NFR-002)

| ID | Type / Category | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR-001** | Performance & Interoperability | The session scheduling engine must sync with external calendar platforms (Google Calendar, Outlook) via standard iCal (`.ics`) export feeds and webhook alerts. | High | **Pass:** External calendar event updates trigger within 5 seconds under peak simulated load; `.ics` files adhere strictly to RFC 5545.<br>**Fail:** Sync response latency exceeds 15 seconds or produces malformed calendar files. | Minimizes missed appointments by keeping members' external schedules aligned. |
| **NFR-002** | Security & Data Integrity | All time-credit ledger operations must ensure ACID transactional consistency, with user credentials and data encrypted using TLS 1.3 in transit and AES-256 at rest. | High | **Pass:** Zero ledger inconsistencies during concurrent transaction tests; zero plaintext credentials stored.<br>**Fail:** Ledger race conditions or negative credit balances occur under concurrent operations. | Guarantees reliability and trust in the digital time-credit currency. |

---

## 📊 2. UML Use-Case Diagram

```mermaid
flowchart LR
    %% Primary Actors
    Learner["👤 Learner Member"]
    Mentor["👤 Skill Mentor"]

    %% External Systems
    Ledger[("🗄️ Ledger System")]
    Calendar["📅 Calendar Service"]

    %% System Boundary
    subgraph Platform ["Peer Skill Exchange Platform"]
        direction TB

        %% 1. Learner Direct Actions (Top)
        UC2(["UC-02: Search & Filter Mentors"])
        UC3(["UC-03: Book Mentorship Session"])
        UC4(["UC-04: Verify Credit Balance"])
        UC8(["UC-08: Sync with External Calendar"])

        %% 2. Shared Completion Actions (Middle)
        UC5(["UC-05: Validate Session Completion"])
        UC6(["UC-06: Transfer Time Credit"])
        UC7(["UC-07: Submit Feedback & Rating"])
        UC9(["UC-09: Raise Session Dispute"])

        %% 3. Mentor Direct Actions (Bottom)
        UC1(["UC-01: Manage Skill Listings"])
    end

    %% Learner Connections (Top-to-Middle, No Crossing)
    Learner --> UC2
    Learner --> UC3
    Learner --> UC5

    %% Mentor Connections (Bottom-to-Middle, No Crossing)
    Mentor --> UC5
    Mentor --> UC1

    %% <<include>> Relationships (Dashed with Arrowheads)
    UC3 -.->|«include»| UC4
    UC5 -.->|«include»| UC6

    %% <<extend>> Relationships (Dashed with Arrowheads)
    UC3 -.->|«extend»| UC8
    UC5 -.->|«extend»| UC7
    UC5 -.->|«extend»| UC9

    %% External System Connections
    UC4 --> Ledger
    UC6 --> Ledger
    UC8 --> Calendar
```
---

## 📐 3. Core Use-Case Flow Specification (UC-03)

* **Use Case ID:** UC-03
* **Use Case Name:** Book Mentorship Session
* **Primary Actor:** Learner Member
* **Secondary Actors:** Skill Mentor, Time-Credit Ledger System, External Calendar Service

### Preconditions
1. Learner Member is authenticated with an active account balance ≥ 1 credit.
2. Skill Mentor has published active listings with open calendar slots.

### Postconditions
1. Time slot is reserved and locked in system calendars.
2. 1 time credit is placed into escrow lock.
3. Notifications and calendar invites are dispatched.

### Main Success Scenario (MSS)
1. Learner filters and selects a mentor profile and desired time slot.
2. Learner submits learning topics and initiates booking request.
3. System triggers `<<include>> UC-04: Verify Credit Balance`.
4. System verifies balance ≥ 1, locks the slot, and moves 1 credit to escrow.
5. System notifies Skill Mentor of booking request.
6. Skill Mentor accepts the booking request.
7. System triggers `<<extend>> UC-08: Sync with External Calendar` to send `.ics` calendar invites.
8. System generates virtual meeting room link and displays confirmation.

### Alternate Flows
* **AF-1: Insufficient Time Credits (Step 4):** Ledger detects 0 credits $\rightarrow$ Booking is blocked $\rightarrow$ System displays error message and prompts user to earn credits by mentoring.
* **AF-2: Mentor Rejection / Request Expiry (Step 6):** Mentor declines or request expires after 24h $\rightarrow$ System unlocks slot $\rightarrow$ Held escrow credit is returned to learner.