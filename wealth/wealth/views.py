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
        {'name': 'Retirement Planning', 'icon': '🏠'},
        {'name': 'Loan Calculator', 'icon': '🏡'},
        {'name': 'Goal Planning', 'icon': '🎯'},
        {'name': 'RD Calculator', 'icon': '💰'},
        {'name': 'Future Money', 'icon': '📈'},
        {'name': 'Salary Calculator', 'icon': '💼'},
        {'name': 'Capital Gain', 'icon': '📊'},
        {'name': 'Surrender Value', 'icon': '🛡️'},
    ]
    return {
        'nav_items': nav_items,
        'calculators': calculators
    }


def mutual_funds(request):
    return render(request, "pages/mutualFun.html")



def justtry(request):
    return render(request, "components/calculators/goal.html")
