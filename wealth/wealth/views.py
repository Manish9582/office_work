from django.shortcuts import render

def deshboard(request):
    return render(request, "pages/dashboard.html")

def global_nav_context(request):
    nav_items = [
        {'url': '/', 'icon': '<i class="fa-solid fa-table-cells-large"></i>', 'label': 'Dashboard', 'highlight': True},
        {'url': '/mutual-funds', 'icon': '★', 'label': 'Mutual Funds'},
        {'url': '/api-funds', 'icon': '📁', 'label': 'Funds'},
        {'url': '/stocks', 'icon': '📈', 'label': 'Stocks'},
        {'url': '/bonds', 'icon': '📄', 'label': 'Bonds'},
        {'url': '/mlds', 'icon': '📊', 'label': 'Market Linked Debentures'},
        {'url': '/fixed-deposits', 'icon': '💲', 'label': 'Fixed Deposits'},
        {'url': '/post-office', 'icon': '📫', 'label': 'Post Office Schemes'},
        {'url': '/insurance', 'icon': '🛡️', 'label': 'Insurance Plans'},
        {'url': '/aifs', 'icon': '📊', 'label': 'AIFs'}
    ]
    calculators = [
        {'name': 'Retirement Planning', 'icon': '🏠','function':'RetirementPlan()'},
        {'name': 'Loan Calculator', 'icon': '🏡' ,'function':'LoanCalculator()'},
        {'name': 'Goal Planning', 'icon': '🎯' ,'function':'GoalPlanning()'},
        {'name': 'RD Calculator', 'icon': '💰','function':'RDCalculator()'},
        {'name': 'Future Money', 'icon': '📈','function':'FutureMoneyCalculator()'},
        {'name': 'Salary Calculator', 'icon': '💼','function':'SalaryCalculator()'},
        {'name': 'Capital Gain', 'icon': '📊','function':'CapitalGainCalculator()'},
        {'name': 'Surrender Value', 'icon': '🛡️','function':'SurrenderValueCalculator()'},
    ]
    return {
        'nav_items': nav_items,
        'calculators': calculators
    }


def mutual_funds(request):
    return render(request, "pages/mutualFun.html")



def justtry(request):
    return render(request, "components/calculators/goal.html")
