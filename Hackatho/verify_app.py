import csv
import py_compile
py_compile.compile('main.py', doraise=True)
from main import IncidentApp, COMPLAINTS_FILE, save_complaint_to_sheet

app = IncidentApp()
app.auth_type_var.set('Qatar ID')
app.auth_id_var.set('1234567890')
app.authenticate_user()
app.sector_var.set('Roads & Traffic')
app.fields['location'].delete(0, 'end')
app.fields['location'].insert(0, 'Main Street')
app.fields['description'].delete('1.0', 'end')
app.fields['description'].insert('1.0', 'Large pothole')
app.media_type = 'photo'
app.media_path = 'demo_capture.png'
app.select_severity('Urgent')
report = app.get_report_data()
report['qid'] = app.authenticated_id
save_complaint_to_sheet(report)
app.refresh_complaint_log()
with open(COMPLAINTS_FILE, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last['qid'] == '1234567890'
assert last['incident_type'] == 'Roads & Traffic'
assert app.complaint_table.get_children()
print('OK')
app.destroy()
