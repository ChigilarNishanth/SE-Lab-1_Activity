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