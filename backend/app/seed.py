"""Idempotent, clearly unverified seed directory; no fabricated phone numbers/hours."""
from sqlalchemy import select
from .db import Category, Service, SessionLocal
from .ai import embed

# Each entry describes an office or a service offered by an office, not 50 distinct offices.
# Official destination URLs are review candidates; verify individual fields before marking verified.
GROUPS={
 'Money & aid':[
 ('Student Accounts','Tuition billing, payment plans and account balances.','tuition payment bill balance fees','https://www.uta.edu/business-affairs/student-accounts'),
 ('Financial Aid & Scholarships','Financial aid applications, FAFSA and aid award questions.','fafsa financial aid award grant','https://www.uta.edu/administration/fao'),
 ('Scholarship Support','Find information about scholarships and scholarship applications.','scholarship funding merit','https://www.uta.edu/administration/fao/scholarships'),
 ('Student Money Management','Budgeting, personal finance and financial education resources.','budget money finance savings debt','https://www.uta.edu/business-affairs/student-accounts'),
 ('Emergency Financial Assistance','Find university resources for emergency financial needs.','emergency financial crisis unexpected expenses','https://www.uta.edu/student-affairs/dos'),
 ('Veteran Education Benefits','Support for military-connected students using education benefits.','veteran military gi bill benefits','https://www.uta.edu/student-affairs/veterans'),
 ],
 'Academics':[
 ('University Advising','Academic advising, choosing classes and planning degree progress.','advising classes degree courses major','https://www.uta.edu/student-success/advising'),
 ('Tutoring & Academic Success','Tutoring and study resources for academic coursework.','tutoring tutor homework study coursework','https://www.uta.edu/student-success'),
 ('Writing Center','Writing consultations for essays, papers and academic projects.','writing essay paper draft proofreading','https://www.uta.edu/owl'),
 ('UTA Libraries','Library collections, research support and study resources.','library research books databases','https://libraries.uta.edu/'),
 ('Registrar','Registration, enrollment records and academic calendar information.','registrar enrollment registration records','https://www.uta.edu/administration/registrar'),
 ('Transcript Requests','Find instructions for requesting an academic transcript.','transcript official academic record','https://www.uta.edu/administration/registrar'),
 ('Graduation Information','Graduation application and commencement planning resources.','graduation commencement graduate application','https://www.uta.edu/administration/registrar'),
 ('TRIO Student Support Services','Academic coaching and support for eligible students.','trio first generation academic coaching','https://www.uta.edu/student-success/trio'),
 ('Undergraduate Research','Explore undergraduate research opportunities and support.','undergraduate research faculty laboratory','https://www.uta.edu/research'),
 ('Graduate School','Graduate education resources, policies and student support.','graduate masters phd doctoral dissertation','https://www.uta.edu/academics/schools-colleges/gradschool'),
 ('Supplemental Instruction','Find supported courses and collaborative study sessions.','supplemental instruction group study review','https://www.uta.edu/student-success'),
 ('Math Support','Locate tutoring and support resources for mathematics courses.','math mathematics calculus algebra','https://www.uta.edu/student-success'),
 ],
 'Health & wellbeing':[
 ('Health Services','Student health services and information about accessing care.','health doctor clinic sick medical','https://www.uta.edu/student-affairs/health-services'),
 ('Counseling & Psychological Services','Counseling and psychological support resources for students.','counseling anxiety stress mental wellbeing','https://www.uta.edu/student-affairs/caps'),
 ('Student Access & Resource Center','Disability access, accommodations and resource support.','disability accommodations access accessible','https://www.uta.edu/student-affairs/sarcenter'),
 ('Maverick Pantry','Campus food support and pantry resources for students.','food pantry hunger groceries','https://www.uta.edu/student-affairs/dos'),
 ('Campus Recreation','Campus fitness, recreation and activity resources.','gym fitness recreation exercise sport','https://www.uta.edu/student-affairs/campus-recreation'),
 ('Health Insurance Information','Find student health insurance information and requirements.','insurance coverage health policy','https://www.uta.edu/student-affairs/health-services'),
 ('Relationship Violence & Sexual Assault Prevention','Locate university prevention and support resources.','relationship violence assault prevention support','https://www.uta.edu/student-affairs/rvsp'),
 ('Student Outreach & Support','Find support navigating personal difficulties affecting studies.','personal difficulty outreach support crisis','https://www.uta.edu/student-affairs/dos'),
 ],
 'International':[
 ('International Student & Scholar Services','Immigration advising resources for current international students.','visa immigration f1 j1 i20 sevis international','https://www.uta.edu/student-affairs/oie/isss'),
 ('International Employment Guidance','Find international student employment guidance including CPT and OPT.','cpt opt employment authorization international','https://www.uta.edu/student-affairs/oie/isss'),
 ('Study Abroad','Explore study abroad programs and planning resources.','study abroad exchange overseas','https://www.uta.edu/student-affairs/oie'),
 ('International Orientation','Orientation resources for incoming international students.','international orientation arrival welcome','https://www.uta.edu/student-affairs/nstfp/new-student/international'),
 ('English Language Resources','Find English language learning and language support information.','english language speaking language learning','https://www.uta.edu/'),
 ],
 'Technology':[
 ('OIT Help Desk','Technical help with campus accounts, Wi-Fi and software.','it wifi password computer login netid technology','https://oit.uta.edu/'),
 ('Canvas Support','Find help accessing Canvas and online course materials.','canvas online course assignment learning','https://www.uta.edu/administration/crtle/'),
 ('Student Software','Find information about university-supported software access.','software microsoft office applications download','https://oit.uta.edu/'),
 ('Computer Labs','Find campus computing and student computer lab information.','computer lab desktop workstation','https://oit.uta.edu/'),
 ('Library Technology Lending','Explore available technology lending and equipment resources.','borrow laptop technology equipment camera','https://libraries.uta.edu/'),
 ],
 'Campus life':[
 ('University Housing','Campus housing, residence hall and housing application resources.','housing dorm residence apartment','https://www.uta.edu/campus-ops/housing'),
 ('Dining Services','Campus dining locations and meal plan information.','dining meal plan cafeteria restaurant','https://dineoncampus.com/utarlington'),
 ('Parking & Transportation','Parking permits, campus transportation and mobility information.','parking permit shuttle transport bus','https://www.uta.edu/pats'),
 ('Mav Express','Find information about your student identification card.','mav id card identification express','https://www.uta.edu/campus-ops/mavexpress'),
 ('Student Organizations','Explore campus organizations and student involvement.','clubs organizations involvement join','https://www.uta.edu/student-affairs/student-organizations'),
 ('New Student Orientation','Orientation and transition resources for new students.','orientation freshman transfer new student','https://www.uta.edu/student-affairs/nstfp'),
 ('Student Governance','Learn about student government and campus representation.','student government representation senate','https://www.uta.edu/student-affairs/student-governance'),
 ('Multicultural Affairs','Campus programs and resources supporting a diverse student community.','multicultural diversity cultural inclusion','https://www.uta.edu/student-affairs/multicultural-affairs'),
 ('Parent & Family Programs','Resources for families supporting UTA students.','parent family support','https://www.uta.edu/student-affairs/nstfp'),
 ],
 'Career & support':[
 ('Career Development Center','Career advising, resumes, internships and job-search resources.','career resume internship job interview','https://www.uta.edu/student-affairs/careers'),
 ('Student Employment','Find information about on-campus student jobs and employment.','student job on campus employment work','https://www.uta.edu/student-affairs/careers'),
 ('Dean of Students','Support with student concerns and university resource navigation.','dean student concern support','https://www.uta.edu/student-affairs/dos'),
 ('Student Conduct','Information about student conduct policies and processes.','conduct policy disciplinary appeal','https://www.uta.edu/student-affairs/conduct'),
 ('University Police Resources','Non-emergency campus safety information and police resources.','police safety lost property security','https://www.uta.edu/campus-ops/police'),
 ]}

def seed(db):
    added=0
    for category,entries in GROUPS.items():
        c=db.scalar(select(Category).where(Category.name==category))
        if not c: c=Category(name=category);db.add(c);db.flush()
        for name,description,tags,url in entries:
            if db.scalar(select(Service.id).where(Service.name==name)): continue
            s=Service(name=name,description=description,category_id=c.id,location='Check the official resource page',hours='Check current hours on the official page',contact='Use the contact details on the official page',source_url=url,tags=tags.split(),next_steps=['Open the official resource page and review current information.','Use the contact method listed there to confirm your next step.'],verified=False)
            embed(s);db.add(s);added+=1
    db.commit()
    from .knowledge import seed_knowledge
    seed_knowledge(db)
    return added
if __name__=='__main__':
    with SessionLocal() as db: print(f'Added {seed(db)} draft services. Review sources before marking verified.')
