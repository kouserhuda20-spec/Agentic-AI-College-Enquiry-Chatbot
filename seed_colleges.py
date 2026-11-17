
import os
import django

# Setup Django environment before importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from college_chatbot.models import College


colleges_data = [
    {
        "name": "RV College of Engineering (RVCE)",
        "location": "Mysuru Road, Bengaluru",
        "established_year": "1963",
        "website": "https://rvce.edu.in",
        "contact_email": "admissions@rvce.edu.in",
        "contact_phone": "+91-80-68188100",
        "kcet_cutoff": "280",
        "comedk_cutoff": "450",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 3.25 Lakh/Yr",
        "management_fee": "Rs 12-18 Lakh/Yr",
        "average_package": "11.5 LPA",
        "highest_package": "62 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Data Science, ECE, ISE, Civil, Mechanical, Biotechnology, Aerospace"
    },
    {
        "name": "BMS College of Engineering (BMSCE)",
        "location": "Basavanagudi, Bengaluru",
        "established_year": "1946",
        "website": "https://bmsce.ac.in",
        "contact_email": "admissions@bmsce.ac.in",
        "contact_phone": "+91-80-26622130",
        "kcet_cutoff": "650",
        "comedk_cutoff": "900",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 3.00 Lakh/Yr",
        "management_fee": "Rs 10-15 Lakh/Yr",
        "average_package": "9.8 LPA",
        "highest_package": "50 LPA",
        "courses_offered": "B.Tech CSE, ECE, ISE, AI & DS, Electrical, Mechanical, Chemical, Medical Electronics"
    },
    {
        "name": "Ramaiah Institute of Technology (MSRIT)",
        "location": "MSR Nagar, Mathikere, Bengaluru",
        "established_year": "1962",
        "website": "https://msrit.edu",
        "contact_email": "admissions@msrit.edu",
        "contact_phone": "+91-80-23600822",
        "kcet_cutoff": "850",
        "comedk_cutoff": "1100",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 3.00 Lakh/Yr",
        "management_fee": "Rs 10-14 Lakh/Yr",
        "average_package": "9.5 LPA",
        "highest_package": "50 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Cyber Security, ECE, ISE, Civil, Mechanical, Industrial Engineering"
    },
    {
        "name": "PES University (PESU - RR Campus)",
        "location": "100 Feet Ring Road, Banashankari 3rd Stage, Bengaluru",
        "established_year": "1972",
        "website": "https://pes.edu",
        "contact_email": "admissions@pes.edu",
        "contact_phone": "+91-80-26721983",
        "kcet_cutoff": "700",
        "comedk_cutoff": "PESSAT Entrance",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "PESSAT: Rs 4.50 Lakh/Yr",
        "management_fee": "Rs 11-16 Lakh/Yr",
        "average_package": "12.0 LPA",
        "highest_package": "65 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, ECE, Electrical, Mechanical, Biotechnology"
    },
    {
        "name": "International Institute of Information Technology Bengaluru (IIIT-B)",
        "location": "Electronic City Phase 1, Bengaluru",
        "established_year": "1999",
        "website": "https://iiitb.ac.in",
        "contact_email": "admissions@iiitb.ac.in",
        "contact_phone": "+91-80-41407777",
        "kcet_cutoff": "JEE Main Rank (< 9000)",
        "comedk_cutoff": "N/A",
        "kcet_fee": "Rs 4.00 Lakh/Yr",
        "comedk_fee": "Rs 4.00 Lakh/Yr",
        "management_fee": "N/A (Merit Only)",
        "average_package": "24.5 LPA",
        "highest_package": "81 LPA",
        "courses_offered": "Integrated M.Tech CSE, Integrated M.Tech ECE, B.Tech CSE"
    },
    {
        "name": "Bangalore Institute of Technology (BIT)",
        "location": "VV Puram, K.R. Road, Bengaluru",
        "established_year": "1979",
        "website": "https://bit-bangalore.edu.in",
        "contact_email": "principal@bit-bangalore.edu.in",
        "contact_phone": "+91-80-26615865",
        "kcet_cutoff": "2100",
        "comedk_cutoff": "3500",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.80 Lakh/Yr",
        "management_fee": "Rs 8-12 Lakh/Yr",
        "average_package": "7.2 LPA",
        "highest_package": "37.5 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Data Science, ECE, ISE, EEE, Civil, Mechanical"
    },
    {
        "name": "University Visvesvaraya College of Engineering (UVCE)",
        "location": "K.R. Circle, Bengaluru",
        "established_year": "1917",
        "website": "https://uvce.ac.in",
        "contact_email": "principal@uvce.ac.in",
        "contact_phone": "+91-80-22961803",
        "kcet_cutoff": "1200",
        "comedk_cutoff": "Govt Only (KCET)",
        "kcet_fee": "Rs 45,000/Yr",
        "comedk_fee": "N/A",
        "management_fee": "N/A (Pure Govt)",
        "average_package": "8.5 LPA",
        "highest_package": "58 LPA",
        "courses_offered": "B.Tech CSE, ECE, ISE, Electrical, Mechanical, Civil, Architecture"
    },
    {
        "name": "Dayananda Sagar College of Engineering (DSCE)",
        "location": "Kumaraswamy Layout, Bengaluru",
        "established_year": "1979",
        "website": "https://dayanandasagar.edu",
        "contact_email": "admissions@dayanandasagar.edu",
        "contact_phone": "+91-80-42161750",
        "kcet_cutoff": "2800",
        "comedk_cutoff": "4200",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.80 Lakh/Yr",
        "management_fee": "Rs 7-11 Lakh/Yr",
        "average_package": "7.5 LPA",
        "highest_package": "40 LPA",
        "courses_offered": "B.Tech CSE, Cyber Security, AI & ML, ECE, ISE, Aeronautical, Medical Electronics, Automobile"
    },
    {
        "name": "BMS Institute of Technology and Management (BMSIT)",
        "location": "Avalahalli, Yelahanka, Bengaluru",
        "established_year": "2002",
        "website": "https://bmsit.ac.in",
        "contact_email": "principal@bmsit.in",
        "contact_phone": "+91-80-68730429",
        "kcet_cutoff": "3500",
        "comedk_cutoff": "5200",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.80 Lakh/Yr",
        "management_fee": "Rs 6-9 Lakh/Yr",
        "average_package": "7.0 LPA",
        "highest_package": "44 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Data Science, ECE, ISE, Electrical, Civil, Mechanical"
    },
    {
        "name": "Nitte Meenakshi Institute of Technology (NMIT)",
        "location": "Yelahanka, Bengaluru",
        "established_year": "2001",
        "website": "https://nmit.ac.in",
        "contact_email": "admissions@nmit.ac.in",
        "contact_phone": "+91-80-22167800",
        "kcet_cutoff": "4500",
        "comedk_cutoff": "6800",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.80 Lakh/Yr",
        "management_fee": "Rs 6-8.5 Lakh/Yr",
        "average_package": "6.8 LPA",
        "highest_package": "41 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Data Science, Aeronautical, ECE, ISE, Civil, Mechanical"
    },
    {
        "name": "RNS Institute of Technology (RNSIT)",
        "location": "Channasandra, Uttarahalli Main Road, Bengaluru",
        "established_year": "2001",
        "website": "https://rnsit.ac.in",
        "contact_email": "admissions@rnsit.ac.in",
        "contact_phone": "+91-80-28611880",
        "kcet_cutoff": "4800",
        "comedk_cutoff": "7200",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.60 Lakh/Yr",
        "management_fee": "Rs 5.5-8 Lakh/Yr",
        "average_package": "6.4 LPA",
        "highest_package": "56 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Cyber Security, ECE, ISE, Instrumentation, EEE"
    },
    {
        "name": "New Horizon College of Engineering (NHCE)",
        "location": "Outer Ring Road, Marathahalli, Bengaluru",
        "established_year": "2001",
        "website": "https://newhorizonindia.edu",
        "contact_email": "admissionsnhce@newhorizonindia.edu",
        "contact_phone": "+91-80-66297777",
        "kcet_cutoff": "5500",
        "comedk_cutoff": "8500",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.80 Lakh/Yr",
        "management_fee": "Rs 6-9 Lakh/Yr",
        "average_package": "6.5 LPA",
        "highest_package": "28 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, ECE, ISE, Electrical, Mechanical, Civil"
    },
    {
        "name": "CMR Institute of Technology (CMRIT)",
        "location": "ITPL Main Road, Kundalahalli, Bengaluru",
        "established_year": "2000",
        "website": "https://cmrit.ac.in",
        "contact_email": "info@cmrit.ac.in",
        "contact_phone": "+91-80-28524466",
        "kcet_cutoff": "6200",
        "comedk_cutoff": "9200",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.60 Lakh/Yr",
        "management_fee": "Rs 5-8 Lakh/Yr",
        "average_package": "6.3 LPA",
        "highest_package": "26.5 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Data Science, ECE, ISE, EEE, Civil, Mechanical"
    },
    {
        "name": "REVA University",
        "location": "Rukmini Knowledge Park, Kattigenahalli, Yelahanka, Bengaluru",
        "established_year": "2012",
        "website": "https://reva.edu.in",
        "contact_email": "admissions@reva.edu.in",
        "contact_phone": "+91-80-46966966",
        "kcet_cutoff": "7800",
        "comedk_cutoff": "11500",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.60 Lakh/Yr",
        "management_fee": "Rs 3.5 - 5.5 Lakh/Yr",
        "average_package": "6.0 LPA",
        "highest_package": "58 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, Robotics & Automation, Cyber Security, ECE, Electrical, Civil, Mechanical"
    },
    {
        "name": "Garden City University (GCU)",
        "location": "16th KM, Old Madras Road, Bengaluru",
        "established_year": "2013",
        "website": "https://gardencity.university",
        "contact_email": "admissions@gardencity.university",
        "contact_phone": "+91-80-66487600",
        "kcet_cutoff": "Direct / University Entrance",
        "comedk_cutoff": "Direct / University Entrance",
        "kcet_fee": "Rs 2.50 Lakh/Yr",
        "comedk_fee": "Rs 2.50 Lakh/Yr",
        "management_fee": "Rs 2.50 - 3.50 Lakh/Yr",
        "average_package": "6.5 LPA",
        "highest_package": "22 LPA",
        "courses_offered": "B.Tech CSE, Data Science, Cyber Security, AI & ML, Biotechnology"
    },
    {
        "name": "JSS Academy of Technical Education (JSSATE)",
        "location": "JSSATE Campus, Uttarahalli Road, Bengaluru",
        "established_year": "1997",
        "website": "https://jssateb.ac.in",
        "contact_email": "info@jssateb.ac.in",
        "contact_phone": "+91-80-28612565",
        "kcet_cutoff": "7100",
        "comedk_cutoff": "10500",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.60 Lakh/Yr",
        "management_fee": "Rs 4.5-7.5 Lakh/Yr",
        "average_package": "6.1 LPA",
        "highest_package": "43 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, ECE, ISE, Robotics & Automation, Civil, Mechanical"
    },
    {
        "name": "MVJ College of Engineering (MVJCE)",
        "location": "Near ITPL, Whitefield, Bengaluru",
        "established_year": "1982",
        "website": "https://mvjce.edu.in",
        "contact_email": "contactmvjce@gmail.com",
        "contact_phone": "+91-80-42574000",
        "kcet_cutoff": "9500",
        "comedk_cutoff": "14000",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.60 Lakh/Yr",
        "management_fee": "Rs 4-6.5 Lakh/Yr",
        "average_package": "5.8 LPA",
        "highest_package": "21 LPA",
        "courses_offered": "B.Tech CSE, Aeronautical, Aerospace, AI & ML, ECE, ISE, Chemical, Civil"
    },
    {
        "name": "Sir M. Visvesvaraya Institute of Technology (Sir MVIT)",
        "location": "International Airport Road, Hunasamaranahalli, Bengaluru",
        "established_year": "1986",
        "website": "https://sirmvit.edu",
        "contact_email": "sirmvitbgl@gmail.com",
        "contact_phone": "+91-80-28365345",
        "kcet_cutoff": "6800",
        "comedk_cutoff": "9800",
        "kcet_fee": "Rs 1.75 Lakh/Yr",
        "comedk_fee": "Rs 2.60 Lakh/Yr",
        "management_fee": "Rs 4.5-7 Lakh/Yr",
        "average_package": "6.2 LPA",
        "highest_package": "35 LPA",
        "courses_offered": "B.Tech CSE, AI & ML, ECE, ISE, Electrical, Biotechnology, Civil, Mechanical"
    },
    {
        "name": "Christ University (Faculty of Engineering)",
        "location": "Kumbalgodu, Kengeri Campus, Bengaluru",
        "established_year": "1969",
        "website": "https://christuniversity.in",
        "contact_email": "admissions@christuniversity.in",
        "contact_phone": "+91-80-40129800",
        "kcet_cutoff": "Christ Entrance Test (CUET)",
        "comedk_cutoff": "Christ Entrance Test (CUET)",
        "kcet_fee": "Rs 2.20 Lakh/Yr",
        "comedk_fee": "Rs 2.50 Lakh/Yr",
        "management_fee": "Rs 2.50 - 4.00 Lakh/Yr",
        "average_package": "6.8 LPA",
        "highest_package": "20 LPA",
        "courses_offered": "B.Tech CSE, Data Science, AI & ML, ECE, Automobile, Civil, Mechanical"
    },
    {
        "name": "Alliance University (Alliance College of Engineering)",
        "location": "Chandapura-Anekal Main Road, Bengaluru",
        "established_year": "2010",
        "website": "https://alliance.edu.in",
        "contact_email": "admissions@alliance.edu.in",
        "contact_phone": "+91-80-46199000",
        "kcet_cutoff": "AUSAT / Direct Admission",
        "comedk_cutoff": "AUSAT / Direct Admission",
        "kcet_fee": "Rs 2.50 Lakh/Yr",
        "comedk_fee": "Rs 3.00 Lakh/Yr",
        "management_fee": "Rs 3.00 - 4.50 Lakh/Yr",
        "average_package": "6.0 LPA",
        "highest_package": "16.7 LPA",
        "courses_offered": "B.Tech CSE, AI & Data Science, ECE, Information Technology, Mechanical, Aerospace"
    }
]


print("Populating Bengaluru Colleges into MySQL...")

for data in colleges_data:
    obj, created = College.objects.update_or_create(
        name=data["name"],
        defaults=data
    )

    status = "Created" if created else "Updated"
    print(f"[{status}] {data['name']}")

print(
    f"\nSuccessfully seeded {len(colleges_data)} colleges "
    "into college_enquiry_db!"
)
