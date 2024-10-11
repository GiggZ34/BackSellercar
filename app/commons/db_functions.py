from django.db.models import Subquery, PositiveIntegerField


class SubqueryCount(Subquery):
    template = "(SELECT COUNT(*) FROM (%(subquery)s) _count)"
    output_field = PositiveIntegerField()


class SubquerySum(Subquery):
    template = "(SELECT SUM(value) FROM (%(subquery)s) _sum)"
    output_field = PositiveIntegerField()
