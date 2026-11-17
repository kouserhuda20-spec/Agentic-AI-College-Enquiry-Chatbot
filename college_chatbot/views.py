
import json
import csv

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import College
from ai_agent.agent import query_agent


# APPROVED 15 COLLEGES
APPROVED_COLLEGES = [
    "RV College of Engineering",
    "BMS College of Engineering",
    "Ramaiah Institute of Technology",
    "PES University",
    "International Institute of Information Technology",
    "Bangalore Institute of Technology",
    "University Visvesvaraya College",
    "Dayananda Sagar College",
    "BMS Institute of Technology",
    "Nitte Meenakshi Institute",
    "RNS Institute of Technology",
    "New Horizon College",
    "CMR Institute of Technology",
    "REVA University",
    "Garden City University",
]


# GET ONLY APPROVED COLLEGES
def get_approved_colleges():
    college_query = Q()

    for name in APPROVED_COLLEGES:
        college_query |= Q(name__icontains=name)

    return College.objects.filter(college_query).distinct().order_by("name")


# DASHBOARD - FRONT PAGE
def dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)


# CHATBOT PAGE
def index(request):
    colleges = get_approved_colleges()

    context = {
        "colleges": colleges,
        "total_colleges": colleges.count(),
    }

    return render(request, "index.html", context)


# CHATBOT API
@csrf_exempt
def chat_api(request):

    if request.method != "POST":
        return JsonResponse(
            {"response": "Invalid request method."},
            status=405
        )

    try:
        data = json.loads(request.body.decode("utf-8"))
        user_message = data.get("message", "").strip()

        if not user_message:
            return JsonResponse(
                {"response": "Please enter a valid question."},
                status=400
            )

        bot_response = query_agent(user_message)

        return JsonResponse({
            "response": bot_response
        })

    except Exception as e:
        print("Chat API Error:", str(e))

        return JsonResponse(
            {
                "response": "Sorry, something went wrong. Please try again."
            },
            status=500
        )


# REPORTS PAGE
def reports(request):
    colleges = get_approved_colleges()

    context = {
        "colleges": colleges,
        "total_colleges": colleges.count(),
    }

    return render(request, "reports.html", context)


# EXPORT APPROVED COLLEGES TO CSV
def export_college_csv(request):
    colleges = get_approved_colleges()

    response = HttpResponse(content_type="text/csv")

    response["Content-Disposition"] = (
        'attachment; filename="college_enquiry_report.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        "College Name",
        "Location",
        "Courses",
        "Fees",
        "KCET Fee",
        "COMEDK Fee",
        "Management Fee",
        "KCET Cutoff",
        "COMEDK Cutoff",
        "Average Package",
        "Highest Package",
        "Contact Email",
        "Contact Phone",
        "Website",
    ])

    for college in colleges:
        writer.writerow([
            college.name,
            college.location,
            college.courses,
            college.fees,
            college.kcet_fee,
            college.comedk_fee,
            college.management_fee,
            college.kcet_cutoff,
            college.comedk_cutoff,
            college.average_package,
            college.highest_package,
            college.contact_email,
            college.contact_phone,
            college.website,
        ])

    return response
