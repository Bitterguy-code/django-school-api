from django.core.exceptions import ValidationError

def validate_subject_format(subject):
    error_message = "Subject must be in title case format."
    good_subject = (subject == subject.title())
    
    if good_subject:
        return subject
    else:
        raise ValidationError(error_message)
    
def validate_professor_name(professor):
    error_message = 'Professor name must be in the format "Professor Adam".'
    good_professor = (professor == professor.title()) & (professor.startswith('Professor'))
    
    if good_professor:
        return professor
    else:
        raise ValidationError(error_message)