from django.shortcuts import render

def main(request):
    return render(request, 'base/calculator.html')

def calculator(request):
    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operator = request.POST.get('operator')

        # Convert to integers (or float if needed)
        try:
            num1 = float(num1)
            num2 = float(num2)
        except (TypeError, ValueError):
            return render(request, 'base/calculator.html', {'result': 'Invalid input!'})

        if operator == 'add':
            result = num1 + num2
        elif operator == 'sub':
            result = num1 - num2
        elif operator == 'mul':
            result = num1 * num2
        elif operator == 'div':
            if num2 == 0:
                result = 'Cannot divide by zero'
            else:
                result = num1 / num2
        else:
            result = 'Invalid operator'

        return render(request, 'base/calculator.html', {'result': result})
    
    # If GET method
    return render(request, 'base/calculator.html')
