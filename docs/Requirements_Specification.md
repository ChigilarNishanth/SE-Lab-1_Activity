# Software Requirements Specification (SRS)
## Peer Skill Exchange & Mentorship Network (Problem #56)

### 1. Functional Requirements (FR-001 to FR-005)

| ID | Type / Category | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Credit Ledger | The system shall maintain an automated time-credit ledger for each member, crediting 1 hour to the mentor and debiting 1 hour from the learner upon verified completion of a session. | High | **Pass:** 1 credit transfers from learner to mentor balance upon mutual sign-off.<br>**Fail:** A member with 0 credits is permitted to confirm a session booking. | Establishes the core peer time-banking exchange model. |
| **FR-002** | Discovery & Search | The system shall allow Skill Mentors to publish tagged skill offerings and allow Learner Members to filter listings by skill name, mentor rating, and availability. | High | **Pass:** Search queries return matching mentor profiles and slots within 2 seconds.<br>**Fail:** Inactive or fully booked slots appear in active search results. | Enables members to discover appropriate skills and mentors effectively. |
| **FR-003** | Scheduling & Booking | The system shall permit Learner Members with ≥ 1 credit to book an open mentor time slot and place the credit into an escrow lock. | High | **Pass:** Selected slot locks in real-time to prevent duplicate bookings across concurrent users.<br>**Fail:** Two learners book the same mentor slot concurrently. | Prevents scheduling overlaps and manages session availability cleanly. |
| **FR-004** | Verification & Validation | The system shall prompt both the Learner Member and Skill Mentor to submit a session completion validation and a 1–5 star rating with feedback within 48 hours. | Medium | **Pass:** Time credit is released from escrow to mentor balance upon dual confirmation.<br>**Fail:** Ledger updates prior to validation confirmation. | Guarantees peer accountability and prevents fraudulent credit claims. |
| **FR-005** | Cancellation & Disputes | The system shall permit session cancellations with 100% credit refund if cancelled >24 hours prior, and allow dispute logging for session no-shows. | Medium | **Pass:** Held credit is restored on valid cancellation; disputes freeze credits for admin resolution.<br>**Fail:** Learner loses credit when a mentor fails to attend. | Protects member time investments against no-shows and technical faults. |

---

### 2. Non-Functional Requirements (NFR-001 & NFR-002)

| ID | Type / Category | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR-001** | Performance & Interoperability | The session scheduling engine must sync with external calendar platforms (Google Calendar, Outlook) via standard iCal (`.ics`) export feeds and webhook alerts. | High | **Pass:** External calendar event updates trigger within 5 seconds under peak simulated load; `.ics` files adhere strictly to RFC 5545.<br>**Fail:** Sync response latency exceeds 15 seconds or produces malformed calendar files. | Minimizes missed appointments by keeping members' external schedules aligned. |
| **NFR-002** | Security & Data Integrity | All time-credit ledger operations must ensure ACID transactional consistency, with user credentials and data encrypted using TLS 1.3 in transit and AES-256 at rest. | High | **Pass:** Zero ledger inconsistencies during concurrent transaction tests; zero plaintext credentials stored.<br>**Fail:** Ledger race conditions or negative credit balances occur under concurrent operations. | Guarantees reliability and trust in the digital time-credit currency. |