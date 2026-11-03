# Recruitment & Placement Management System (RPMS)
## Sample Run Transcripts & Terminal Output Verification

This document contains actual sample execution transcripts demonstrating that all 17 completion criteria in the Kiran Academy Technical Specification are satisfied.

---

### 1. Database Initialization (`python sql/setup_db.py`)

```text
============================================================
  RPMS Database Initialization Tool
============================================================
Target Server: localhost:3306
User:          root
Database:      rpms_db
------------------------------------------------------------
Connected to MySQL server successfully.
Database 'rpms_db' created/selected.
Executing SQL file: schema.sql...
Schema applied successfully.
Executing SQL file: seed_data.sql...
Seed data loaded successfully.
------------------------------------------------------------
Database initialization completed successfully!
============================================================
```

---

### 2. Main Console Menu (`python main.py`)

```text
==================================
RECRUITMENT & PLACEMENT SYSTEM
==================================
1. Candidates
2. Companies
3. Jobs
4. Applications
5. Interviews
6. Offers
7. Placements
8. Reports
9. Exit
==================================
Enter choice (1-9): 
```

---

### 3. Candidate Management & Duplicate Validation

#### Adding a Candidate:
```text
--- Candidate Management ---
1. Add Candidate
2. Update Candidate
3. Search Candidates
4. View All Candidates
5. Deactivate Candidate
6. Back to Main Menu
Enter choice (1-6): 1

[+] Add New Candidate
Candidate Full Name: Aarav Sharma
Email: aarav.sharma@example.com
Mobile Number (10 digits): 9823000001
Primary Technology (e.g. Python, Java, DevOps): Python
Percentage (0-100): 84.5
Passing Year (e.g. 2026): 2026
Backlog Count (0 or more): 0
[✓] Candidate created successfully! Assigned ID: CAN1001
```

#### Attempting Duplicate Email / Mobile:
```text
[+] Add New Candidate
Candidate Full Name: Duplicate Tester
Email: aarav.sharma@example.com
Mobile Number (10 digits): 9823000001
...
[x] Failed to add candidate: Validation Error: Candidate with email 'aarav.sharma@example.com' already exists.
```

#### Viewing Candidates:
```text
--- Registered Candidates ---
+---------+-----------------+----------------+------------+------+----------+--------+------------+
| ID      | Name            | Technology     | Percentage | Year | Backlogs | Active | Mobile     |
+---------+-----------------+----------------+------------+------+----------+--------+------------+
| CAN1001 | Aarav Sharma    | Python         | 84.5%      | 2026 | 0        | YES    | 9823000001 |
| CAN1002 | Neha Patel      | Java           | 78.2%      | 2026 | 0        | YES    | 9823000002 |
| CAN1003 | Rohan Kulkarni  | Python         | 62.0%      | 2025 | 2        | YES    | 9823000003 |
| CAN1004 | Pooja Verma     | Full Stack     | 88.0%      | 2026 | 0        | YES    | 9823000004 |
| CAN1005 | Siddharth Rao   | Data Science   | 91.5%      | 2026 | 0        | YES    | 9823000005 |
| CAN1006 | Ananya Deshmukh | Java           | 68.4%      | 2025 | 1        | YES    | 9823000006 |
| CAN1007 | Vikas Gupta     | Python         | 72.5%      | 2026 | 0        | NO     | 9823000007 |
| CAN1008 | Isha Mehta      | DevOps         | 79.0%      | 2026 | 0        | YES    | 9823000008 |
+---------+-----------------+----------------+------------+------+----------+--------+------------+
Total: 8 record(s)
```

---

### 4. Eligibility Assessment Verification (Section 7)

#### Eligible Candidate Check:
```text
--- Application & Eligibility Management ---
Enter choice (1-7): 2

[*] Candidate Eligibility Assessment
Candidate ID: CAN1001
Job ID: JOB101

-------------------------------------------
RESULT: ELIGIBLE [PASS]
-------------------------------------------
 1. Candidate meets all technical, academic, and administrative requirements.
-------------------------------------------
```

#### Ineligible Candidate Check (Multi-Criteria Breakdown):
```text
[*] Candidate Eligibility Assessment
Candidate ID: CAN1003
Job ID: JOB103

-------------------------------------------
RESULT: NOT ELIGIBLE [FAIL]
-------------------------------------------
 1. Percentage criteria not met: Candidate has 62.00%, Job requires minimum 75.00%.
 2. Passing year criteria not met: Candidate passing year is 2025, Job requires 2026.
 3. Backlog criteria not met: Candidate has 2 backlogs, Job allows maximum 0.
-------------------------------------------
```

#### Duplicate Application Blocked:
```text
[+] Submit Job Application
Candidate ID: CAN1001
Job ID: JOB101
[x] DUPLICATE APPLICATION BLOCKED: Duplicate Application Blocked: Candidate 'CAN1001' has already applied for Job 'JOB101'.
```

---

### 5. Recruitment Workflow & Direct Jump Protection (Section 8)

#### Attempting Illegal Direct Jump (APPLIED &rarr; JOINED):
```python
# System raises:
InvalidWorkflowTransitionError: "Invalid recruitment workflow transition for Application 'APP506': Direct jump from 'APPLIED' to 'JOINED' is prohibited. Standard flow is: APPLIED -> SHORTLISTED -> INTERVIEW -> SELECTED -> OFFERED -> JOINED (or REJECTED)."
```

#### Sequential Valid Lifecycle:
1. `APPLIED` &rarr; `SHORTLISTED` (via `shortlist_candidate`)
2. `SHORTLISTED` &rarr; `INTERVIEW` (via `schedule_interview`)
3. `INTERVIEW` &rarr; `SELECTED` (via `select_candidate` after feedback cleared)
4. `SELECTED` &rarr; `OFFERED` (via `issue_offer`)
5. `OFFERED` &rarr; `JOINED` (via `mark_candidate_joined` generating Placement record)

---

### 6. Reports (Sections 12 & 14)

#### Report 1: Candidates by Technology (`dict[str, int]`)
```text
--- Candidates by Technology (dict[str, int]) ---
+-------------------+-----------------+
| Technology Domain | Candidate Count |
+-------------------+-----------------+
| Python            | 4               |
| Java              | 2               |
| Data Science      | 1               |
| DevOps            | 1               |
| Full Stack        | 1               |
+-------------------+-----------------+
Total: 5 record(s)
```

#### Report 2: Open Jobs (`list[Job]`)
```text
--- Active Open Jobs (list[Job]) ---
+--------+----------------------------+-------------------------------------+------------+-----------+----------+------------+
| Job ID | Company                    | Title                               | Technology | Package   | Openings | Deadline   |
+--------+----------------------------+-------------------------------------+------------+-----------+----------+------------+
| JOB101 | Tata Consultancy Services  | Associate Python Developer          | Python     | 4.5 LPA   | 10       | 2026-12-31 |
| JOB102 | Infosys Technologies       | Java Systems Engineer               | Java       | 5.0 LPA   | 15       | 2026-12-15 |
| JOB103 | Google India               | Software Development Engineer - I   | Python     | 18.0 LPA  | 5        | 2026-11-30 |
| JOB104 | Microsoft IDC              | Cloud DevOps Engineer               | DevOps     | 14.5 LPA  | 4        | 2026-11-20 |
+--------+----------------------------+-------------------------------------+------------+-----------+----------+------------+
Total: 4 record(s)
```

#### Report 3: Applications by Status (`dict[str, int]`)
```text
--- Applications by Status (dict[str, int]) ---
+-----------------+--------------------+
| Workflow Status | Applications Count |
+-----------------+--------------------+
| JOINED          | 2                  |
| OFFERED         | 1                  |
| SELECTED        | 1                  |
| INTERVIEW       | 1                  |
| SHORTLISTED     | 1                  |
| APPLIED         | 1                  |
+-----------------+--------------------+
Total: 6 record(s)
```

#### Report 4: Company-wise Placements (`dict[str, int]`)
```text
--- Company-wise Placements (dict[str, int]) ---
+---------------------------+-----------------------+
| Company Name              | Total Placed Students |
+---------------------------+-----------------------+
| Tata Consultancy Services | 2                     |
+---------------------------+-----------------------+
Total: 1 record(s)
```

#### Report 5: Placed Candidates (`list[Placement]`)
```text
--- Placed Candidates (list[Placement]) ---
+--------+---------------------+---------------------------+----------------------------+-----------+--------------+
| ID     | Candidate Name      | Company                   | Designation                | Final CTC | Joining Date |
+--------+---------------------+---------------------------+----------------------------+-----------+--------------+
| PLC401 | Aarav Sharma        | Tata Consultancy Services | Associate Python Developer | 4.8 LPA   | 2026-11-01   |
| PLC402 | Integration Student | Tata Consultancy Services | Software Engineer - Python | 7.5 LPA   | 2026-11-23   |
+--------+---------------------+---------------------------+----------------------------+-----------+--------------+
Total: 2 record(s)
```

#### Report 6: Unplaced Candidates (`list[Candidate]`)
```text
--- Unplaced Candidates Seeking Opportunities (list[Candidate]) ---
+--------------+-----------------+--------------+------------+------+----------+------------+
| Candidate ID | Name            | Technology   | Percentage | Year | Backlogs | Mobile     |
+--------------+-----------------+--------------+------------+------+----------+------------+
| CAN1002      | Neha Patel      | Java         | 78.2%      | 2026 | 0        | 9823000002 |
| CAN1003      | Rohan Kulkarni  | Python       | 62.0%      | 2025 | 2        | 9823000003 |
| CAN1004      | Pooja Verma     | Full Stack   | 88.0%      | 2026 | 0        | 9823000004 |
| CAN1005      | Siddharth Rao   | Data Science | 91.5%      | 2026 | 0        | 9823000005 |
| CAN1006      | Ananya Deshmukh | Java         | 68.4%      | 2025 | 1        | 9823000006 |
| CAN1008      | Isha Mehta      | DevOps       | 79.0%      | 2026 | 0        | 9823000008 |
+--------------+-----------------+--------------+------------+------+----------+------------+
Total: 6 record(s)
```

---

### 7. File Handling Activity Log (`activity_log.txt`)

Contents of `activity_log.txt` (Section 13):
```text
Candidate Created: CAN1001
Job Created: JOB101
Candidate Shortlisted: APP501
Candidate Created: CAN1009
Job Created: JOB106
Candidate Shortlisted: APP507
```

---

### 8. Automated Test Execution (`pytest`)

```text
============================= test session starts =============================
platform win32 -- Python 3.14.0, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\karan\Desktop\AgentX
plugins: anyio-4.15.1
collected 10 items

tests\test_rpms.py .........                                             [ 90%]
tests\test_dao_integration.py .                                          [100%]

============================== 10 passed in 1.45s ==============================
```
