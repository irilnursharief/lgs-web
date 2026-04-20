from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def index(request):
    return render(request, "index.html", {"form": ContactForm()})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Build email content
            subject = f"New Inquiry from {data['full_name']} — {data['company_name']}"
            message = render_to_string("emails/contact_email.txt", {"data": data})

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.CONTACT_RECIPIENTS,
                    fail_silently=False,
                )
                return JsonResponse({"status": "success"})
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)}, status=500)
        else:
            return JsonResponse(
                {"status": "invalid", "errors": form.errors}, status=400
            )

    return JsonResponse({"status": "method_not_allowed"}, status=405)
