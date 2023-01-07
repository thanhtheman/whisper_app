from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginating (request, collection, number_of_results_per_page):
    page = request.GET.get('page')
    p = Paginator(collection, number_of_results_per_page)
    try:
        results_per_page = p.page(page)
    except PageNotAnInteger:
        page = 1
        results_per_page = p.page(page)
    except EmptyPage:
        page = p.num_pages
        results_per_page = p.page(page)

    left_index = int(page) - 1
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 2
    if right_index > p.num_pages:
        right_index = p.num_pages + 1
    custom_range = range(left_index, right_index)

    return custom_range, results_per_page 