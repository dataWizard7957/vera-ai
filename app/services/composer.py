import json
import time
from app.services.prompt_builder import build_prompt
from app.services.llm_service import generate
from app.services.validator import validate_response

from app.services.scorer import score_message
from app.services.hallucination import has_hallucination

from app.services.formatter import (
    normalize_message
)

from app.services.cta_selector import (
    enforce_cta_diversity
)

from app.utils.logger import logger


FALLBACK_MESSAGE = {
    "body": (
        "Customer engagement has slowed recently. "
        "A simple recall campaign may help improve repeat visits. "
        "Want me to draft it?"
    ),
    "cta": "Reply YES",
    "send_as": "whatsapp",
    "suppression_key": "fallback_message",
    "rationale": (
        "Fallback response due to generation failure."
    )
}


def compose_message(context: dict):
    start_time = time.time()
    prompt = build_prompt(context)

    best_message = None
    best_score = -999

    # Multi-candidate generation
    
    for _ in range(1):
        generation_start = time.time()

        try:

            raw_output = generate(prompt)
            logger.info(
                f"Generation took: "
                f"{time.time() - generation_start:.2f}s"
            )

            # Empty response handling
            if not raw_output or not raw_output.strip():

                logger.warning(
                    "Empty LLM response detected"
                )

                continue

            parsed = json.loads(raw_output)

        except Exception as e:

            logger.warning(
                f"Generation/parsing failed: {str(e)}"
            )

            continue

        # Required field validation
        required_fields = [
            "body",
            "cta",
            "send_as",
            "suppression_key",
            "rationale"
        ]

        missing_fields = [
            field for field in required_fields
            if field not in parsed
        ]

        if missing_fields:

            logger.warning(
                f"Missing required fields: {missing_fields}"
            )

            continue

        # Hallucination filter
        if has_hallucination(
            parsed.get("body", "")
        ):

            logger.warning(
                "Hallucination filter triggered"
            )

            continue

        # Quality scoring
        score = score_message(
            parsed,
            context
        )

        logger.info(
            f"Candidate scored: {score}"
        )

        # Keep best candidate
        if score > best_score:

            best_score = score
            best_message = parsed

    # Final fallback
    if not best_message:

        logger.warning(
            "All candidates failed. Using fallback."
        )

        best_message = FALLBACK_MESSAGE

    # Normalize formatting
    formatted = normalize_message(
        best_message
    )

    # Improve CTA diversity
    formatted = enforce_cta_diversity(
        formatted
    )

    # Final validation
    validated = validate_response(
        formatted
    )

    logger.info(
    f"Total compose_message time: "
    f"{time.time() - start_time:.2f}s"
)

    return validated
