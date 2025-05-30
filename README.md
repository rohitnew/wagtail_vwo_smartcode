# Wagtail VWO SmartCode

A Wagtail plugin that injects VWO (Visual Website Optimizer) SmartCode into your Wagtail pages for A/B testing.

## Installation

1. Copy `wagtail_vwo_smartcode.zip` into your Docker image.
2. Add `RUN pip install wagtail_vwo_smartcode.zip` to your Dockerfile.

## Usage

Add to `INSTALLED_APPS`, include the context processor, and insert the template into your base HTML.
