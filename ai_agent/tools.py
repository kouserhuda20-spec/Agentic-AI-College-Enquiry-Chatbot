
import re

from django.db.models import Q
from langchain_core.tools import tool

from college_chatbot.models import College
from .rag_engine import rag_query


# ==========================================
# COMMON COLLEGE SEARCH FUNCTION
# ==========================================

STOP_WORDS = {
    "the", "a", "an", "of", "in", "for", "and",
    "college", "institute", "university", "technology",
    "engineering", "give", "me", "full", "details",
    "about", "information", "including", "please"
}


def normalize(text):
    """Convert text into lowercase alphanumeric words."""
    return re.sub(r"[^a-z0-9]", " ", str(text).lower()).strip()


def find_college(query):
    """Find the best matching college using its name and abbreviation."""

    query_normalized = normalize(query)
    query_tokens = set(query_normalized.split())

    if not query_tokens:
        return None

    colleges = list(College.objects.all())

    best_college = None
    best_score = 0

    for college in colleges:
        name = college.name or ""
        normalized_name = normalize(name)
        name_tokens = set(normalized_name.split())

        # Extract abbreviations inside brackets, e.g. RNSIT, CMRIT
        abbreviations = re.findall(r"\(([^)]+)\)", name)

        score = 0

        # Exact full-name match
        if normalized_name and normalized_name in query_normalized:
            score += 100

        # Exact abbreviation match
        for abbreviation in abbreviations:
            alias = normalize(abbreviation)

            if alias and alias in query_tokens:
                score += 100

        # Match distinctive college-name words
        important_name_words = name_tokens - STOP_WORDS
        important_query_words = query_tokens - STOP_WORDS

        common_words = important_name_words & important_query_words

        score += len(common_words) * 15

        # Prefer matches with more of the college's distinctive words
        if important_name_words:
            score += (
                len(common_words) / len(important_name_words)
            ) * 30

        if score > best_score:
            best_score = score
            best_college = college

    if best_score >= 30:
        return best_college

    return None


def college_details(college):
    """Format college information from the database."""

    return f"""
College: {college.name}
Location: {college.location}
Description: {college.description}
Courses: {college.courses}
Courses Offered: {college.courses_offered}
Fees: {college.fees}
KCET Fees: {college.kcet_fee}
COMEDK Fees: {college.comedk_fee}
Management Fees: {college.management_fee}
KCET Cutoff: {college.kcet_cutoff}
COMEDK Cutoff: {college.comedk_cutoff}
Average Package: {college.average_package}
Highest Package: {college.highest_package}
Website: {college.website}
Phone: {college.contact_phone}
Email: {college.contact_email}
"""


# ==========================================
# TOOL 1: SEARCH COLLEGE INFORMATION
# ==========================================

@tool
def get_college_info(query: str) -> str:
    """
    Find college information using college names,
    abbreviations, locations, fees, courses and placements.
    """

    try:
        college = find_college(query)

        if college:
            return college_details(college)

        # If no college name matches, search other database fields.
        words = [
            word for word in normalize(query).split()
            if len(word) > 2 and word not in STOP_WORDS
        ]

        if not words:
            return "Please provide a college name or keyword."

        search_query = Q()

        fields = [
            "location",
            "description",
            "courses",
            "courses_offered",
        ]

        for word in words:
            for field in fields:
                search_query |= Q(**{f"{field}__icontains": word})

        colleges = College.objects.filter(
            search_query
        ).distinct()[:5]

        if not colleges:
            return "No matching college information found in the database."

        return "\n\n".join(
            college_details(c) for c in colleges
        )

    except Exception as e:
        return f"College search error: {str(e)}"


# ==========================================
# TOOL 2: COMPARE TWO COLLEGES
# ==========================================

@tool
def compare_colleges(college1: str, college2: str) -> str:
    """
    Compare two colleges using Django database records.
    Supports full names and abbreviations.
    """

    try:
        first = find_college(college1)
        second = find_college(college2)

        if not first:
            return f"College not found: {college1}"

        if not second:
            return f"College not found: {college2}"

        if first.id == second.id:
            return "Please provide two different colleges to compare."

        fields = [
            ("Location", "location"),
            ("Courses", "courses_offered"),
            ("KCET Fees", "kcet_fee"),
            ("COMEDK Fees", "comedk_fee"),
            ("Management Fees", "management_fee"),
            ("KCET Cutoff", "kcet_cutoff"),
            ("COMEDK Cutoff", "comedk_cutoff"),
            ("Average Package", "average_package"),
            ("Highest Package", "highest_package"),
        ]

        results = [
            f"COLLEGE COMPARISON",
            f"College 1: {first.name}",
            f"College 2: {second.name}",
            ""
        ]

        for label, field in fields:
            value1 = getattr(first, field, None) or "Not Available"
            value2 = getattr(second, field, None) or "Not Available"

            results.append(
                f"{label}: {first.name} = {value1} | "
                f"{second.name} = {value2}"
            )

        return "\n".join(results)

    except Exception as e:
        return f"Comparison error: {str(e)}"


# ==========================================
# TOOL 3: SEMANTIC RAG SEARCH
# ==========================================

@tool
def search_college_knowledge(query: str) -> str:
    """
    Search college documents using semantic RAG retrieval.
    Use for additional admission, course, fee and placement knowledge.
    """

    try:
        result = rag_query(query)

        if not result:
            return "No relevant college information found."

        return result

    except Exception as e:
        return f"RAG search error: {str(e)}"


# ==========================================
# REGISTER AI TOOLS
# ==========================================

tools = [
    get_college_info,
    compare_colleges,
    search_college_knowledge
]
