def build_conversation_id(
    merchant_id: str,
    trigger_id: str
):

    return (
        f"conv_{merchant_id}_{trigger_id}"
    )


def build_suppression_key(
    trigger_id: str,
    merchant_id: str,
    customer_id=None
):

    trigger_id = trigger_id.lower()

    # Customer-specific recall
    if customer_id:

        return (
            f"recall:{customer_id}:{trigger_id}"
        )

    # Research campaigns
    if "research" in trigger_id:

        return (
            f"research:{merchant_id}:{trigger_id}"
        )

    # Performance dips
    if "perf" in trigger_id:

        return (
            f"performance:{merchant_id}:{trigger_id}"
        )

    # Generic fallback
    return (
        f"{trigger_id}:{merchant_id}"
    )


def build_template_name(
    trigger_id: str
):

    trigger_id = trigger_id.lower()

    if "research" in trigger_id:

        return (
            "vera_research_digest_v1"
        )

    if "recall" in trigger_id:

        return (
            "merchant_recall_reminder_v1"
        )

    if "perf" in trigger_id:

        return (
            "vera_growth_reactivation_v1"
        )

    return (
        "vera_growth_message_v1"
    )


def build_template_params(
    context: dict
):

    params = []

    merchant_name = (
        context.get("merchant_name")
    )

    customer_name = (
        context.get("customer_name")
    )

    if customer_name:

        params.append(customer_name)

    if merchant_name:

        params.append(merchant_name)

    return params
