def progress_label(value):
    return 'завершено' if value >= 100 else 'в процессе' if value else 'запланировано'
