import csv
import os
import tkinter as tk
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import ttk, messagebox

try:
    import cv2
except ImportError:  # pragma: no cover
    cv2 = None

COMPLAINTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "incident_complaints.csv")
MEDIA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captured_media")
DEPARTMENT_ROUTE_MAP = {
    "Public Safety & Crime": "Police",
    "Roads & Traffic": "Road Maintenance",
    "Infrastructure & Utilities": "Utilities",
    "Environment & Sanitation": "Environment Services",
    "Residential & Community": "Community Services",
    "Fire & Medical Rescue": "Fire & Rescue",
}

DEPARTMENT_STANDARD_UPDATES = {
    "Police": [
        "Incident acknowledged and logged.",
        "Case review completed.",
        "Investigation assigned.",
        "Final response submitted.",
    ],
    "Road Maintenance": [
        "Road inspection scheduled.",
        "Traffic management placed.",
        "Temporary repair completed.",
        "Permanent repair sign-off complete.",
    ],
    "Utilities": [
        "Utility issue acknowledged.",
        "Site inspection complete.",
        "Repair crew dispatched.",
        "Service restored.",
    ],
    "Environment Services": [
        "Environment team notified.",
        "Site cleaned and inspected.",
        "Waste removal completed.",
        "Closure review signed off.",
    ],
    "Community Services": [
        "Resident support team notified.",
        "Inspection completed.",
        "Community follow-up arranged.",
        "Resolution confirmed.",
    ],
    "Fire & Rescue": [
        "Emergency response initiated.",
        "Scene assessment complete.",
        "Rescue support completed.",
        "Outcome documented.",
    ],
}

DEPARTMENT_DEMO_ISSUES = {
    "Police": [
        "Suspicious person loitering near a school gate after dark.",
        "Vehicle theft report from a residential parking area.",
        "Break-in alarm triggered at a community market store.",
        "Domestic disturbance reported near a public housing block.",
        "Street harassment complaint on a busy pedestrian crossing.",
        "Unattended bag left outside a metro station entrance.",
        "Noise disturbance from a nightclub after midnight.",
        "Public intoxication complaint outside a bus terminal.",
        "Illegal street vending creating crowding near a mosque.",
        "Suspicious package reported at a municipal office building.",
        "Burglary attempt at a retail shop on the main boulevard.",
        "Motorbike theft near a residential compound gate.",
        "Altercation between neighbors near a community park.",
        "Trespassing complaint at an abandoned warehouse lot.",
        "Threatening message reported by a local resident.",
        "Stolen bicycle recovered outside a school campus.",
        "Illegal dumping near a supermarket with security footage.",
        "Night traffic harassment complaint near a residential street.",
        "Scam call complaint from a senior resident in a housing estate.",
        "Unregistered vehicle driving erratically near a hospital entrance.",
    ],
    "Road Maintenance": [
        "Large pothole has formed near the bus stop on Al Rayyan Road.",
        "Street sign is missing at a junction near a school zone.",
        "Road markings have faded near a major roundabout.",
        "Drainage water is pooling across a lane near a residential area.",
        "A damaged speed bump is creating danger for cyclists.",
        "Concrete barrier is cracked and needs replacement near a worksite.",
        "Road shoulders are eroded beside a bridge access road.",
        "Traffic lights are flickering at an intersection near a clinic.",
        "A utility trench has not been properly repaired on a major road.",
        "Street edge has collapsed near a service lane.",
        "Roadside fence is damaged after a heavy vehicle impact.",
        "A pedestrian crossing is partially missing near a market.",
        "Tree roots are lifting tiles on a city sidewalk.",
        "Power cable warning sign is down near a junction.",
        "A section of asphalt has buckled after rain.",
        "Road humps are deteriorated near a residential neighborhood.",
        "A fallen traffic cone is blocking safety lines on the highway.",
        "Pavement is crumbling near a school bus drop-off point.",
        "A temporary lane closure barrier has been left in the road.",
        "Road surface has developed a deep rut near a bus lane.",
    ],
    "Utilities": [
        "Power outage is affecting several homes on a residential street.",
        "Water leakage is visible beside a public park irrigation line.",
        "Streetlight is flickering and not operating after sunset.",
        "Low water pressure is affecting a multi-unit apartment block.",
        "Exposed electrical cable is seen near a service road.",
        "Water meter box is overflowing near a neighborhood entrance.",
        "Transformer is making a loud humming sound near a school.",
        "Internet cabinet is damaged in a public housing district.",
        "Main water supply line is leaking behind a commercial center.",
        "Gas odor is reported near a residential utility trench.",
        "Downed power line is near a roadside barrier.",
        "Water tank overflow is flooding a nearby walkway.",
        "Streetlight is completely out on a narrow alley.",
        "Main feeder cable is sparking near a maintenance box.",
        "Water quality issue reported from a shared apartment block.",
        "Several homes lost power after a transformer trip.",
        "Utility cabinet door is open beside a single-story building.",
        "Electrical conduit is exposed near a pedestrian path.",
        "Wastewater is pooling near a public utility access point.",
        "Water main burst is causing flooding on a residential street.",
    ],
    "Environment Services": [
        "Garbage piled up outside a public bin near a market square.",
        "Illegal dumping is affecting a roadside green area.",
        "Floodwater is standing beside a pedestrian path after rain.",
        "Dirty drainage canal is causing odor near a residential block.",
        "Solid waste overflow is blocking a public entrance.",
        "Unauthorized waste burn is creating smoke near a housing project.",
        "Open sewage leak is visible beside a roadside ditch.",
        "Blocked storm drain is causing standing water in a park lot.",
        "Waste collection was missed at a residential cluster.",
        "Dead tree branches are obstructing a public road.",
        "Plastic litter is accumulating near a beach access point.",
        "Brush fire risk is growing near a vacant public lot.",
        "A foul smell is coming from an unattended waste container.",
        "Flooded service lane is causing traffic disruption after rainfall.",
        "Bins are overflowing in a city park during peak hours.",
        "Sewage backup is reported in a public toilet block.",
        "A blocked drainage channel is causing road flooding near homes.",
        "Discarded furniture is stacked near a community park entrance.",
        "Smell of contaminated runoff is drifting near a school.",
        "Wastewater is pooling near a residential compound gate.",
    ],
    "Community Services": [
        "Neighbor fence is damaged and affecting access to a shared driveway.",
        "A community complaint about unmaintained landscaping in a housing area.",
        "Children's play equipment is unsafe in a local park.",
        "Blocked garbage collection route is causing neighborhood concerns.",
        "Noise from construction work is affecting nearby residents late at night.",
        "A shared building staircase is poorly lit and unsafe.",
        "Open drain near a playground is causing concern for children.",
        "Residents report unsafe pathways around a community center.",
        "A public garden gate is broken and not secure.",
        "Community wall has collapsed near a local park.",
        "Heating issue reported in a public housing apartment block.",
        "Broken bench and damaged lighting in a community plaza.",
        "A stairwell has a loose railing and needs repair.",
        "Rear access path is overgrown and not safe for residents.",
        "Street dogs are gathering near the local community center.",
        "Pedestrian walkway is obstructed by construction materials.",
        "Residents are reporting poor sanitation in a shared courtyard.",
        "Public noticeboards are damaged near a residential compound.",
        "Lift malfunction is affecting access in a public housing building.",
        "Local park lighting is failing and residents feel unsafe.",
    ],
    "Fire & Rescue": [
        "Smoke odor reported from a warehouse unit near a business district.",
        "Chemical smell detected near a maintenance room in a building.",
        "Fire extinguisher cabinet is damaged and needs inspection.",
        "Vehicle fire alarm triggered near a busy service road.",
        "Cooking fire reported in a small apartment kitchen.",
        "Flammable materials stored near an open public area.",
        "Emergency alarm activated in a school building after maintenance work.",
        "Crowd panic after a false alarm in a shopping center.",
        "Smoke coming from a parked vehicle near a residential block.",
        "Electrical fire risk reported from a workshop unit.",
        "Gas leak smell detected behind a commercial kitchen.",
        "Fire door is blocked in a public building corridor.",
        "A small blaze has been extinguished but needs inspection.",
        "Medical emergency assistance requested outside a public facility.",
        "Waste fire reported near a vacant plot of land.",
        "Vehicle collision with smoke and heat concerns on a highway lane.",
        "Community member reports a suspicious gas odor near a housing estate.",
        "A rooftop air conditioning unit is smoking in a commercial building.",
        "Emergency response needed for a medical case at a bus station.",
        "Fire alarm activation from a residential tower due to electrical fault.",
    ],
}

DEPARTMENT_STATUS_PRIORITY = {"In Progress": 0, "Created": 1, "Received": 1, "Resolved": 2}

WORKFLOW_STEPS = {
    "Public Safety & Crime": [
        "Complaint created",
        "Reported to public safety desk",
        "Reviewed by incident officer",
        "Investigation and response",
        "Resolution and closure",
    ],
    "Roads & Traffic": [
        "Complaint created",
        "Forwarded to road maintenance team",
        "Site inspection scheduled",
        "Repair/traffic control action",
        "Case closed",
    ],
    "Infrastructure & Utilities": [
        "Complaint created",
        "Escalated to utilities team",
        "Service inspection and diagnosis",
        "Repair dispatch",
        "Service restored and closed",
    ],
    "Environment & Sanitation": [
        "Complaint created",
        "Forwarded to sanitation team",
        "Waste/flood inspection",
        "Clean-up or remediation",
        "Closure review",
    ],
    "Residential & Community": [
        "Complaint created",
        "Allocated to community services",
        "On-site review",
        "Resident follow-up",
        "Resolution logged",
    ],
    "Fire & Medical Rescue": [
        "Complaint created",
        "Emergency response dispatch",
        "Scene assessment",
        "Medical or fire intervention",
        "Outcome recorded",
    ],
}


def get_incident_details():
    """Retrieve incident information from the form fields."""
    return {
        "incident_type": "",
        "location": "",
        "description": "",
        "severity": 2,
        "media_type": "",
        "media_path": "",
        "qid": "",
    }


def format_summary(report):
    severity_value = int(report.get("severity", 2))
    severity_labels = {
        1: "Minor",
        2: "Major",
        3: "Urgent",
        4: "Life-Threatening",
    }
    urgency = severity_labels.get(severity_value, "Major")

    lines = [
        "Complaint Summary",
        "-" * 40,
        f"Issue type: {report.get('incident_type', '')}",
        f"Location: {report.get('location', '')}",
        f"Urgency: {urgency} / 4",
        f"Description: {report.get('description', '')}",
    ]

    if report.get("media_path"):
        lines.append(f"Captured live media: {report.get('media_type', 'media').title()} ({os.path.basename(report.get('media_path', ''))})")

    lines.extend([
        "-" * 40,
        "Your complaint has been recorded for the city council review.",
    ])
    return "\n".join(lines)


def display_complaint(report):
    return format_summary(report)


def ensure_complaint_sheet():
    fieldnames = [
        "submitted_at",
        "incident_type",
        "location",
        "severity",
        "description",
        "media_type",
        "media_path",
        "department",
        "status",
        "acknowledged",
        "latest_update",
        "qid",
    ]

    if not os.path.exists(COMPLAINTS_FILE):
        with open(COMPLAINTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        return

    with open(COMPLAINTS_FILE, newline="", encoding="utf-8") as csv_file:
        rows = list(csv.reader(csv_file))

    if not rows:
        with open(COMPLAINTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        return

    existing_headers = rows[0]
    header_map = {"photos": "media_path", "photo": "media_path", "media_path": "media_path"}
    normalized_headers = []
    for header in existing_headers:
        normalized_headers.append(header_map.get(header, header))

    for expected in ["media_type", "media_path", "department", "status", "acknowledged", "latest_update", "qid"]:
        if expected not in normalized_headers:
            normalized_headers.append(expected)

    normalized_rows = [normalized_headers]
    for row in rows[1:]:
        row_values = list(row)
        while len(row_values) < len(normalized_headers):
            row_values.append("")
        if len(row_values) > len(normalized_headers):
            row_values = row_values[:len(normalized_headers)]
        normalized_rows.append(row_values)

    with open(COMPLAINTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(normalized_rows)


def save_complaint_to_sheet(report):
    ensure_complaint_sheet()

    department = report.get("department") or DEPARTMENT_ROUTE_MAP.get(report.get("incident_type", ""), "General")
    record = {
        "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "incident_type": report.get("incident_type", ""),
        "location": report.get("location", ""),
        "severity": report.get("severity", 3),
        "description": report.get("description", ""),
        "media_type": report.get("media_type", ""),
        "media_path": report.get("media_path", ""),
        "department": department,
        "status": report.get("status", "Received"),
        "acknowledged": report.get("acknowledged", "False"),
        "latest_update": report.get("latest_update", "Complaint submitted and awaiting team review."),
        "qid": report.get("qid", ""),
    }

    with open(COMPLAINTS_FILE, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[
            "submitted_at",
            "incident_type",
            "location",
            "severity",
            "description",
            "media_type",
            "media_path",
            "department",
            "status",
            "acknowledged",
            "latest_update",
            "qid",
        ])
        writer.writerow(record)


def seed_demo_department_issues():
    if not os.path.exists(COMPLAINTS_FILE):
        ensure_complaint_sheet()

    base_time = datetime(2026, 8, 1, 8, 0, 0)
    all_rows = []

    for department, issues in DEPARTMENT_DEMO_ISSUES.items():
        for index in range(5):
            detail = issues[index % len(issues)]
            record = {
                "submitted_at": (base_time + timedelta(minutes=index * 17 + (len(DEPARTMENT_DEMO_ISSUES) * 5))).strftime("%Y-%m-%d %H:%M:%S"),
                "incident_type": department,
                "location": f"{department} Zone {index + 1}",
                "severity": (index % 4) + 1,
                "description": detail,
                "media_type": "photo" if index % 2 == 0 else "video",
                "media_path": f"{department.lower().replace(' ', '_')}_{index + 1}.png",
                "department": department,
                "status": "Created",
                "acknowledged": "False",
                "latest_update": "Complaint created and awaiting department review.",
                "qid": "1234567",
            }
            all_rows.append(record)

    fieldnames = [
        "submitted_at",
        "incident_type",
        "location",
        "severity",
        "description",
        "media_type",
        "media_path",
        "department",
        "status",
        "acknowledged",
        "latest_update",
        "qid",
    ]

    with open(COMPLAINTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)


class IncidentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Madinati - City Infrastructure Incident Complaint Form")
        self.geometry("820x660")
        self.minsize(700, 560)
        self.resizable(True, True)

        self.configure(padx=18, pady=18)

        title = ttk.Label(
            self,
            text="Madinati - City Infrastructure Incident Complaint Form",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", pady=(0, 18))

        self.auth_frame = ttk.Frame(self)
        self.auth_frame.pack(fill="x", pady=(0, 12))

        ttk.Label(self.auth_frame, text="Mandatory Sign-in", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        ttk.Label(self.auth_frame, text="Authenticate using a Qatar ID or Driver's License to continue.", foreground="#555555").pack(anchor="w", pady=(4, 8))

        auth_row = ttk.Frame(self.auth_frame)
        auth_row.pack(fill="x")

        ttk.Label(auth_row, text="ID type:", font=("Segoe UI", 10, "bold")).pack(side="left")
        self.auth_type_var = tk.StringVar(value="Qatar ID")
        self.auth_type_combo = ttk.Combobox(
            auth_row,
            textvariable=self.auth_type_var,
            values=["Qatar ID", "Driver's License"],
            state="readonly",
            width=18,
        )
        self.auth_type_combo.pack(side="left", padx=(8, 12))

        self.auth_id_var = tk.StringVar()
        self.auth_entry = ttk.Entry(auth_row, textvariable=self.auth_id_var, width=28)
        self.auth_entry.pack(side="left")

        ttk.Button(auth_row, text="Sign In", command=self.authenticate_user).pack(side="left", padx=(12, 0))

        self.auth_status_var = tk.StringVar(value="Not signed in")
        ttk.Label(self.auth_frame, textvariable=self.auth_status_var, foreground="#8a3b0f").pack(anchor="w", pady=(8, 0))

        subtitle = ttk.Label(
            self,
            text="Please provide details about the incident.",
            font=("Segoe UI", 11),
        )
        subtitle.pack(anchor="w", pady=(0, 16))

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.status_banner_var = tk.StringVar(value="")
        self.status_banner = ttk.Label(self, textvariable=self.status_banner_var, background="#eefaf3", foreground="#0d5a3a", padding=(12, 8), anchor="w")
        self.status_banner.pack(fill="x", pady=(0, 8))
        self.status_banner_job = None

        self.main_frame = ttk.Frame(self.notebook, padding=18)
        self.notebook.add(self.main_frame, text="Report Incident")

        self.contacts_tab = ttk.Frame(self.notebook, padding=18)
        self.notebook.add(self.contacts_tab, text="Emergency Contacts")

        self.log_tab = ttk.Frame(self.notebook, padding=18)
        self.notebook.add(self.log_tab, text="Complaint Log")

        self.department_tab = ttk.Frame(self.notebook, padding=18)
        self.notebook.add(self.department_tab, text="Department Queue")

        self.is_signed_in = False
        self.authenticated_id = ""
        self._lock_form_until_auth()

        self.fields = {
            "location": self._create_entry("Where is the issue located?", "road, area, landmark, address"),
        }
        self.media_type = ""
        self.media_path = ""

        self.sector_var = tk.StringVar(value="Public Safety & Crime")
        self.sectors = [
            "Public Safety & Crime",
            "Roads & Traffic",
            "Infrastructure & Utilities",
            "Environment & Sanitation",
            "Residential & Community",
            "Fire & Medical Rescue",
        ]

        sector_frame = ttk.Frame(self.main_frame)
        sector_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(sector_frame, text="Select the issue sector:", font=("Segoe UI", 10, "bold")).pack(anchor="w")

        self.sector_buttons = {}
        sector_row = ttk.Frame(sector_frame)
        sector_row.pack(fill="x", pady=(6, 0))

        for sector in self.sectors:
            button = tk.Button(
                sector_row,
                text=sector,
                width=22,
                bg="#e8f2ff",
                activebackground="#dcecff",
                relief="raised",
                bd=1,
                command=lambda selected=sector: self.select_sector(selected),
            )
            button.pack(side="left", padx=(0, 8), pady=(0, 8))
            self.sector_buttons[sector] = button

        self.select_sector("Public Safety & Crime")

        detail_row = ttk.Frame(self.main_frame)
        detail_row.pack(fill="both", expand=True, pady=6)

        self.description_frame = ttk.Frame(detail_row)
        self.description_frame.pack(side="left", fill="both", expand=True)
        self.fields["description"] = self._create_text_area("Please describe the issue in detail.", self.description_frame)

        self.photo_frame = ttk.Frame(detail_row)
        self.photo_frame.pack(side="left", fill="y", padx=(18, 0), pady=(0, 0))
        ttk.Label(self.photo_frame, text="Live media evidence", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        ttk.Button(self.photo_frame, text="Capture Live Photo", command=lambda: self.capture_live_media("photo")).pack(anchor="w", pady=(6, 4))
        ttk.Button(self.photo_frame, text="Record 3s Live Video", command=lambda: self.capture_live_media("video")).pack(anchor="w", pady=(0, 8))
        self.photo_listbox = tk.Listbox(self.photo_frame, width=34, height=7)
        self.photo_listbox.pack(fill="y", expand=True)

        severity_frame = ttk.Frame(self.main_frame)
        severity_frame.pack(fill="x", pady=(8, 10))
        ttk.Label(severity_frame, text="Urgency:", font=("Segoe UI", 10, "bold")).pack(anchor="w")

        self.severity_var = tk.StringVar(value="Major")
        self.severity_levels = {
            "Minor": {"label": "🟢 Minor", "value": 1, "color": "#d9f2d9"},
            "Major": {"label": "🟡 Major", "value": 2, "color": "#fff1b8"},
            "Urgent": {"label": "🟠 Urgent", "value": 3, "color": "#f9d7a5"},
            "Life-Threatening": {"label": "🔴 Life-Threatening", "value": 4, "color": "#f7c7c7"},
        }

        urgency_row = ttk.Frame(severity_frame)
        urgency_row.pack(fill="x", pady=(6, 0))
        self.severity_buttons = {}

        for key, config in self.severity_levels.items():
            button = tk.Button(
                urgency_row,
                text=config["label"],
                width=14,
                bg=config["color"],
                activebackground=config["color"],
                relief="raised",
                bd=1,
                command=lambda selected=key: self.select_severity(selected),
            )
            button.pack(side="left", padx=(0, 8))
            self.severity_buttons[key] = button

        self.select_severity("Major")

        buttons = ttk.Frame(self.main_frame)
        buttons.pack(fill="x", pady=(18, 10))
        ttk.Button(buttons, text="Submit Complaint", command=self.submit_form).pack(side="left")
        ttk.Button(buttons, text="Clear", command=self.clear_form).pack(side="left", padx=(10, 0))

        summary_label = ttk.Label(self.main_frame, text="Complaint Summary", font=("Segoe UI", 12, "bold"))
        summary_label.pack(anchor="w", pady=(12, 6))

        self.summary = tk.Text(self.main_frame, height=8, width=90, wrap="word", state="disabled")
        self.summary.pack(fill="both", expand=True)

        seed_demo_department_issues()
        self._render_contact_directory()
        self._render_complaint_log_table()
        self._render_department_queue()
        self.clear_form()

    def authenticate_user(self):
        auth_type = self.auth_type_var.get().strip()
        auth_value = self.auth_id_var.get().strip()

        if not auth_type or not auth_value:
            self.auth_status_var.set("Please enter a valid Qatar ID or Driver's License.")
            messagebox.showerror("Authentication required", "Please enter a valid Qatar ID or Driver's License to continue.")
            return

        self.is_signed_in = True
        self.authenticated_id = auth_value
        self.auth_status_var.set(f"Signed in successfully ({auth_type} accepted in prototype mode).")
        self._unlock_form_after_auth()
        messagebox.showinfo("Prototype authentication", f"{auth_type} accepted for demo purposes. This is a prototype and any entered ID is treated as valid.")

    def _lock_form_until_auth(self):
        self.notebook.tab(self.main_frame, state="disabled")
        self.notebook.tab(self.contacts_tab, state="disabled")
        self.notebook.tab(self.log_tab, state="disabled")
        self.notebook.tab(self.department_tab, state="disabled")

    def _unlock_form_after_auth(self):
        self.notebook.tab(self.main_frame, state="normal")
        self.notebook.tab(self.contacts_tab, state="normal")
        self.notebook.tab(self.log_tab, state="normal")
        self.notebook.tab(self.department_tab, state="normal")

    def _render_contact_directory(self):
        contact_rows = [
            ("Police Emergency", "999", "Emergency police response"),
            ("Fire & Rescue", "911", "Fire and rescue assistance"),
            ("Road Maintenance", "188", "Potholes, road hazards, signage"),
            ("Water & Sewer Services", "991", "Leaks, burst pipes, drainage"),
            ("Electricity / Power", "991", "Power outages and exposed wires"),
            ("Waste Management", "184", "Illegal dumping and missed pickups"),
            ("Public Works", "184", "Street maintenance and public infrastructure"),
            ("City Service Hotline", "184", "General infrastructure reporting"),
        ]

        ttk.Label(self.contacts_tab, text="Infrastructure and emergency contact list", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 10))

        columns = ("department", "phone", "details")
        contacts_table = ttk.Treeview(self.contacts_tab, columns=columns, show="headings", height=12)
        contacts_table.heading("department", text="Department")
        contacts_table.heading("phone", text="Phone")
        contacts_table.heading("details", text="Service")
        contacts_table.column("department", width=220, anchor="w")
        contacts_table.column("phone", width=150, anchor="center")
        contacts_table.column("details", width=330, anchor="w")
        contacts_table.pack(fill="both", expand=True)

        for department, phone, details in contact_rows:
            contacts_table.insert("", tk.END, values=(department, phone, details))

    def _render_complaint_log_table(self):
        ttk.Label(self.log_tab, text="Complaint Register", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 10))

        columns = ("submitted_at", "incident_type", "location", "severity", "status", "department", "description", "qid")
        self.complaint_table = ttk.Treeview(self.log_tab, columns=columns, show="headings", height=12)
        self.complaint_table.heading("submitted_at", text="Submitted")
        self.complaint_table.heading("incident_type", text="Sector")
        self.complaint_table.heading("location", text="Location")
        self.complaint_table.heading("severity", text="Urgency")
        self.complaint_table.heading("status", text="Status")
        self.complaint_table.heading("department", text="Department")
        self.complaint_table.heading("description", text="Description")
        self.complaint_table.heading("qid", text="QID")
        self.complaint_table.column("submitted_at", width=150, anchor="w")
        self.complaint_table.column("incident_type", width=150, anchor="w")
        self.complaint_table.column("location", width=150, anchor="w")
        self.complaint_table.column("severity", width=90, anchor="center")
        self.complaint_table.column("status", width=100, anchor="center")
        self.complaint_table.column("department", width=140, anchor="w")
        self.complaint_table.column("description", width=260, anchor="w")
        self.complaint_table.column("qid", width=120, anchor="w")
        self.complaint_table.pack(fill="both", expand=True)
        self.complaint_table.bind("<ButtonRelease-1>", self.open_selected_complaint)

        delete_frame = ttk.Frame(self.log_tab)
        delete_frame.pack(fill="x", pady=(8, 0))
        ttk.Button(delete_frame, text="Delete Selected Request", command=self.delete_selected_complaint).pack(anchor="e")
        self.refresh_complaint_log()

    def refresh_complaint_log(self):
        for row in self.complaint_table.get_children():
            self.complaint_table.delete(row)

        if not os.path.exists(COMPLAINTS_FILE):
            return

        with open(COMPLAINTS_FILE, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                severity_label = {
                    "1": "Minor",
                    "2": "Major",
                    "3": "Urgent",
                    "4": "Life-Threatening",
                }.get(str(row.get("severity", "2")), row.get("severity", "2"))
                self.complaint_table.insert("", tk.END, values=(
                    row.get("submitted_at", ""),
                    row.get("incident_type", ""),
                    row.get("location", ""),
                    severity_label,
                    row.get("status", "Received"),
                    row.get("department", DEPARTMENT_ROUTE_MAP.get(row.get("incident_type", ""), "General")),
                    row.get("description", ""),
                    row.get("qid", ""),
                ))

    def open_selected_complaint(self, event):
        selection = self.complaint_table.selection()
        if not selection:
            return

        row_values = self.complaint_table.item(selection[0], "values")
        if not row_values:
            return

        record = {
            "submitted_at": row_values[0],
            "incident_type": row_values[1],
            "location": row_values[2],
            "severity": row_values[3],
            "status": row_values[4],
            "department": row_values[5],
            "description": row_values[6],
            "qid": row_values[7],
        }
        self.show_complaint_details(record)

    def delete_selected_complaint(self):
        selection = self.complaint_table.selection()
        if not selection:
            messagebox.showwarning("No request selected", "Please select a complaint from the table first.")
            return

        row_values = self.complaint_table.item(selection[0], "values")
        if not row_values:
            return

        match = {
            "submitted_at": row_values[0],
            "incident_type": row_values[1],
            "location": row_values[2],
            "qid": row_values[7],
        }

        if not os.path.exists(COMPLAINTS_FILE):
            return

        with open(COMPLAINTS_FILE, newline="", encoding="utf-8") as csv_file:
            rows = list(csv.DictReader(csv_file))

        filtered_rows = [
            row for row in rows
            if not (
                row.get("submitted_at") == match["submitted_at"]
                and row.get("incident_type") == match["incident_type"]
                and row.get("location") == match["location"]
                and row.get("qid") == match["qid"]
            )
        ]

        with open(COMPLAINTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
            fieldnames = [
                "submitted_at",
                "incident_type",
                "location",
                "severity",
                "description",
                "media_type",
                "media_path",
                "department",
                "status",
                "acknowledged",
                "latest_update",
                "qid",
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)

        self.refresh_complaint_log()
        self.refresh_department_queue()

    def show_complaint_details(self, record):
        detail_window = tk.Toplevel(self)
        detail_window.title("Complaint Details")
        detail_window.geometry("620x420")

        ttk.Label(detail_window, text="Complaint Details", font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=18, pady=(18, 8))

        info = tk.Text(detail_window, height=12, wrap="word")
        info.pack(fill="both", expand=True, padx=18, pady=(0, 12))

        status = record.get("status", "Received")
        department = record.get("department", DEPARTMENT_ROUTE_MAP.get(record.get("incident_type", ""), "General"))
        acknowledged = "Yes" if self._read_record_from_csv(record).get("acknowledged", "False").lower() == "true" else "No"
        update = self._read_record_from_csv(record).get("latest_update", "No latest update recorded.")

        info.insert("1.0", (
            f"Submitted: {record.get('submitted_at', '')}\n"
            f"Sector: {record.get('incident_type', '')}\n"
            f"Location: {record.get('location', '')}\n"
            f"Urgency: {record.get('severity', '')}\n"
            f"Department: {department}\n"
            f"Status: {status}\n"
            f"Acknowledged: {acknowledged}\n"
            f"QID: {record.get('qid', '')}\n"
            f"Description: {record.get('description', '')}\n"
            f"Latest update: {update}\n"
        ))
        info.config(state="disabled")

        ttk.Button(detail_window, text="Close", command=detail_window.destroy).pack(anchor="e", padx=18, pady=(0, 18))

    def _render_department_queue(self):
        ttk.Label(self.department_tab, text="Department Operations Queue", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 10))

        controls = ttk.Frame(self.department_tab)
        controls.pack(fill="x", pady=(0, 10))
        ttk.Label(controls, text="Select department:").pack(side="left")
        self.department_filter_var = tk.StringVar(value="Police")
        self.department_filter = ttk.Combobox(controls, textvariable=self.department_filter_var, values=[
            "Police",
            "Road Maintenance",
            "Utilities",
            "Environment Services",
            "Community Services",
            "Fire & Rescue",
        ], state="readonly", width=22)
        self.department_filter.pack(side="left", padx=(8, 12))
        self.department_filter.bind("<<ComboboxSelected>>", lambda event: self.refresh_department_queue())

        ttk.Button(controls, text="Refresh", command=self.refresh_department_queue).pack(side="left")

        columns = ("submitted_at", "incident_type", "location", "status", "description", "latest_update", "qid")
        self.department_table = ttk.Treeview(self.department_tab, columns=columns, show="headings", height=8)
        self.department_table.heading("submitted_at", text="Submitted")
        self.department_table.heading("incident_type", text="Sector")
        self.department_table.heading("location", text="Location")
        self.department_table.heading("status", text="Status")
        self.department_table.heading("description", text="Description")
        self.department_table.heading("latest_update", text="Latest Update")
        self.department_table.heading("qid", text="QID")
        self.department_table.column("submitted_at", width=120, anchor="w")
        self.department_table.column("incident_type", width=130, anchor="w")
        self.department_table.column("location", width=130, anchor="w")
        self.department_table.column("status", width=90, anchor="center")
        self.department_table.column("description", width=220, anchor="w")
        self.department_table.column("latest_update", width=220, anchor="w")
        self.department_table.column("qid", width=120, anchor="w")
        self.department_table.pack(fill="both", expand=True, pady=(0, 8))

        self.department_table.bind("<<TreeviewSelect>>", self._on_department_issue_selected)

        update_panel = ttk.LabelFrame(self.department_tab, text="Selected issue update")
        update_panel.pack(fill="x", pady=(0, 10))

        ttk.Label(update_panel, text="Custom update:").pack(anchor="w", padx=10, pady=(10, 0))
        self.department_update_box = tk.Text(update_panel, height=4, wrap="word", padx=6, pady=6)
        self.department_update_box.pack(fill="x", padx=10, pady=(4, 10))

        action_frame = ttk.Frame(update_panel)
        action_frame.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Button(action_frame, text="Submit", command=self.submit_department_update).pack(side="left")
        ttk.Button(action_frame, text="Received", command=self.mark_issue_received).pack(side="left", padx=(12, 0))
        ttk.Button(action_frame, text="In Progress", command=lambda: self.update_selected_issue_status("In Progress")).pack(side="left", padx=(12, 0))
        ttk.Button(action_frame, text="Completed", command=lambda: self.update_selected_issue_status("Resolved")).pack(side="left", padx=(12, 0))

        self.refresh_department_queue()

    def _on_department_issue_selected(self, event=None):
        self.department_update_box.delete("1.0", tk.END)

        selected = self.department_table.selection()
        if not selected:
            return

        selected_row = self.department_table.item(selected[0], "values")
        if not selected_row:
            return

        row_record = {
            "submitted_at": selected_row[0],
            "incident_type": selected_row[1],
            "location": selected_row[2],
            "status": selected_row[3],
            "qid": selected_row[6],
        }
        current_update = self._read_record_from_csv(row_record).get("latest_update", "")
        if current_update:
            self.department_update_box.insert("1.0", current_update)

    def refresh_department_queue(self):
        selected_department = self.department_filter_var.get()
        self.department_update_box.delete("1.0", tk.END)

        for row in self.department_table.get_children():
            self.department_table.delete(row)

        if not os.path.exists(COMPLAINTS_FILE):
            return

        department_rows = []
        with open(COMPLAINTS_FILE, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row_department = row.get("department") or DEPARTMENT_ROUTE_MAP.get(row.get("incident_type"), "General")
                if row_department != selected_department:
                    continue
                department_rows.append(row)

        department_rows.sort(key=lambda row: (DEPARTMENT_STATUS_PRIORITY.get(row.get("status", "Received"), 99), row.get("submitted_at", "")))

        for row in department_rows:
            self.department_table.insert("", tk.END, values=(
                row.get("submitted_at", ""),
                row.get("incident_type", ""),
                row.get("location", ""),
                row.get("status", "Created"),
                row.get("description", ""),
                row.get("latest_update", "Complaint submitted and awaiting team review."),
                row.get("qid", ""),
            ))

    def _read_record_from_csv(self, record):
        if not os.path.exists(COMPLAINTS_FILE):
            return {}

        with open(COMPLAINTS_FILE, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if (
                    row.get("submitted_at") == record.get("submitted_at")
                    and row.get("incident_type") == record.get("incident_type")
                    and row.get("location") == record.get("location")
                    and row.get("qid") == record.get("qid")
                ):
                    return row
        return {}

    def _get_department_update_message(self):
        custom_update = self.department_update_box.get("1.0", tk.END).strip()
        if custom_update:
            return custom_update
        return "Issue updated by the department."

    def _build_status_update_message(self, status_name, custom_update=""):
        custom_update = (custom_update or "").strip()
        if status_name == "Received":
            return "This issue was received."
        if status_name == "In Progress":
            return custom_update if custom_update else "This issue is now in progress."
        if status_name == "Resolved":
            return "This problem was resolved."
        return custom_update if custom_update else "Issue updated by the department."

    def submit_department_update(self):
        record = self._get_selected_department_record()
        if record is None:
            messagebox.showwarning("No issue selected", "Please select an issue from the department queue first.")
            return
        custom_update = self._get_department_update_message()
        current_status = record.get("status", "Received")
        update_message = self._build_status_update_message(current_status, custom_update)
        self._update_issue_row(record, {"status": current_status, "acknowledged": "True", "latest_update": update_message})
        self.department_update_box.delete("1.0", tk.END)
        self.refresh_department_queue()
        self.refresh_complaint_log()
        self.show_notification_banner(record.get("qid", "Unknown"), current_status)

    def mark_issue_received(self):
        record = self._get_selected_department_record()
        if record is None:
            messagebox.showwarning("No issue selected", "Please select an issue from the department queue first.")
            return
        custom_update = self._get_department_update_message()
        update_message = self._build_status_update_message("Received", custom_update)
        self._update_issue_row(record, {"status": "Received", "acknowledged": "True", "latest_update": update_message})
        self.department_update_box.delete("1.0", tk.END)
        self.refresh_department_queue()
        self.refresh_complaint_log()
        self.show_notification_banner(record.get("qid", "Unknown"), "Received")

    def update_selected_issue_status(self, next_status):
        record = self._get_selected_department_record()
        if record is None:
            messagebox.showwarning("No issue selected", "Please select an issue from the department queue first.")
            return
        custom_update = self._get_department_update_message()
        if next_status == "In Progress":
            final_status = "In Progress"
        elif next_status == "Resolved":
            final_status = "Resolved"
        else:
            final_status = next_status
        update_message = self._build_status_update_message(final_status, custom_update)
        self._update_issue_row(record, {"status": final_status, "acknowledged": "True", "latest_update": update_message})
        self.department_update_box.delete("1.0", tk.END)
        self.refresh_department_queue()
        self.refresh_complaint_log()
        self.show_notification_banner(record.get("qid", "Unknown"), final_status)

    def _get_selected_department_record(self):
        selection = self.department_table.selection()
        if not selection:
            return None
        row_values = self.department_table.item(selection[0], "values")
        if not row_values:
            return None
        return {
            "submitted_at": row_values[0],
            "incident_type": row_values[1],
            "location": row_values[2],
            "status": row_values[3],
            "qid": row_values[6],
        }

    def _update_issue_row(self, record, updates):
        if not os.path.exists(COMPLAINTS_FILE):
            return

        with open(COMPLAINTS_FILE, newline="", encoding="utf-8") as csv_file:
            rows = list(csv.DictReader(csv_file))

        fieldnames = list(rows[0].keys()) if rows else [
            "submitted_at",
            "incident_type",
            "location",
            "severity",
            "description",
            "media_type",
            "media_path",
            "department",
            "status",
            "acknowledged",
            "latest_update",
            "qid",
        ]

        for row in rows:
            matches = (
                row.get("submitted_at") == record.get("submitted_at")
                and row.get("incident_type") == record.get("incident_type")
                and row.get("location") == record.get("location")
                and row.get("qid") == record.get("qid")
            )
            if matches:
                row.update(updates)
                break

        with open(COMPLAINTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def show_notification_banner(self, qid, current_status):
        label = qid or "this issue"
        if current_status == "Received":
            message = f"Your issue for {label} was acknowledged."
        elif current_status == "In Progress":
            message = f"Your issue for {label} was moved to In Progress."
        elif current_status == "Resolved":
            message = f"Your issue for {label} was resolved."
        else:
            message = f"Your issue for {label} was updated."
        self.status_banner_var.set(message)

    def select_sector(self, sector):
        self.sector_var.set(sector)
        for key, button in self.sector_buttons.items():
            if key == sector:
                button.config(relief="sunken", borderwidth=2, bg="#cfe7ff")
            else:
                button.config(relief="raised", borderwidth=1, bg="#e8f2ff")

    def _create_entry(self, label_text, placeholder):
        frame = ttk.Frame(self.main_frame)
        frame.pack(fill="x", pady=6)
        ttk.Label(frame, text=label_text, font=("Segoe UI", 10, "bold")).pack(anchor="w")
        entry = ttk.Entry(frame)
        entry.insert(0, placeholder)
        entry.configure(foreground="#666666")
        entry.bind("<FocusIn>", lambda event, e=entry, p=placeholder: self._clear_placeholder(e, p))
        entry.bind("<FocusOut>", lambda event, e=entry, p=placeholder: self._restore_placeholder(e, p))
        entry.pack(fill="x", pady=(4, 0))
        return entry

    def _create_text_area(self, label_text, parent=None):
        frame = ttk.Frame(parent if parent is not None else self.main_frame)
        frame.pack(fill="both", expand=True, pady=6)
        ttk.Label(frame, text=label_text, font=("Segoe UI", 10, "bold")).pack(anchor="w")
        text = tk.Text(frame, height=10, wrap="word")
        text.pack(fill="both", expand=True, pady=(4, 0))
        return text

    def capture_live_media(self, media_type):
        if cv2 is None:
            messagebox.showerror("Camera unavailable", "OpenCV is required for live photo/video capture.")
            return

        os.makedirs(MEDIA_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_extension = "png" if media_type == "photo" else "mp4"
        media_name = f"incident_{media_type}_{timestamp}.{file_extension}"
        media_path = os.path.join(MEDIA_DIR, media_name)

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Camera unavailable", "No camera was detected. Please check the device and try again.")
            return

        try:
            if media_type == "photo":
                ret, frame = cap.read()
                if not ret:
                    messagebox.showerror("Capture failed", "Unable to capture a live photo.")
                    return
                cv2.imwrite(media_path, frame)
            else:
                video_writer = cv2.VideoWriter(
                    media_path,
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    20.0,
                    (640, 480),
                )
                if not video_writer.isOpened():
                    messagebox.showerror("Capture failed", "Unable to start live video recording.")
                    return
                for _ in range(60):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    video_writer.write(frame)
                video_writer.release()

            self.media_type = media_type
            self.media_path = media_path
            self._refresh_photo_list()
            messagebox.showinfo("Media captured", f"Live {media_type} saved successfully.")
        finally:
            cap.release()

    def _refresh_photo_list(self):
        self.photo_listbox.delete(0, tk.END)
        if self.media_path:
            self.photo_listbox.insert(tk.END, f"{self.media_type.title()} captured: {os.path.basename(self.media_path)}")
        else:
            self.photo_listbox.insert(tk.END, "No live media captured yet")

    def select_severity(self, level):
        self.severity_var.set(level)
        for key, button in self.severity_buttons.items():
            if key == level:
                button.config(relief="sunken", borderwidth=2)
            else:
                button.config(relief="raised", borderwidth=1)

    def _clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.configure(foreground="#000000")

    def _restore_placeholder(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(foreground="#666666")

    def get_report_data(self):
        severity_key = self.severity_var.get()
        severity_value = self.severity_levels.get(severity_key, {"value": 3})["value"]

        report = {
            "incident_type": self.sector_var.get().strip(),
            "location": self.fields["location"].get().strip(),
            "description": self.fields["description"].get("1.0", tk.END).strip(),
            "severity": severity_value,
            "media_type": self.media_type,
            "media_path": self.media_path,
            "qid": self.authenticated_id,
        }

        if report["location"] in ("", "road, area, landmark, address"):
            report["location"] = ""

        return report

    def submit_form(self):
        if not self.verify_authentication():
            return

        report = self.get_report_data()

        if not self.authenticated_id:
            messagebox.showerror("Authentication required", "Please sign in with a Qatar ID or Driver's License before continuing.")
            return
        if not report["incident_type"]:
            messagebox.showerror("Missing information", "Please select the issue sector.")
            return
        if not report["location"]:
            messagebox.showerror("Missing information", "Please enter the location of the issue.")
            return
        if not report["description"]:
            messagebox.showerror("Missing information", "Please describe the issue in detail.")
            return

        severity_value = int(report["severity"])
        if not 1 <= severity_value <= 4:
            messagebox.showerror("Invalid severity", "Severity must be between 1 and 4.")
            return

        save_complaint_to_sheet(report)
        self.refresh_complaint_log()
        self.clear_form()

        summary = display_complaint(report)
        self.summary.config(state="normal")
        self.summary.delete("1.0", tk.END)
        self.summary.insert("1.0", summary)
        self.summary.config(state="disabled")

    def clear_form(self):
        for key, field in self.fields.items():
            if isinstance(field, tk.Text):
                field.delete("1.0", tk.END)
            else:
                field.delete(0, tk.END)
                if key == "location":
                    field.insert(0, "road, area, landmark, address")
                    field.configure(foreground="#666666")

        self.media_type = ""
        self.media_path = ""
        self._refresh_photo_list()
        self.select_sector("Public Safety & Crime")
        self.select_severity("Major")
        self.summary.config(state="normal")
        self.summary.delete("1.0", tk.END)
        self.summary.insert("1.0", "Your complaint summary will appear here after submission.")
        self.summary.config(state="disabled")

    def verify_authentication(self):
        if not self.is_signed_in:
            messagebox.showerror("Authentication required", "Please sign in with a Qatar ID or Driver's License before continuing.")
            return False
        return True


if __name__ == "__main__":
    app = IncidentApp()
    app.mainloop()
