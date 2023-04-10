from django.core.exceptions import ValidationError
import os


def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extension = ['.jpg', '.png', '.jpeg']

    if not ext.lower() in valid_extension:
        raise ValidationError(f"Unsupported file extension. Allowed extension: {valid_extension}") 