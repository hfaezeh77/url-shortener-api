
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import secrets
import string
from django.shortcuts import redirect
from .db import url_collection
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

url_store = {}


@api_view(["GET"])
def hello(request):
    return Response({
        "message": "Hello! My URL Shortener API is working."
    })



@api_view(["POST"])
def shorten_url(request):
    original_url = request.data.get("url")

    if not original_url:
        return Response(
            {"error": "The url field is required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        URLValidator()(original_url)
    except ValidationError:
        return Response(
            {"error": "Please provide a valid URL."},
            status=status.HTTP_400_BAD_REQUEST
    )
    characters = string.ascii_letters + string.digits
    short_code = "".join(
        secrets.choice(characters) for _ in range(6)
    )

    url_collection.insert_one({
        "short_code": short_code,
        "original_url": original_url
    })

    return Response({
        "original_url": original_url,
        "short_code": short_code,
        "short_url": f"http://127.0.0.1:8000/{short_code}/"
    }, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def redirect_url(request, short_code):
    url_document = url_collection.find_one({
        "short_code": short_code
    })

    if not url_document:
        return Response(
            {"error": "Short URL not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    return redirect(url_document["original_url"])