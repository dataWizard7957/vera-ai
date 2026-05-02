import re


def normalize_message(
    message: dict
):

    body = message.get(
        "body",
        ""
    ).strip()

    # Remove repeated whitespace
    body = re.sub(
        r"\s+",
        " ",
        body
    )

    # Capitalize first character only
    if body:
        body = body[0].upper() + body[1:]

    message["body"] = body

    return message
