def readiness_score(employee, course):
    return min(100, 50 + len(set(employee.interests or []) & set(course.tags or [])) * 10)
