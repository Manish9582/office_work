from django.shortcuts import render

def justtry(request):
    return render(request, "components/calculators/goal.html")

def deshboard(request):
    return render(request, "pages/dashboard.html")

def global_nav_context(request):
    nav_items = [
        {'url': '/', 'icon': '<i class="fa-solid fa-table-cells-large"></i>', 'label': 'Dashboard', 'highlight': True},
        {'url': '/mutual-funds', 'icon': '★', 'label': 'Mutual Funds'},
        {'url': '/api-funds', 'icon': '📁', 'label': 'Funds'},
        {'url': '/stocks', 'icon': '📈', 'label': 'Stocks'},
        {'url': '/bonds', 'icon': '📄', 'label': 'Bonds'},
        {'url': '/market', 'icon': '📊', 'label': 'Market Linked Debentures'},
        {'url': '/fixed-deposits', 'icon': '💲', 'label': 'Fixed Deposits'},
        {'url': '/post-office', 'icon': '📫', 'label': 'Post Office Schemes'},
        {'url': '/insurance', 'icon': '🛡️', 'label': 'Insurance Plans'},
        {'url': '/aifs', 'icon': '📊', 'label': 'AIFs'}
    ]
    calculators = [
        {'name': 'Retirement Planning', 'icon': '🏠','function':'toggleCalculator(Retirement)'},
        {'name': 'Loan Calculator', 'icon': '🏡' ,'function':'toggleCalculator(Loan)'},
        {'name': 'Goal Planning', 'icon': '🎯' ,'function':'toggleCalculator(Goal)'},
        {'name': 'RD Calculator', 'icon': '💰','function':'toggleCalculator(RD)'},
        {'name': 'Future Money', 'icon': '📈','function':'toggleCalculator(Future)'},
        {'name': 'Salary Calculator', 'icon': '💼','function':'toggleCalculator(Salary)'},
        {'name': 'Capital Gain', 'icon': '📊','function':'toggleCalculator(Capital)'},
        {'name': 'Surrender Value', 'icon': '🛡️','function':'toggleCalculator(Surrender)'},
    ]
    filtermarket=[
        {'icon': '<i class="fa-solid fa-table-cells-large"></i>', 'title': 'All MLDs'},
        {'icon':'<i class="fa-solid fa-chart-line"></i>','title':'Equity Linked'},
        {'icon':'<i class="fa-solid fa-coins"></i>','title':'Commodity'},
        {'icon':'<i class="fa-solid fa-rupee-sign"></i>','title':'Currency'},
        {'icon':'<i class="fa-solid fa-layer-group"></i>','title':'Hybrid'}
    ]
    return {
        'nav_items': nav_items,
        'calculators': calculators,
        'filler':filtermarket
    }


def mutual_funds(request):
    return render(request, "pages/mutualFun.html")

def fixed_deposit(request):
    return render(request, "pages/fixeddeposit.html")

def post_office(request):
    return render(request, "pages/postoffice.html")

def insurance(request):
    return render(request, "pages/insurance.html")

def aif(request):
    return render(request, "pages/aif.html")

def funds(request):
    return render(request, "pages/funds.html")

def stocks(request):
    return render(request, "pages/stocks.html")

def bonds(request):
    return render(request, "pages/bonds.html")

def market(request):
    return render(request, "pages/market.html")

def chatAi(request):
    return render(request,"pages/maya.html")

def chat(request):
    return render(request,"pages/userChat.html")