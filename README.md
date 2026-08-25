# SE-Lab-1_Activity
PES University - Dept. of CSE - Lab 1: Requirements Engineering &amp; UML Use-Case Modelling (Problem #56)

# SE Lab 1: Requirements Engineering & UML Use-Case Modelling
**Course:** Software Engineering Lab  
**Institution:** PES University - Dept. of CSE  
**Problem Statement #56:** Peer Skill Exchange & Mentorship Network  

---

## 📌 Deliverables Directory
* 📋 **Requirements Specification:** [`docs/Requirements_Specification.md`](docs/Requirements_Specification.md) (5 FRs, 2 NFRs)
* 📐 **Use Case Specification:** [`docs/Use_Case_Specification.md`](docs/Use_Case_Specification.md) (Detailed MSS & Alternate Flows for UC-03)
* 📊 **UML Diagram Source:** [`diagrams/use_case_diagram.puml`](diagrams/use_case_diagram.puml)

---

## 📊 UML Use-Case Diagram

```mermaid
flowchart LR
    %% Primary Human Actors (Left)
    Learner["👤 Learner Member"]
    Mentor["👤 Skill Mentor"]

    %% Platform Boundary
    subgraph Platform ["Peer Skill Exchange Platform"]
        direction TB
        
        %% Core Use Cases
        UC1(["UC-01: Manage Skill Listings"])
        UC2(["UC-02: Search & Filter Mentors"])
        UC3(["UC-03: Book Mentorship Session"])
        UC5(["UC-05: Validate Session Completion"])
        
        %% Supporting / Included / Extended Use Cases
        UC4(["UC-04: Verify Credit Balance"])
        UC6(["UC-06: Transfer Time Credit"])
        UC7(["UC-07: Submit Feedback & Rating"])
        UC8(["UC-08: Sync with External Calendar"])
        UC9(["UC-09: Raise Session Dispute"])
    end

    %% External Systems (Right)
    Ledger[("🗄️ Ledger System")]
    Calendar["📅 Calendar Service"]

    %% Actor Connections (Straight into Core Use Cases)
    Mentor --- UC1
    Learner --- UC2
    Learner --- UC3
    Learner --- UC5
    Mentor --- UC5

    %% Include Relationships
    UC3 -. "&laquo;include&raquo;" .-> UC4
    UC5 -. "&laquo;include&raquo;" .-> UC6

    %% Extend Relationships
    UC3 -. "&laquo;extend&raquo;" .-> UC8
    UC5 -. "&laquo;extend&raquo;" .-> UC7
    UC5 -. "&laquo;extend&raquo;" .-> UC9

    %% External System Connections
    UC4 --- Ledger
    UC6 --- Ledger
    UC8 --- Calendar
```