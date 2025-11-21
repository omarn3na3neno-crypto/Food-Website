from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Message

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # إعادة تهيئة الفورم بعد الحفظ
            form = BookingForm()
            success_message = "Booking saved successfully!"
            return render(request, 'reservations/book_table.html', {
                'form': form,
                'success_message': success_message
            })
    else:
        form = BookingForm()

    return render(request, 'reservations/book_table.html', {'form': form})



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        content = request.POST.get("message")
        
        Message.objects.create(
            name_user=name,
            email_user=email,
            subject_user=subject,
            content_user=content
        )
        return redirect('index')  # يعيد تحميل الصفحة بعد الإرسال

    return render(request, 'menu/index.html')