from django.core.exceptions import ValidationError

MAX_IMAGE_SIZE_MB = 5

IMAGE_TYPE = {
    'png': 'image/png',
    'jpg': 'image/jpg',
    'jpeg': 'image/jpeg'
}


def validate_image(image):
    """Валидация фотографии по размер и формату."""
    max_upload_size_kb = MAX_IMAGE_SIZE_MB * 2 ** 20

    if image.content_type not in IMAGE_TYPE.values():
        raise ValidationError(
            f'Тип загружаемого файла не поддерживается.',
        )

    if image.size > max_upload_size_kb:
        raise ValidationError(
            f'Фотография не должна привышать {MAX_IMAGE_SIZE_MB} MB.',
        )
