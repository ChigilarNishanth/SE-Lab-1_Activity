# Use-Case Flow Specification

**Use Case ID:** UC-03  
**Use Case Name:** Book Mentorship Session  
**Primary Actor:** Learner Member  
**Secondary / Supporting Actors:** Skill Mentor, Time-Credit Ledger System, External Calendar Service  

---

### 1. Description
Enables an authenticated Learner Member holding sufficient time credits to search for a mentor's listing, select an available time slot, and lock 1 time credit into escrow pending session completion.

### 2. Preconditions
1. The Learner Member is authenticated and logged into the platform.
2. The Learner Member holds an active balance of at least 1 verified time credit.
3. The Skill Mentor has at least one active listing with published available calendar slots.

### 3. Postconditions
1. The selected time slot is locked and marked as "Confirmed" on both members' schedules.
2. 1 time credit is placed into escrow from the learner's ledger.
3. Calendar invitations and automated notifications are dispatched to both actors.

---

### 4. Main Success Scenario (MSS)

| Step | Actor Action | System Response |
| :--- | :--- | :--- |
| **1** | Learner searches for a skill category and selects a Mentor profile. | Retrieves and displays mentor profile, ratings, and open slots. |
| **2** | Learner selects an open time slot and clicks **Request Booking**. | Prompts learner to input session goals/topics. |
| **3** | Learner submits session goals and confirms the booking. | System triggers `<<include>> UC-04: Verify Credit Balance`. |
| **4** | | Verifies learner balance ≥ 1, locks the time slot, and transitions 1 credit to escrow. |
| **5** | | Dispatches booking notification to the Skill Mentor. |
| **6** | Skill Mentor reviews the request and clicks **Accept Booking**. | Updates booking status to "Confirmed" in the database. |
| **7** | | Invokes `<<extend>> UC-08: Sync with External Calendar` to dispatch iCal invites. |
| **8** | | Displays confirmation screen with session meeting link to both parties. |

---

### 5. Alternate Flows

* **AF-1: Insufficient Time Credits (At Step 4)**
  * **4a.** The system ledger detects that the learner's balance is 0 credits.
  * **4b.** The system halts booking and displays: *"Booking Failed: You have 0 time credits. Mentor a peer to earn credits before scheduling a session."*
  * **4c.** The learner is redirected to skill listing management (`UC-01`). The use case terminates in failure.

* **AF-2: Mentor Rejection or Expiration (At Step 6)**
  * **6a.** The Skill Mentor declines the booking request or fails to respond within 24 hours.
  * **6b.** The system unlocks the reserved slot and refunds the escrowed credit back to the learner's active balance.
  * **6c.** The system dispatches an alert: *"Session request declined/expired. Your time credit has been restored."*
  * **6d.** The use case terminates.