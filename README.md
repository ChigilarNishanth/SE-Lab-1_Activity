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
graph LR
    Learner["fa:fa-user Learner Member"]
    Mentor["fa:fa-user Skill Mentor"]
    Ledger["fa:fa-database Ledger System"]
    Calendar["fa:fa-calendar Calendar Service"]

    subgraph "Peer Skill Exchange Platform"
        UC1([UC-01: Manage Skill Listings])
        UC2([UC-02: Search & Filter Mentors])
        UC3([UC-03: Book Mentorship Session])
        UC4([UC-04: Verify Credit Balance])
        UC5([UC-05: Validate Session Completion])
        UC6([UC-06: Transfer Time Credit])
        UC7([UC-07: Submit Feedback & Rating])
        UC8([UC-08: Sync with External Calendar])
        UC9([UC-09: Raise Session Dispute])
    end

    Learner --> UC2
    Learner --> UC3
    Learner --> UC5
    Mentor --> UC1
    Mentor --> UC5

    UC3 -.->|<<include>>| UC4
    UC5 -.->|<<include>>| UC6

    UC8 -.->|<<extend>>| UC3
    UC7 -.->|<<extend>>| UC5
    UC9 -.->|<<extend>>| UC5

    UC4 --> Ledger
    UC6 --> Ledger
    UC8 --> Calendar
```