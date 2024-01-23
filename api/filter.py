from rest_framework.filters import BaseFilterBackend


class ConsumerFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        min_previous_jobs_count = request.query_params.get("min_previous_jobs_count", None)
        max_previous_jobs_count = request.query_params.get("max_previous_jobs_count", None)
        previous_jobs_count = request.query_params.get("previous_jobs_count", None)
        status = request.query_params.get("status", None)

        if min_previous_jobs_count and not previous_jobs_count:
            queryset = queryset.filter(previous_jobs_count__gte=min_previous_jobs_count)
        if max_previous_jobs_count and not previous_jobs_count:
            queryset = queryset.filter(previous_jobs_count__lte=max_previous_jobs_count)
        if previous_jobs_count:
            queryset = queryset.filter(previous_jobs_count=previous_jobs_count)
        if status:
            queryset = queryset.filter(status=status)
        return queryset
