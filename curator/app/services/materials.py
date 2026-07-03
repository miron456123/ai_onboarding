def material_summary(course):
    return {'title': course.title, 'outcomes': course.learning_outcomes or []}
