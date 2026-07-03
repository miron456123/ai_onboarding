def suggest_next_step(employee, courses):
    return f"{employee.name}: начните с курса «{courses[0].title}»." if courses else 'Каталог курсов пуст.'
