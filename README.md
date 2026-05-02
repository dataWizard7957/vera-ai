
# Vera AI Bot

AI-powered merchant engagement and auto-reply system built with FastAPI, OpenAI/Groq LLMs, and trigger-based campaign generation.

## Overview

Vera AI Bot generates contextual WhatsApp-style merchant engagement messages based on business triggers such as:

* Performance spikes or dips
* Festival campaigns
* Customer recall and winback
* Dormancy detection
* Appointment reminders
* Competitor activity
* Seasonal demand shifts
* Loyalty and retention campaigns

The system focuses on:

* Natural conversational messaging
* CTA diversity
* Reduced repetition
* Hallucination control
* Trigger-aware personalization
* Merchant-specific campaign suggestions

---

# Features

* FastAPI backend
* LLM-powered response generation
* OpenAI + Groq support
* Trigger-specific prompting
* CTA selection and diversity logic
* Validation and hallucination checks
* Message suppression support
* Modular service architecture


---

# Tech Stack

* Python 
* FastAPI
* OpenAI SDK
* Groq SDK
* Pydantic v2
* HTTPX
* Docker


---

# Project Structure

```text
app/
├── api/
│   ├── context.py
│   ├── health.py
│   ├── metadata.py
│   ├── reply.py
│   └── tick.py
│
├── models/
│   ├── context_models.py
│   ├── conversation_models.py
│   └── response_models.py
│
├── services/
│   ├── auto_reply.py
│   ├── category_prompts.py
│   ├── composer.py
│   ├── conversation.py
│   ├── cta.py
│   ├── cta_selector.py
│   ├── diversity.py
│   ├── examples.py
│   ├── formatter.py
│   ├── hallucination.py
│   ├── hostility_detector.py
│   ├── intent_detector.py
│   ├── llm_service.py
│   ├── prompt_builder.py
│   ├── scorer.py
│   ├── state_manager.py
│   ├── suppression.py
│   ├── trigger_prompts.py
│   └── validator.py
│
├── store/
│   └── memory_store.py
│
├── utils/
│   └── logger.py
│
├── config.py
└── main.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/vera-ai.git
cd vera-ai
```

## Install Dependencies

```bash
pip install -r requirements.txt
```


---

# API Endpoints

## Health Check

```http
GET /health
```

## Generate Reply

```http
POST /reply
```

## Tick Processing

```http
POST /tick
```

## Metadata

```http
GET /metadata
```

---

# Example Response

```json
{
  "action": "",
  "message": {
    "body": "",
    "cta": "",
    "send_as": "",
    "suppression_key": "",
    "rationale": ""
  }
}
```

---


# Key Design Goals

* Conversational messaging
* Business-context awareness
* Trigger relevance
* Safe and controlled generation
* Modular architecture
* Easy deployment and scaling

---

# Future Improvements

* Redis-backed memory store
* Analytics dashboard
* Multi-language support
* Campaign performance scoring
* A/B testing support
* Conversation history persistence
* Queue-based async processing




