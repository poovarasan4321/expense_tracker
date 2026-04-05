from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction
from .forms import TransactionForm
import csv
from django.http import HttpResponse

# DASHBOARD


@login_required
def dashboard(request):
    data = Transaction.objects.filter(user=request.user)

    credit = data.filter(type='Credit').aggregate(
        Sum('amount'))['amount__sum'] or 0
    debit = data.filter(type='Debit').aggregate(
        Sum('amount'))['amount__sum'] or 0

    return render(request, 'dashboard.html', {
        'transactions': data,
        'credit': credit,
        'debit': debit,
        'balance': credit - debit
    })

# ADD EXPENSE


@login_required
def add_expense(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/')
    return render(request, 'add_expense.html', {'form': form})

# REPORT + FILTER


@login_required
def report(request):
    data = Transaction.objects.filter(user=request.user)

    date = request.GET.get('date')
    month = request.GET.get('month')
    year = request.GET.get('year')

    if date:
        data = data.filter(date=date)
    if month:
        data = data.filter(date__month=month)
    if year:
        data = data.filter(date__year=year)

    total = data.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'report.html', {
        'transactions': data,
        'total': total
    })

# DOWNLOAD CSV


@login_required
def download_report(request):
    data = Transaction.objects.filter(user=request.user)

    date = request.GET.get('date')
    month = request.GET.get('month')
    year = request.GET.get('year')

    if date:
        data = data.filter(date=date)
    if month:
        data = data.filter(date__month=month)
    if year:
        data = data.filter(date__year=year)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Amount', 'Type', 'Category', 'Description', 'Date'])

    for i in data:
        writer.writerow([i.amount, i.type, i.category, i.description, i.date])

    return response


@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Transaction, id=id, user=request.user)

    if request.method == 'POST':
        expense.amount = request.POST.get('amount')
        expense.type = request.POST.get('type')
        expense.category = request.POST.get('category')
        expense.description = request.POST.get('description')
        expense.date = request.POST.get('date')

        expense.save()
        return redirect('dashboard')

    return render(request, 'edit.html', {'expense': expense})


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Transaction, id=id, user=request.user)

    if request.method == "POST":
        expense.delete()
        return redirect('dashboard')

    return redirect('dashboard')