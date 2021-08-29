from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def building_materials(request):
    return render(request, 'building-materials.html', {})


def artificial_intelligence(request):
    return render(request, 'artificial-intelligence.html', {})


def computer_hardware_networking(request):
    return render(request, 'computer-hardware-networking.html', {})


def software_testing(request):
    return render(request, 'hosting.html', {})


def app_development(request):
    return render(request, 'app-development.html', {})


def ui_ux_design_analysis(request):
    return render(request, 'ui-ux-design-analysis.html', {})


def website_development(request):
    return render(request, 'website-development.html', {})


def hosting(request):
    return render(request, "hosting.html", {})


def terms(request):
    return render(request, "terms-conditions.html", {})
